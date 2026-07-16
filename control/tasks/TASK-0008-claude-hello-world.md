# TASK-0008 — Claude Code deterministic Python hello-world handshake

Status: `READY`

## Authority

The human repository owner explicitly authorized this bounded cross-provider workflow proof in ChatGPT Work on 2026-07-16.

## Recorded base

- canonical repository: `Natoshi-moto/Quantum-Nexus`
- canonical branch: `main`
- base commit before this task was opened: `bb077c2d4ec0ef5e2679f98d60fd9a391bb20138`
- declared actor: fresh ephemeral Claude Code session launched by `.claude/run_task.sh`
- actor branch class: `claude/`

## Objective

Create the smallest deterministic Python artifact that proves a fresh Claude Code worker can receive a canonical task, work only on an isolated actor branch, execute named checks, produce a sanitized receipt, and return reviewable bytes.

This task proves only the bounded workflow. It does not prove autonomous orchestration, general correctness, non-leakage, or readiness for high-risk work.

## Writable paths

- `experiments/provider_handshake/claude_hello.py`
- `tests/test_claude_hello.py`
- `control/receipts/TASK-0008-claude-hello-world.md`

No other path is authorized.

## Required behavior

1. `claude_hello.py` must use only the Python standard library.
2. Importing the module must have no side effects.
3. It must expose a callable that deterministically returns exactly `Hello from Claude Code`.
4. Executing the file with Python must write exactly `Hello from Claude Code\n` to standard output, write nothing to standard error, and exit zero.
5. The implementation must not read environment variables, local files, command-line input, network state, clocks, randomness, user identity, or protected project paths.
6. The test file must verify both the imported callable and the subprocess contract, including exact stdout, empty stderr, and zero exit status.
7. Tests must not require third-party packages or network access.

## Required verification

The Claude Code actor must execute and record the observed results of:

1. `python3 -m py_compile experiments/provider_handshake/claude_hello.py tests/test_claude_hello.py`
2. `python3 -m unittest -v tests/test_claude_hello.py`
3. `python3 experiments/provider_handshake/claude_hello.py`
4. a changed-path check showing only the three authorized paths changed;
5. an inspection confirming there are no credential-like strings, external dependencies, network calls, environment reads, nondeterministic inputs, or protected-path references in the authored files.

The host launcher and staged-content guard remain responsible for branch creation, protected-control-plane preflight, staging, guard execution, commit, and optional push. The task actor must not claim those host actions as its own `T1_EXECUTED` evidence unless it directly observes their output.

## Evidence rules

- Use `T1_EXECUTED` only for commands this fresh Claude Code session actually ran and observed.
- Use `T2_READ` for source bytes it directly inspected.
- Use `T3_CLAIM/T3_RELAYED` for launcher, host, prior-session, or external statements it did not independently reproduce.
- Say `UNKNOWN` rather than reconstructing missing evidence.

## Required receipt

Create `control/receipts/TASK-0008-claude-hello-world.md` containing:

- task ID and verdict: `PASS FOR INDEPENDENT REVIEW`, `FAIL`, or `BLOCKED`;
- actor, Claude Code version if directly observed, branch, and recorded base;
- exact changed paths;
- exact commands executed and their observed exit results;
- exact expected and observed CLI output represented safely;
- evidence tier for every material claim;
- limitations, discrepancies, and blockers;
- final readiness for independent review.

## Forbidden

- Do not modify governance, launchers, hooks, configuration, historical tasks, historical receipts, handoffs, ledger entries, or Git metadata.
- Do not read, list, search, quote, or modify the host-only vault, local-run logs, outer dump, or private material.
- Do not use network tools or external dependencies.
- Do not commit, push, merge, or update `main`; the host launcher owns branch commit/push mechanics.
- Do not create TASK-0009 or claim that Codex reviewed this work.
- Do not broaden this task into `NEXUS-CAPSULE-0001` or any product implementation.
