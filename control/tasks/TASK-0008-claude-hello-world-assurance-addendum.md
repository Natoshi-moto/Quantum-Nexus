# TASK-0008 assurance addendum — deterministic and audit-negative controls

Status: `READY`

This additive amendment was authorized by the human repository owner before the first TASK-0008 actor run. It tightens the original task without replacing or concealing the earlier task bytes. If there is any ambiguity, this addendum adds assurance requirements but does not broaden writable paths or implementation authority.

## Additional implementation contract

1. The public callable must accept no required arguments and return a Python `str` with exactly 22 Unicode code points: `Hello from Claude Code`.
2. The CLI accepts no positional arguments. An unexpected argument must produce a deterministic non-zero result; the implementation and tests must define and verify the exact exit code and stderr contract.
3. Importing the module in a fresh Python subprocess must produce empty stdout, empty stderr, and exit zero.
4. Two independent CLI subprocess executions must produce byte-identical stdout, stderr, and exit status.
5. At least one CLI execution must use:
   - the absolute Python interpreter path;
   - the absolute script path;
   - an unrelated temporary working directory;
   - `PYTHONNOUSERSITE=1`;
   - no repository path added through `PYTHONPATH`.
6. The implementation remains deterministic and offline. The test harness may use temporary directories and subprocess environment controls from the Python standard library.

## Required negative control

The test suite must create a temporary, non-repository copy of the implementation, alter the greeting in that copy, and execute the exact-output contract test against the altered copy. The negative control passes only if the altered copy is rejected.

The temporary mutation must never touch the Git checkout, staged content, task branch source, or historical records. The receipt must distinguish:

- the ordinary suite passing against authentic task bytes; and
- the deliberately altered temporary copy being rejected.

A negative-control rejection is expected evidence, not a task failure.

## Additional verification and provenance

The fresh Claude Code actor must:

1. record `python3 --version` as `T1_EXECUTED`;
2. compute SHA-256 for the implementation and test file after final edits and record both full digests as `T1_EXECUTED`;
3. run the full test suite twice in separate commands and record both observed results;
4. confirm the receipt itself contains no raw local log, protected path contents, username, home-directory path, secret, token, or unnecessary host identifier;
5. state that hashes identify inspected bytes but do not by themselves prove correctness, authorship, or non-leakage.

The later independent reviewer must recompute these hashes from the pushed GitHub branch rather than trusting the receipt.

## Cross-provider follow-on constraints

TASK-0009 must not be opened until TASK-0008 has a fixed reviewed commit and the exact canonical base is known.

The later Codex actor must:

- directly inspect the canonical Claude implementation and tests;
- rerun their checks;
- record review findings with evidence tiers;
- author a separate implementation in separately authorized paths;
- add a provider-neutral differential test that executes both implementations and compares normalized observable behavior;
- disclose that its implementation is independently authored after seeing Claude's work and is therefore not a blind independent implementation;
- preserve any disagreement rather than silently normalizing it away.

## Final dual-audit protocol

After both provider artifacts are integrated, two fresh read-only audit sessions receive the same:

- repository URL;
- task IDs;
- recorded bases;
- branch heads;
- integration commits;
- final `main`;
- required test commands;
- mutation challenge.

One ChatGPT auditor and one Claude auditor must each return `APPROVE`, `REQUEST CHANGES`, or `BLOCKED` with exact evidence. Neither auditor should be shown the other auditor's verdict before submitting its first verdict. Agreement is evidence of convergence, not proof; disagreement is retained and reconciled additively.

No audit session may modify code, task records, receipts, branches, PRs, or `main`. A separate integration/acceptance session records the outcome only after both reports exist.

## Clarifications and follow-on gate

For avoidance of doubt, the original prohibition on reading command-line input means that user-supplied values must not influence or be incorporated into the greeting. Inspecting whether unexpected arguments are present solely to reject them deterministically is required and permitted.

A source-backed namespace discrepancy exists before the Codex follow-on: `CANONICAL_WORKFLOW.md` names `codex/<task-slug>` as the Codex actor branch class, while the current `.codex/run_task.sh` creates `pc/<task-slug>`. This does not block TASK-0008's Claude branch. It is a hard precondition for TASK-0009: before Codex performs writable work, a separate human-authorized task must either reconcile the launcher with the canonical `codex/` namespace or record an explicit reviewed exception. The dual auditors must check this point rather than treating the two names as interchangeable.
