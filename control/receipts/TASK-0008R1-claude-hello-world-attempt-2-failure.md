# TASK-0008R1 attempt 2 — controller failure record

task ID: `TASK-0008R1-claude-hello-world-retry`

verdict: `FAIL — REQUIRED RECEIPT ABSENT`

recording actor: ChatGPT Work integration/controller session

## Directly verified GitHub evidence

- canonical `main` remained `3ea7c4a6611a0c6b605da0cc7c51dc85a45c2a10` — `T1_EXECUTED`;
- preserved failed branch: `claude/task-0008r1-claude-hello-world-retry-failed-attempt-2` — `T1_EXECUTED`;
- preserved commit: `e46aac801df78cf2e59d72332478625694e7fc53` — `T1_EXECUTED`;
- the branch is one commit ahead and zero behind its recorded base — `T1_EXECUTED`;
- its diff adds exactly:
  - `experiments/provider_handshake/claude_hello.py` — 19 lines;
  - `tests/test_claude_hello.py` — 129 lines;
- `control/receipts/TASK-0008R1-claude-hello-world-retry.md` is absent — `T1_EXECUTED`;
- no TASK-0008R1 implementation was integrated into `main`.

## Human-relayed local execution evidence

The human operator relayed that:

- the Claude launcher again stopped because the mandatory receipt was absent;
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v tests/test_claude_hello.py` ran 8 tests and reported `OK`;
- direct CLI output was `Hello from Claude Code`;
- relayed SHA-256:
  - implementation: `298dddfc01f0a3716de00e671890beade31aba2e44408b1fe84b7d33e9f57290`;
  - tests: `b012b1dece884a6748f932cdfd74069f1d41d8103cd1466910ff1e8300cfe00c`;
- the staged no-leak guard passed before the human preserved the two source files on the explicitly failed branch.

Those local results and SHA-256 values are `T3_RELAYED` to this recording session until a separate actor recomputes them from the GitHub commit.

## Reproducible control-plane finding

Two fresh Claude Code runs produced different Python source/test bytes that reportedly passed the same eight behavioral gates, yet both omitted their exact mandatory receipt. Canonical `.claude/settings.json` and the pre-tool hook do not deny `control/receipts/`; therefore a receipt-path permission block is not supported by the inspected source.

The raw host-only logs were not inspected. The exact internal reason for omission remains `UNKNOWN`.

Attempt 2 is preserved as failure evidence only and must not be merged as successful completion.
