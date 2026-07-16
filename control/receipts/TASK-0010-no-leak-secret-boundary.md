# TASK-0010 no-leak secret-boundary receipt

task ID: `TASK-0010-no-leak-secret-boundary`

verdict: `PASS FOR INDEPENDENT REVIEW`

actor: Codex in ChatGPT Work — `T1_EXECUTED`

branch: `codex/task-0010-no-leak-secret-boundary` — `T1_EXECUTED`

base before task opening: `7a815bf194ccf1d23a2116526e633d9d2262cf8a` — `T1_EXECUTED`

task-opening commit: `1e6fe94a786e4bd6856e09ca203ea2a46caa1ad5` — `T1_EXECUTED`

## Triggering finding

The stopped TASK-0009 receipt accurately contained the branch `pc/task-0009-codex-cross-provider-review-and-implementation`. The canonical scanner's unbounded OpenAI-style alternative matched the word-internal substring beginning at the final two letters of `task-` and produced an obvious-credential false positive — `T1_EXECUTED` against the supplied public task output and `T2_READ` against the canonical guard source.

No credential was inferred from the blocked message. The raw host log, vault, outer dump, and private material were not inspected.

## Changed paths

- `.codex/no_leak_guard.sh`
- `tests/test_no_leak_secret_pattern.sh`
- `control/receipts/TASK-0010-no-leak-secret-boundary.md`

No other path is authorized.

## Exact change

Old alternative:

`sk-[A-Za-z0-9_-]{20,}`

New alternative:

`(^|[^A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}`

All other alternatives in `secret_pattern` were preserved byte-for-byte — `T1_EXECUTED` by applying one exact single-occurrence replacement and `T2_READ` from the resulting source.

The boundary continues to match a standalone token shape and shapes following a space, quote, equals sign, slash, or underscore. It rejects word-internal appearances in `task-` and `risk-`.

## Verification

Initial scratch execution of the regression test exited 2 because the first scratch copies were placed flat while the test correctly resolves repository layout from `tests/` to `.codex/`. This harness setup error occurred before pattern evaluation and is retained as `T1_EXECUTED`.

After arranging the exact candidate bytes in repository-shaped scratch paths:

- `bash -n .codex/no_leak_guard.sh` — exit 0, no output — `T1_EXECUTED`;
- `bash -n tests/test_no_leak_secret_pattern.sh` — exit 0, no output — `T1_EXECUTED`;
- `bash tests/test_no_leak_secret_pattern.sh` — exit 0, output `PASS: secret-pattern boundary regression` — `T1_EXECUTED`.

The regression constructs synthetic credential shapes at runtime so its source does not contain standalone credential-shaped literals. It covers the OpenAI-style boundary and all pre-existing AWS, PEM, GitHub, fine-grained GitHub, and Slack alternatives — `T2_READ`.

## Limitations

- This actor did not access or execute against the host-only vault.
- The full staged-content guard was not run in this scratch environment because its trusted host configuration is intentionally unavailable.
- Passing the lexical regression does not prove general secret detection or eliminate false negatives.
- The stopped TASK-0009 work remains unintegrated and must be rechecked with the reviewed guard bytes; this task does not authorize bypassing the guard.

readiness: `READY FOR INDEPENDENT REVIEW`
