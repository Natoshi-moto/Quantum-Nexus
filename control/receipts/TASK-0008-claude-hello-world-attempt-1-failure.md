# TASK-0008 attempt 1 — controller failure record

task ID: `TASK-0008-claude-hello-world`

verdict: `FAIL — REQUIRED RECEIPT ABSENT`

recording actor: ChatGPT Work integration/controller session

## Directly verified GitHub evidence

- canonical `main` remained `f692ed19e307ec06252680be8fd9959007ff9948` — `T1_EXECUTED`;
- preserved failed branch: `claude/task-0008-claude-hello-world-failed-attempt-1` — `T1_EXECUTED`;
- preserved commit: `244a30a6f4f82084514d61614fe326ab9d15213f` — `T1_EXECUTED`;
- the failed branch is one commit ahead and zero behind its recorded base — `T1_EXECUTED`;
- its diff adds exactly:
  - `experiments/provider_handshake/claude_hello.py` — 37 lines;
  - `tests/test_claude_hello.py` — 146 lines;
- `control/receipts/TASK-0008-claude-hello-world.md` is absent from the preserved commit — `T1_EXECUTED`;
- no TASK-0008 implementation was integrated into `main`.

## Human-relayed local execution evidence

The human operator relayed the fail-closed launcher result:

- Claude Code exited without creating the required sanitized receipt;
- the host launcher stopped before staging, committing, or pushing;
- the human subsequently preserved only the two authorized Python source paths after the no-leak staged guard passed.

The human also relayed:

- Python compilation completed without reported error;
- `python3 -m unittest -v tests/test_claude_hello.py` ran 8 tests and reported `OK`;
- direct CLI output was `Hello from Claude Code`;
- relayed SHA-256:
  - implementation: `959a780b435239331b7f4d994919506a16f5ff977de6f1c95c738fe401c3316e`;
  - tests: `3d37af11c1613027baaa0f2402e243ee7567e2fa32b48c840b6153cde00b6124`.

Those local command results and SHA-256 values are `T3_RELAYED` to this recording session until independently recomputed from the preserved GitHub bytes.

## Interpretation

The implementation may be technically correct, but TASK-0008 failed its workflow contract because the required actor receipt was absent. The host stopping before automatic commit/push is positive fail-closed control evidence; it does not convert the overall task into a pass.

The preserved branch is failure evidence only. It must not be merged as TASK-0008 completion.
