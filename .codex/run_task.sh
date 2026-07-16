#!/usr/bin/env bash
set -euo pipefail

die() {
  printf 'PC CODEX STOPPED: %s\n' "$1" >&2
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

command -v codex >/dev/null || die 'Codex CLI is not installed or not on PATH'
command -v git >/dev/null || die 'Git is not installed or not on PATH'

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(git -C "$script_dir/.." rev-parse --show-toplevel 2>/dev/null)" || die 'launcher is not inside a Git checkout'
repo_root="$(realpath -- "$repo_root")"
cd "$repo_root"

"$repo_root/.codex/no_leak_guard.sh" --config-only

[[ -z "$(git status --porcelain=v1 --untracked-files=all)" ]] || die 'working tree must be completely clean before a controlled run'
[[ "$(git branch --show-current)" == 'main' ]] || die 'start a controlled run from main'

git pull --ff-only origin main
task_input="$1"
task_path="$(realpath -- "$task_input")"
case "$task_path" in
  "$repo_root/control/tasks/"TASK-*.md) ;;
  *) die 'task must be a TASK-*.md file under control/tasks/' ;;
esac

task_id="$(basename -- "$task_path" .md)"
branch_slug="$(printf '%s' "$task_id" | tr '[:upper:]' '[:lower:]' | tr -c 'a-z0-9._-' '-')"
branch="pc/$branch_slug"
git show-ref --verify --quiet "refs/heads/$branch" && die 'the local task branch already exists'
git ls-remote --exit-code --heads origin "$branch" >/dev/null 2>&1 && die 'the remote task branch already exists'
git switch -c "$branch"

mkdir -p "$repo_root/.codex/local-runs"
raw_log="$repo_root/.codex/local-runs/$task_id.final.txt"
receipt="$repo_root/control/receipts/$task_id.md"

prompt="Execute the task in control/tasks/$task_id.md. Obey AGENTS.md and .codex/NO_LEAK_VAULT. The outer dump is readable context but is not writable and is not export-authorized. Write only inside this Git checkout. Do not commit, push, use network tools, modify .git or .codex, or print protected content. Create a sanitized receipt at control/receipts/$task_id.md."

set +e
codex \
  --strict-config \
  --sandbox workspace-write \
  --ask-for-approval never \
  --cd "$repo_root" \
  exec \
  --ephemeral \
  "$prompt" > "$raw_log"
codex_status=$?
set -e
[[ $codex_status -eq 0 ]] || die "Codex exited with status $codex_status; raw local output remains under .codex/local-runs/"
[[ -f "$receipt" ]] || die 'Codex did not create the required sanitized receipt'

git add -A
"$repo_root/.codex/no_leak_guard.sh" --staged
git commit -m "PC Codex: $task_id"

if $push_branch; then
  git push -u origin "$branch"
  printf 'PC CODEX COMPLETE: pushed %s for ChatGPT review.\n' "$branch"
else
  printf 'PC CODEX COMPLETE: committed locally on %s. Review it, then run:\n' "$branch"
  printf '  git push -u origin %q\n' "$branch"
fi
