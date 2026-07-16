# TASK-0005 — Claude Code controlled-run bootstrap

Status: `READY`

## Objective

Add a fail-closed Claude Code 2.1.211 control plane that follows the same human-owned canonical workflow and private dump boundary as Codex.

## Recorded target

- target platform: Fedora
- observed Claude Code version: 2.1.211 — `T1_EXECUTED` by the human and relayed to the integration agent
- minimum supported launcher version: 2.1.208

## Writable paths

- `.claude/settings.json`
- `.claude/run_task.sh`
- `.codex/hooks/pre_tool_use_policy.py`
- `.gitignore`
- `design/CLAUDE_CODE_CONTROL_PLANE.md`
- `SYNC_LEDGER.md`
- `control/receipts/TASK-0005-claude-code-control-bootstrap.md`

## Required results

1. Claude Code reads the shared `CLAUDE.md`, `AGENTS.md`, and canonical workflow.
2. Project settings deny built-in reads/edits of private control-plane paths and deny network/MCP tools for controlled tasks.
3. A `PreToolUse` hook blocks Bash, file, search, and patch tools that name private control-plane paths.
4. The launcher verifies the vault/checkout/origin, requires clean synchronized `main`, creates a `claude/<task-slug>` branch, runs Claude non-interactively without permission bypass, requires a sanitized receipt, runs the staged no-leak guard, commits, and optionally pushes only the task branch.
5. Raw Claude output remains ignored and local-only.
6. Static syntax, JSON, hook-denial, and safe-command tests pass before publication.
7. On-PC Claude execution remains unclaimed until a separate smoke task passes.

## Forbidden

- Do not use `--dangerously-skip-permissions` or `bypassPermissions`.
- Do not grant Claude write access outside the nested Git checkout.
- Do not grant network, browser, MCP, remote-control, commit, push, merge, or Git-configuration authority to the Claude task session.
- Do not expose the real vault or local logs.
- Do not edit historical task or receipt records.

## Verification

Perform local static tests, read back every changed file from GitHub `main`, and queue a separate bounded Claude smoke task.
