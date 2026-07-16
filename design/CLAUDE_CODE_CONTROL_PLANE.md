# Claude Code control plane

Status: static implementation complete; on-PC execution pending.

## Purpose

Claude Code is a peer task worker under the same human-owned canonical workflow as Codex. It does not own `main`, write to the outer dump, or treat readable material as export-authorized.

## Controlled command

```bash
bash .claude/run_task.sh --push control/tasks/TASK-*.md
```

The trusted host launcher validates the local vault and checkout, requires clean synchronized `main`, records the base commit, creates a `claude/<task-slug>` branch, invokes Claude non-interactively, requires a sanitized receipt, runs the staged no-leak guard, commits, and optionally pushes only the task branch.

The Claude session does not receive commit, push, merge, remote-control, browser, network, or MCP authority. The launcher does not use `--dangerously-skip-permissions` or `bypassPermissions`.

## Defense in depth

1. `CLAUDE.md`, `AGENTS.md`, and `CANONICAL_WORKFLOW.md` define the shared contract.
2. `.claude/settings.json` denies private control-plane paths and dangerous/network tools.
3. A shared `PreToolUse` hook blocks tool inputs naming `.codex`, `.claude`, the vault, or local run logs.
4. The launcher performs hook self-tests before branching.
5. Claude Code's task session writes only inside the nested checkout.
6. The host stages output and runs the existing no-leak guard before committing.
7. GitHub review and ledger integration are still required before the work becomes canonical.

## Version basis

The target PC reported Claude Code `2.1.211`. The launcher requires `2.1.208` or newer because current path-deny behavior is part of the safety model.

Design sources read on 2026-07-16:

- <https://code.claude.com/docs/en/cli-reference>
- <https://code.claude.com/docs/en/hooks>
- <https://code.claude.com/docs/en/permissions>
- <https://code.claude.com/docs/en/security>

## Remaining proof

Static tests cannot prove the target PC's effective Claude configuration. A separate smoke task must run through the launcher, show the hook lifecycle, change only its receipt, push a `claude/` branch, and pass independent GitHub comparison before this control plane is marked operational.
