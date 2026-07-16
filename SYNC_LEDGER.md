# Sync Ledger

Running record of every zip snapshot handed to a chat-based agent, matched against the repo's state at that time. This is how drift between the PC folder, the zip, and GitHub gets caught instead of silently accumulating.

## Log

| Round | Zip received | Repo HEAD before | Repo HEAD after | Status |
|---|---|---|---|---|
| 1 | `Quantum_Nexus_v0_0_0.zip` (2026-07-16) | `bb937dee` (LICENSE only) | `e20b4b1af7e7669a2b80388cc20603f908d18b55` | Scaffold landed with the exact supplied commit message. A write test succeeded at `caf04e2db661e1a36705600ac54a0983b3d3426c`, then `.write-test` was removed in the scaffold commit. Fresh GitHub reads matched all 11 supplied files byte-for-byte. Project content **not yet imported** — see open questions below. |

## Verified supplement received in ChatGPT session 3

- Uploaded wrapper: `Quantum Nexus v0.0.0(1).zip`, SHA-256 `2f0098484f60482be45ba3b86b2723bcac2953a91f3f1e46107175df2577811f`.
- Inner genesis ZIP and complete Git bundle were both present once; the earlier triple-duplicate and self-nesting observations do not describe this supplement.
- Bundle: SHA-256 Git object format, complete one-commit history, `main` at `7fe3699155e4ac9ce49964a6d43eb636bc125d3f429d5069b5b51e54c6a5bec7`.
- Bundle checkout and inner ZIP tree matched recursively, byte-for-byte.
- Every SHA-256 manifest entry passed.
- `node scripts/verify_genesis.mjs` passed with archive root `47b25c56b7feed9debfa1c83b57e50d92a5169a6238da8767d58ec0cc3dcb678`.
- `node --test tests/test_genesis.mjs`: 9 passed, 0 failed.
- Aggregate remains `ASSEMBLING`: conversation states are `SOURCE_CLOSED`, `OPEN`, `OPEN`; the third conversation has no raw capture.
- Obvious credential-pattern scan found no matches, but `PUBLICATION_REVIEW.md` explicitly says manual privacy, copyright, consent, and secret review is not complete. Raw captures were therefore not imported into this public repo.

## Open questions blocking full content import (round 1)

1. **Resolved for initial control plane:** this chat-connected agent owns direct writes to GitHub `main`. PC Codex may read the outer dump but writes only inside the nested `Quantum-Nexus` checkout and returns reviewable changes plus a receipt.
2. **Resolved for the current supplement:** it contains one inner ZIP and one complete bundle. The older duplicate-download copies are not candidates for import.
3. **`openui-main.zip`** — this is third-party code (the OpenUI open-source project), not original Nexus work. Vendoring the full source into this repo bloats it and creates drift risk against upstream. Recommend a pointer file (upstream repo + commit/version) instead of a full copy, unless this is meant to be a deliberate fork — human's call.
4. **`station-defense-genericc.zip`** — referenced in the design docs as an already-built, separate project. Does it get its own repo (with this repo referencing it), or live under `external/` here?
5. **Resolved for the current supplement:** no self-nested wrapper exists. The wrapper intentionally contains a distinct genesis ZIP plus its matching Git bundle.
6. **Resolved by direct execution:** both files exist in the supplement; the verifier passed and all 9 tests passed.
7. **Relationship to the `Lab` GitHub repo** (existing, separate, has the actual `nexus-kernel` / router code referenced in the AI handoff notes) — does it merge into this repo, stay separate and get referenced, or something else?
8. **Raw-capture publication decision:** the genesis package is mechanically consistent, but its own publication review is incomplete. Human review or an explicitly labelled redacted derivative is required before public import.

## Basic secret scan (round 1)

Ran a pattern scan (AWS keys, PEM private key headers, OpenAI-style `sk-` tokens, Slack tokens, GitHub tokens) across every file in the round-1 zip. Nothing matched. This is a shallow, non-exhaustive check — not a substitute for a real scan before anything sensitive-adjacent gets pushed, and it says nothing about content that isn't a well-known key format.

## Session log

- **Session 1 (2026-07-16, chat interface):** Read round-1 zip and GitHub profile/repo. Drafted this scaffold. GitHub write access broken all session — see `handoffs/HANDOFF_2026-07-16_chat-session-1.md` for full detail. Nothing pushed.

- **Session 3 (2026-07-16, ChatGPT Work):** Authenticated as `Natoshi-moto`; repository permissions reported `admin` and `push`. Performed and read back a real write test, landed the reviewed scaffold, removed the test file, verified all 11 files exactly, and independently ran the supplied genesis verifier/tests. See `handoffs/HANDOFF_2026-07-16_chatgpt-session-3.md`.

## PC Codex control-plane bootstrap

A fail-closed PC-side prototype was added after the scaffold. The real `.codex/NO_LEAK_VAULT` is local-only and ignored; the public repo contains only a redacted template. Local T1 tests observed: valid configuration passed; safe staged content passed; an exact copy of protected dump content was blocked; an obvious credential pattern was blocked; and a symlink/path escape was blocked without printing protected content. The smoke task is ready but **has not run on the user's PC**, so remote control is not yet claimed.

## PC control-plane handshake

`TASK-0001-smoke-test` completed on Fedora with Codex CLI `0.144.4`. GitHub comparison showed branch `pc/task-0001-smoke-test` exactly one commit ahead of `main`, changing only `control/receipts/TASK-0001-smoke-test.md` (10 additions, 0 deletions). The sanitized receipt was read directly from GitHub and promoted to `main` at `c636c30dcf48d189ce6ba1f1dde0a94f8f740f46`. The bounded PC task/receipt loop is therefore connected; this does not broaden the PC write boundary or waive review for later tasks.


## PC private-dump reconciliation and control-plane incident

`TASK-0002-private-dump-reconciliation` completed on Fedora. GitHub comparison showed the PC branch changed only the schema-bounded sanitized receipt, which was promoted to `main` at `fa53e99a220387c205837b514e7fcf79f5d2a6a1`. The receipt reports the nested checkout boundary passed and records aggregate category counts only.

The supplied local terminal trace also showed that the task agent opened and displayed the local vault before producing the safe receipt. No vault or raw log entered GitHub, and the registry contained no credentials, but the read/display violated policy. The launcher is now remediated with a fail-closed `PreToolUse` path block, a startup self-test, a prompt that makes the vault host-only, and stricter `AGENTS.md` language. See `handoffs/INCIDENT_2026-07-16_vault-terminal-disclosure.md`.


## PC control-plane privacy regression

`TASK-0003-control-plane-privacy-regression` completed on Fedora. GitHub comparison showed branch `pc/task-0003-control-plane-privacy-regression` exactly one commit ahead of `main`, changing only the nine-line sanitized receipt. The task agent started after the launcher's host-side hook preflight, the `PreToolUse` hook ran before every tool call shown in the local trace, and the agent made no private-control-plane, outer-dump, or network access attempt. The receipt was promoted to `main` at `0e40db743cd1e1a9d6bb3b6f0aab426dfa6ba951`.


## Provider-neutral canonical workflow

`TASK-0004-provider-neutral-canonical-chain` replaced the temporary provider-exclusive bootstrap rule with a human-owned canonical change chain. The task was opened from base `bba869ba434c58f41d50b9a96fa29c9493c07771` at `244e9d3d8384ba4bfa5efaa0caea50b8dcfdf467`. The canonical workflow landed at `203bf1c4cd0a3c07c27586b467b4cc5559db244c`, the Claude Code entrypoint at `5407d31dc2e7557894c0156104c4e70b274f20f3`, and the shared `AGENTS.md` contract at `9545c912b4438a3c1c404ab460b4f3226dcfe01f`. The receipt was read back from `main` at `96a12e5fbac00da79375f3fb15a13a44229c4143`.

The human repository owner is final authority. Claude Code, Codex, chat-connected agents, and human-authored changes now use the same task, recorded base, actor branch, verification, receipt, independent review, integration, and fast-forward synchronization chain. The Claude Code automation launcher is deliberately not claimed complete until the installed PC version and its sandbox, permissions, and hooks are verified in a separate task.


## Claude Code control-plane static bootstrap

`TASK-0005-claude-code-control-bootstrap` opened from base `84e8dd15af7dedbb7ad733a4250c975132b1e264` at `a02953194b6f00001a7aaea6fd48f9b618594d47`. Claude project deny rules landed at `90c838283926705acd19aac5143f8458748992f1`, the controlled launcher at `ef5356f081d13a78529a95e9c85e7a6a013deae0`, the provider-neutral pre-tool hook at `e74a460da24ecfd80b87c2cfc33eeafe4ab61101`, local-state ignore rules at `1dfb3fbecd04a5bfab7db790008b31832603cd55`, and the design record at `16639fe8252f733ff41b65fa4e4b9393b642bdba`. The static receipt landed at `717bf67aee7a40c8930d207e06d7ea6a45241a56`.

Local static tests in the integration environment passed JSON, shell, and Python syntax; protected Read, Edit, and Bash inputs were denied; and a safe Git status input was allowed. The launcher uses `acceptEdits`, not Claude's dangerous permission-bypass mode. Operational status remains pending until the target Fedora PC completes the separate Claude smoke task and GitHub comparison confirms a receipt-only branch.


## Claude Code operational handshake

`TASK-0006-claude-control-smoke` ran on Fedora through `bash .claude/run_task.sh` with Claude Code `2.1.211`. GitHub comparison showed branch `claude/task-0006-claude-control-smoke` exactly one commit ahead of base `a6f7dc233e48217fed9d3371c022e71f3e61d18a`, changing only the 13-line sanitized receipt. The receipt reports the correct base, valid `claude/` task branch, clean starting tree, and no private-control-plane, outer-dump, network/remote, or session Git-mutation attempt. The exact receipt was promoted to `main` at `48bc53bd9fbaf8b70d718c734175751302988955`.

Claude Code is now an operational peer worker under the provider-neutral canonical workflow. This establishes the controlled task/receipt/branch loop; every future Claude change still requires its own task, independent diff review, integration record, and fast-forward synchronization.

## TASK-0007 canonical project-map integration

PR #1 proposed the canonical project map and its sanitized task receipt from task-opening base `96230ca1469fd66b194781bd1bf8e681a2b635ce`. A separate Claude Code session returned `APPROVE`, reported no discrepancy against the recorded base, current `main`, authorized paths, required results, evidence-tier discipline, factual accuracy, stale-documentation findings, or privacy boundaries, and stated that the reviewed bytes were safe for a separate integration step.

This separate integration session independently reverified live GitHub state immediately before merging: PR head `5589d634b1898416b94e43d92d9c44e8f15397cf` was two commits ahead and zero behind unchanged `main`; the merge base was the task-opening commit; and the complete diff contained exactly `design/PROJECT_MAP.md` and `control/receipts/TASK-0007-project-map.md`. The PR was marked ready and merged with GitHub's history-preserving merge method at `0e1b76a632f1858172b6110c4aa4b288e7dff4f1`, preserving map commit `e1d35c3e53bb1cf7cb236f5fc3f7e934b815c14a` and receipt commit `5589d634b1898416b94e43d92d9c44e8f15397cf`.

`NEXUS-CAPSULE-0001` remains a `RECOMMENDATION` only. This integration grants no authority to implement it, import private or external material, alter governance, or claim the proposed unified product already exists.


## TASK-0010 no-leak secret-boundary integration

PR #2 repaired the scanner's OpenAI-style token alternative so word-internal text such as the accurate TASK-0009 branch name no longer triggers the `sk-` rule. The accepted source branch was `codex/task-0010-no-leak-secret-boundary` at reviewed head `c56c9e68ddd865a904c8217360da3c7322fb2288`, based on unchanged task-opening main `1e6fe94a786e4bd6856e09ca203ea2a46caa1ad5`.

The human repository owner supplied and attributed an external fresh Claude Code verdict of `APPROVE` for those exact bytes — `T3_RELAYED` in this integration session. This separate integration session independently reverified live GitHub state immediately before writing: the PR was open at the expected head and base; its merge base was exactly the task-opening main; it was mergeable without a reported conflict; and the complete diff contained exactly `.codex/no_leak_guard.sh`, `tests/test_no_leak_secret_pattern.sh`, and `control/receipts/TASK-0010-no-leak-secret-boundary.md`. The guard expression's only semantic text change was `sk-[A-Za-z0-9_-]{20,}` to `(^|[^A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}`; all other alternatives were byte-identical. Shell syntax and `bash tests/test_no_leak_secret_pattern.sh` passed — `T1_EXECUTED` against fetched head content.

The PR was marked ready and merged with GitHub's history-preserving `merge` method plus expected-head guard at merge commit `861747138721d5e641684e49fbfe5c6c31847c21`. The merge preserved all four source commits through head `c56c9e68ddd865a904c8217360da3c7322fb2288`; it was not squashed, rebased, force-updated, or rewritten.

Exception retained: the new lexical boundary deliberately does not flag an `sk-` shape immediately preceded by an ASCII alphanumeric character. This narrow false-negative trade-off is documented in the task receipt; the regression does not prove general secret detection.

**TASK-0009 remains blocked and unintegrated.** This merge only repairs the scanner. It does not review, approve, clear, commit, or integrate the user's staged TASK-0009 files; those files must be preserved, synchronized onto this reviewed guard, restored, cleaned of generated pycache staging, and rerun through the canonical no-leak guard before TASK-0009 can continue.
