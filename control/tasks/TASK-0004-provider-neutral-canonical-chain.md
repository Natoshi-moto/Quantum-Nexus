# TASK-0004 — provider-neutral canonical change chain

Status: `READY`

## Objective

Replace the temporary ChatGPT-exclusive integration wording with a human-owned, provider-neutral workflow for Claude Code, Codex, chat-connected agents, and manual human work. Define the canonical and auditable lifecycle for every accepted repository change.

## Authority

The human repository owner is the final authority. No AI provider owns the project.

## Writable paths

- `AGENTS.md`
- `CLAUDE.md`
- `CANONICAL_WORKFLOW.md`
- `SYNC_LEDGER.md`
- `control/receipts/TASK-0004-provider-neutral-canonical-chain.md`

## Required results

1. Define GitHub `main` as the canonical approved project state.
2. Define the outer dump as private, read-only source material rather than canonical code.
3. Give Claude Code, Codex, chat-connected agents, and the human equal access to the same task/branch/receipt/review protocol.
4. Require a task ID, recorded base commit, actor branch, bounded changes, tests, receipt, independent review, integration record, and fast-forward local synchronization.
5. Define how unmanaged or emergency changes are adopted without falsifying history.
6. Add a concise Claude Code entrypoint that points to the shared provider-neutral rules.
7. Preserve the no-leak, append-only, evidence-tier, and non-execution firewalls.

## Forbidden

- Do not weaken the private dump boundary.
- Do not give any AI provider permanent ownership of `main`.
- Do not rewrite or delete historical records.
- Do not claim that a local Claude Code launcher is complete before its installed version and controls are verified.
- Do not include private dump content, credentials, or local-only paths.

## Verification

Read every changed file back from GitHub `main` and record the resulting commit IDs in the sync ledger.
