# Incident — local vault displayed in TASK-0002 terminal trace

Date: 2026-07-16  
Status: contained and remediated

## What happened

The TASK-0002 PC Codex run opened and displayed the local `.codex/NO_LEAK_VAULT` while reading its instructions. The output remained in the user's terminal and the ignored local run log. This violated the control-plane rule even though the task receipt itself stayed sanitized.

## Evidence

- `T2_READ`: the supplied TASK-0002 terminal trace shows the vault read and local display.
- `T1_EXECUTED`: GitHub comparison and direct file reads showed the task branch changed only the bounded receipt.
- `T1_EXECUTED`: the sanitized receipt was promoted to `main`; the vault and raw run log were not committed.

No credentials or authentication tokens were present in the displayed policy registry. No evidence shows the vault or raw log entered GitHub. The incident is still recorded because protected path and policy data must not be printed.

## Root cause

The launcher prompt told the task agent to obey the vault, which encouraged it to open the file. The prior guard checked staged output but did not stop a read before execution.

## Remediation

- The task prompt now says the host has already validated the vault and forbids task-agent access to `.codex` and local run logs.
- A `PreToolUse` hook denies Bash or patch operations that name the private control-plane paths.
- The launcher runs a fail-closed hook self-test before creating a task branch.
- The launcher enables the reviewed hook for non-interactive automation with Codex's hook-trust override.
- `AGENTS.md` now defines the vault and local logs as host-only.

The staged-content guard remains the final export check. This incident does not broaden dump read or write authority.
