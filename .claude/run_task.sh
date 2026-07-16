#!/usr/bin/env bash
set -euo pipefail

die() {
  printf 'PC CLAUDE STOPPED: %s\n' "$1" >&2
  exit 1
}

usage() {
  printf 'Usage: %s [--push] control/tasks/TASK-*.md\n' "$0"
}

push_branch=false
if [[ "${1:-}" == '--push' ]]; then
  push_branch=true
  shift
fi
[[ $# -eq 1 ]] || { usage >&2; exit 2; }

command -v claude >/dev/null || die 'Claude Code is not installed or not on PATH'
command -v git >/dev/null || die 'Git is not installed or not on PATH'
command -v python3 >/dev/null || die 'Python 3 is not installed or not on PATH'

minimum_claude_version='2.1.208'
claude_version_raw="$(claude --version)"
claude_version="$(printf '%s\n' "$claude_version_raw" | grep -Eo '[0-9]+\.[0-9]+\.[0-9]+' | head -n 1)"
[[ -n "$claude_version" ]] || die 'could not parse the Claude Code version'
oldest="$(printf '%s\n%s\n' "$minimum_claude_version" "$claude_version" | sort -V | head -n 1)"
[[ "$oldest" == "$minimum_claude_version" ]] || die "Claude Code $minimum_claude_version or newer is required"

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(git -C "$script_dir/.." rev-parse --show-toplevel 2>/dev/null)" || die 'launcher is not inside a Git checkout'
repo_root="$(realpath -- "$repo_root")"
cd "$repo_root"

"$repo_root/.codex/no_leak_guard.sh" --config-only

hook_script="$repo_root/.codex/hooks/pre_tool_use_policy.py"
[[ -f "$hook_script" ]] || die 'private control-plane hook is missing'
for probe in \
  '{"hook_event_name":"PreToolUse","tool_name":"Read","tool_input":{"file_path":".codex/NO_LEAK_VAULT"}}' \
  '{"hook_event_name":"PreToolUse","tool_name":"Edit","tool_input":{"file_path":".claude/settings.json"}}'
do
  hook_probe="$(printf '%s\n' "$probe" | python3 "$hook_script")"
  python3 - "$hook_probe" <<'PY' || die 'private control-plane hook self-test failed'
import json
import sys

payload = json.loads(sys.argv[1])
result = payload.get("hookSpecificOutput", {})
if result.get("permissionDecision") != "deny":
    raise SystemExit(1)
PY
done
safe_probe="$(printf '%s\n' '{"hook_event_name":"PreToolUse","tool_name":"Bash","tool_input":{"command":"git status --short"}}' | python3 "$hook_script")"
[[ -z "$safe_probe" ]] || die 'private control-plane hook rejected a safe command'

[[ -z "$(git status --porcelain=v1 --untracked-files=all)" ]] || die 'working tree must be completely clean before a controlled run'
[[ "$(git branch --show-current)" == 'main' ]] || die 'start a controlled run from main'

git pull --ff-only origin main
[[ -z "$(git status --porcelain=v1 --untracked-files=all)" ]] || die 'working tree changed while synchronizing main'
base_commit="$(git rev-parse HEAD)"

task_input="$1"
task_path="$(realpath -- "$task_input")"
case "$task_path" in
  "$repo_root/control/tasks/"TASK-*.md) ;;
  *) die 'task must be a TASK-*.md file under control/tasks/' ;;
esac

task_id="$(basename -- "$task_path" .md)"
branch_slug="$(printf '%s' "$task_id" | tr '[:upper:]' '[:lower:]' | tr -c 'a-z0-9._-' '-')"
branch="claude/$branch_slug"
git show-ref --verify --quiet "refs/heads/$branch" && die 'the local task branch already exists'
git ls-remote --exit-code --heads origin "$branch" >/dev/null 2>&1 && die 'the remote task branch already exists'
git switch -c "$branch"

mkdir -p "$repo_root/.codex/local-runs"
raw_log="$repo_root/.codex/local-runs/claude-$task_id.final.txt"
receipt="$repo_root/control/receipts/$task_id.md"

prompt="Execute control/tasks/$task_id.md. Obey CLAUDE.md, AGENTS.md, and CANONICAL_WORKFLOW.md. The recorded base commit is $base_commit and the actor is Claude Code $claude_version on branch $branch. The host already validated the private vault. Never read, open, search, list, quote, print, or modify .codex, .claude, or local run logs. Do not inspect the outer dump unless the task explicitly requires bounded read-only inspection. Write only task-authorized paths inside this Git checkout. Do not commit, push, merge, use network tools, modify Git configuration, or print protected content. Create the task's sanitized receipt under control/receipts/."

set +e
claude -p \
  --permission-mode acceptEdits \
  --setting-sources project \
  --tools 'Bash,Edit,Read,Write,Glob,Grep' \
  --disallowed-tools WebFetch WebSearch Agent 'mcp__*' \
  --strict-mcp-config \
  --disable-slash-commands \
  --no-chrome \
  --no-session-persistence \
  --output-format text \
  "$prompt" > "$raw_log"
claude_status=$?
set -e
[[ $claude_status -eq 0 ]] || die "Claude Code exited with status $claude_status; raw local output remains under .codex/local-runs/"
[[ -f "$receipt" ]] || die 'Claude Code did not create the required sanitized receipt'

git add -A
"$repo_root/.codex/no_leak_guard.sh" --staged
git commit -m "Claude Code: $task_id"

if $push_branch; then
  git push -u origin "$branch"
  printf 'PC CLAUDE COMPLETE: pushed %s for independent review.\n' "$branch"
else
  printf 'PC CLAUDE COMPLETE: committed locally on %s. Review it, then run:\n' "$branch"
  printf '  git push -u origin %q\n' "$branch"
fi
