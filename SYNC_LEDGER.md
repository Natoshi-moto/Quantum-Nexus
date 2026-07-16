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
