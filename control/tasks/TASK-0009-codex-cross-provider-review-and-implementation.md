# TASK-0009 — Codex cross-provider review and independent hello implementation

Status: `READY`

## Authority

The human repository owner authorized Codex to review both preserved Claude Code attempts, independently re-execute their public tests, author a separate deterministic Python implementation, and produce cross-provider differential evidence.

## Recorded base and actor exception

- canonical repository: `Natoshi-moto/Quantum-Nexus`
- canonical branch: `main`
- base before this task was opened: `2fed51e359f37bafe7dfb82739724bab42e691ed`
- declared actor: a fresh ephemeral Codex CLI session launched by `.codex/run_task.sh`
- expected branch from the currently canonical launcher: `pc/task-0009-codex-cross-provider-review-and-implementation`

`CANONICAL_WORKFLOW.md` specifies `codex/`, while the current launcher still creates `pc/`. The human authorizes the expected `pc/` branch for this task as a one-time, explicitly recorded legacy exception. This does not resolve the discrepancy or authorize future silent equivalence.

## Fixed Claude evidence

Attempt 1:

- branch: `claude/task-0008-claude-hello-world-failed-attempt-1`
- commit: `244a30a6f4f82084514d61614fe326ab9d15213f`
- recorded base: `f692ed19e307ec06252680be8fd9959007ff9948`
- paths: `experiments/provider_handshake/claude_hello.py`, `tests/test_claude_hello.py`
- actor receipt: absent

Attempt 2:

- branch: `claude/task-0008r1-claude-hello-world-retry-failed-attempt-2`
- commit: `e46aac801df78cf2e59d72332478625694e7fc53`
- recorded base: `3ea7c4a6611a0c6b605da0cc7c51dc85a45c2a10`
- paths: `experiments/provider_handshake/claude_hello.py`, `tests/test_claude_hello.py`
- actor receipt: absent

The commits are failure evidence, not implementation authority.

## Objectives

1. Inspect both fixed Claude commits using local, read-only Git operations.
2. Recompute their source/test SHA-256 values from Git bytes.
3. Extract each implementation and test pair into separate temporary directories and independently run their test suites offline.
4. Review scope, determinism, exact I/O contracts, import behavior, argument rejection, negative controls, privacy boundaries, and receipt absence.
5. State only source-supported conclusions. The raw host logs are forbidden and the internal cause of either omission remains `UNKNOWN` unless the public bytes prove it.
6. Author a separate Codex implementation after review, clearly disclosing that it is not blind.
7. Add a differential test that executes both fixed Claude implementations and the Codex implementation and compares their normalized observable contracts.
8. Produce the exact mandatory sanitized receipt.

## Writable paths

- `experiments/provider_handshake/codex_hello.py`
- `tests/test_codex_hello.py`
- `tests/test_provider_handshake_differential.py`
- `control/receipts/TASK-0009-codex-cross-provider-review-and-implementation.md`

No other path is authorized.

## Codex implementation contract

1. Use only the Python standard library.
2. Import with no stdout, stderr, or other side effect.
3. Expose a no-required-argument callable returning exactly `Hello from Codex`.
4. With no arguments, the CLI emits exactly `Hello from Codex\n`, empty stderr, and exit zero.
5. Unexpected positional arguments are rejected with a deterministic, tested non-zero exit and stable stderr.
6. Do not consume environment values, files, network state, clocks, randomness, identity, or protected paths to produce the greeting.
7. Include ordinary, isolated-environment, repeatability, import-side-effect, unexpected-argument, and temporary-tamper negative-control tests.

## Differential requirements

The differential test must use the fixed commit IDs, not mutable branch names. It must:

- obtain each Claude source/test pair with read-only `git show`;
- place each pair in its own temporary directory without modifying the checkout;
- verify the relayed SHA-256 values or report exact discrepancies;
- run both Claude suites and require success;
- run each implementation twice;
- normalize provider-specific greeting text while preserving provider identity;
- compare success exit, one-line stdout, empty stderr, import silence, repeatability, and deterministic rejection of unexpected input;
- include the Codex implementation under the same normalized contract;
- fail non-zero on any divergence not explicitly permitted by the provider label.

This is an independently authored-after-review implementation, not a blind independent implementation. The receipt must say so.

## Required verification

Execute and record:

1. read-only comparisons of each Claude commit with its recorded base;
2. exact changed-path checks for both Claude commits;
3. SHA-256 recomputation for all four Claude files;
4. independent execution of both extracted Claude suites;
5. `python3 -m py_compile experiments/provider_handshake/codex_hello.py tests/test_codex_hello.py tests/test_provider_handshake_differential.py`;
6. `python3 -m unittest -v tests/test_codex_hello.py tests/test_provider_handshake_differential.py`, twice as separate commands;
7. `python3 experiments/provider_handshake/codex_hello.py`;
8. SHA-256 for all three authored Python files;
9. changed-path confirmation showing exactly the four authorized paths;
10. an obvious credential, external-dependency, network-call, environment-read, nondeterminism, and protected-path reference inspection.

## Required receipt

Create exactly:

`control/receipts/TASK-0009-codex-cross-provider-review-and-implementation.md`

It must include:

- task ID and `PASS FOR INDEPENDENT REVIEW`, `FAIL`, or `BLOCKED`;
- actor/version, base, branch, and the explicit legacy `pc/` exception;
- both Claude commits, comparisons, changed paths, recomputed hashes, and rerun results;
- separate SOURCE findings and CLAIM/UNKNOWN limitations;
- Codex changed paths, commands, outputs, hashes, and test results;
- differential results and any disagreements;
- explicit non-blind limitation;
- receipt-omission finding without raw-log speculation;
- final blockers and readiness.

Before returning, read the exact receipt back and confirm it is non-empty and contains literal markers `TASK-0009`, a verdict, `T1_EXECUTED`, `T2_READ`, `UNKNOWN`, `changed paths`, `limitations`, and `non-blind`.

## Forbidden

- Do not inspect `.codex/NO_LEAK_VAULT`, `.codex/local-runs`, `.claude/`, raw logs, outer dump, or private material.
- Do not modify either Claude branch or its commits.
- Do not edit governance, launchers, hooks, configuration, historical tasks, failure records, handoffs, or ledger.
- Do not use network tools or external packages.
- Do not commit, push, merge, or update `main`; the host launcher owns branch mechanics.
- Do not claim either Claude attempt passed its overall task merely because its Python tests pass.
- Do not claim the internal cause of receipt omission is known.
- Do not broaden this task into NEXUS-CAPSULE-0001 or product implementation.
