# TASK-0008R1 — fresh Claude Code hello-world retry

Status: `READY`

## Authority

The human repository owner authorized a fresh retry after TASK-0008 attempt 1 failed closed because Claude Code omitted the mandatory receipt.

## Recorded base and prior evidence

- canonical repository: `Natoshi-moto/Quantum-Nexus`
- canonical branch: `main`
- base before this retry task was opened: `3cb03ec14ce26b5ecdacf74b532fc48aed184964`
- failed attempt branch: `claude/task-0008-claude-hello-world-failed-attempt-1`
- failed attempt commit: `244a30a6f4f82084514d61614fe326ab9d15213f`
- failure record: `control/receipts/TASK-0008-claude-hello-world-attempt-1-failure.md`
- declared actor: a new ephemeral Claude Code session launched by `.claude/run_task.sh`
- actor branch class: `claude/`

The prior branch is evidence only. Do not copy, amend, merge, or continue its working session. Reimplement from the canonical task requirements in this fresh run.

## Governing requirements

Read and satisfy:

1. `control/tasks/TASK-0008-claude-hello-world.md`;
2. `control/tasks/TASK-0008-claude-hello-world-assurance-addendum.md`;
3. this retry envelope.

This retry changes the receipt path and provenance only. All original behavioral, negative-control, determinism, privacy, and evidence requirements remain binding.

## Writable paths

- `experiments/provider_handshake/claude_hello.py`
- `tests/test_claude_hello.py`
- `control/receipts/TASK-0008R1-claude-hello-world-retry.md`

No other path is authorized.

## Mandatory completion order

1. Read all three governing task files.
2. Implement the two Python files from the requirements.
3. Execute every original and assurance-addendum verification, including two complete unit-test runs and the temporary mutation negative control.
4. Compute final SHA-256 values.
5. Create the sanitized receipt at exactly:
   `control/receipts/TASK-0008R1-claude-hello-world-retry.md`
6. As the final verification operation before returning, read that exact receipt back and confirm it is non-empty and contains all of these literal markers:
   - `TASK-0008R1`
   - one of `PASS FOR INDEPENDENT REVIEW`, `FAIL`, or `BLOCKED`
   - `T1_EXECUTED`
   - `T2_READ`
   - `changed paths`
   - `limitations`
7. If the receipt is absent or incomplete, do not report success. Create or correct it within the authorized path, read it back again, and return only after the markers are present.

## Receipt requirements

The receipt must include:

- retry task ID and honest verdict;
- fresh actor and directly observed Claude Code version;
- branch and launcher-supplied base;
- prior attempt identified only as preserved failure evidence;
- exact changed paths;
- exact commands and observed exit results;
- ordinary-suite and expected negative-control results separately;
- expected and observed stdout, stderr, and exit behavior;
- two test-run results;
- full SHA-256 values;
- evidence tiers for every material claim;
- discrepancies, limitations, blockers, and readiness.

## Forbidden

All original TASK-0008 forbidden actions remain binding. Additionally:

- do not inspect the host-only raw log from attempt 1;
- do not claim continuation of the prior Claude session;
- do not copy the preserved failed implementation;
- do not edit or delete the prior task, addendum, or failure record;
- do not open TASK-0009;
- do not commit, push, merge, or update `main`; the launcher owns host-side branch mechanics.
