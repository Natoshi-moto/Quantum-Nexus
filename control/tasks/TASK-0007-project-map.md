# TASK-0007 — canonical project map and product definition

Status: `READY`

## Authority

The human repository owner explicitly authorized this task in ChatGPT Work on 2026-07-16.

## Recorded base

- canonical repository: `Natoshi-moto/Quantum-Nexus`
- canonical branch: `main`
- base commit before this task was opened: `0d415b1600cef4f5a33312e8d88be09f4471bb3d`
- actor branch class: `codex/`

## Objective

Create one plain-English, evidence-aware map of what Quantum Nexus is now, what the canonical repository actually contains, what remains relayed or unknown, how the existing components relate, which decisions remain open, and what single falsifiable build target should follow.

This is a synthesis task, not an import or implementation task.

## Writable paths

- `design/PROJECT_MAP.md`
- `control/receipts/TASK-0007-project-map.md`

## Required results

`design/PROJECT_MAP.md` must:

1. State a concise present-tense product definition without claiming that pending systems already exist.
2. Separate the operational governance/control plane from proposed product, research, archive, and external-project material.
3. Inventory every current canonical file or coherent file group and state what is present versus placeholder-only.
4. Use the repository evidence tiers: `T1_EXECUTED`, `T2_READ`, and `T3_CLAIM/T3_RELAYED`.
5. Identify `UNKNOWN` rather than reconstructing missing artifacts.
6. Describe the canonical task/branch/receipt/review/integration flow.
7. State the private outer-dump and host-only control-plane boundaries without exposing protected material.
8. Record stale or contradictory status documentation without silently repairing historical files.
9. List the human decisions still required for genesis publication, third-party material, Station Defense, Lab/nexus-kernel, and product scope.
10. Select one bounded, falsifiable next build target and define its pass/fail condition.
11. Distinguish current source-backed facts from recommendations.

## Required verification

1. Read current `AGENTS.md`, `CANONICAL_WORKFLOW.md`, `CLAUDE.md`, `README.md`, `SYNC_LEDGER.md`, current handoffs, control-plane designs, task envelopes, receipts, folder READMEs, and checked-in launcher/guard sources.
2. Confirm the task branch starts at this task-opening commit.
3. Compare the complete task branch against both its recorded base and current `main`.
4. Confirm the branch changes only the two authorized paths.
5. Read both new files back from GitHub after committing them.
6. Check Markdown structure, repository-relative references, evidence labels, and obvious credential/private-key patterns.
7. Create the required sanitized receipt.

## Forbidden

- Do not inspect, summarize, quote, or export the private outer dump.
- Do not inspect host-only vault or local-run paths.
- Do not import genesis captures, archives, external projects, transcripts, or private material.
- Do not claim that relayed tests were executed by this actor.
- Do not edit historical tasks, receipts, handoffs, incidents, or ledger entries.
- Do not change governance, launcher, guard, configuration, or product code.
- Do not merge or promote the implementation without independent review.
- Do not rewrite history or force-update any branch.

## Receipt

Create `control/receipts/TASK-0007-project-map.md` containing:

- task ID;
- actor and branch;
- base and task-opening commits;
- changed paths;
- source files read;
- verification results with evidence tiers;
- limitations and blockers;
- readiness for independent review.
