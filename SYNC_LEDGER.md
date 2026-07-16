# Sync Ledger

Running record of every zip snapshot handed to a chat-based agent, matched against the repo's state at that time. This is how drift between the PC folder, the zip, and GitHub gets caught instead of silently accumulating.

## Log

| Round | Zip received | Repo HEAD before | Repo HEAD after | Status |
|---|---|---|---|---|
| 1 | `Quantum_Nexus_v0_0_0.zip` (2026-07-16) | `bb937dee` (LICENSE only) | *pending* | Skeleton drafted (README, AGENTS.md, folder placeholders). GitHub write access failed all session (`403 Resource not accessible by integration`, 5+ attempts) — nothing actually pushed. Content bundled in `PENDING_SCAFFOLD.md` for next session. Project content **not yet imported** — see open questions below. |

## Open questions blocking full content import (round 1)

1. **Single writer to GitHub?** Proposing the chat-based agent is the only one that pushes, so there's no race between it and the CLI agent. Needs the human's confirmation — if the CLI agent also has push access, we need a rule for who owns what path.
2. **Three byte-identical copies of `Nexus_Auditable_Genesis_v0.1_ASSEMBLING` (`.zip` and `.bundle`, suffixed `(1)`/`(2)`)** — confirmed identical by hash, look like duplicate-download artifacts. Safe to collapse to one canonical copy unless there's a reason to keep the duplicates.
3. **`openui-main.zip`** — this is third-party code (the OpenUI open-source project), not original Nexus work. Vendoring the full source into this repo bloats it and creates drift risk against upstream. Recommend a pointer file (upstream repo + commit/version) instead of a full copy, unless this is meant to be a deliberate fork — human's call.
4. **`station-defense-genericc.zip`** — referenced in the design docs as an already-built, separate project. Does it get its own repo (with this repo referencing it), or live under `external/` here?
5. **`Quantum Nexus v0.0.0.zip` nested inside itself** in the round-1 upload (a snapshot containing an earlier snapshot of the same archive). Assuming this is an artifact of how the export was built, not intentional — flagging in case it's not.
6. **`genesis/README.md`'s own verify commands** (`node scripts/verify_genesis.mjs`, `node --test tests/test_genesis.mjs`) **reference a `scripts/` and `tests/` folder that isn't in the round-1 zip.** Either they exist on the PC and weren't included, or they haven't been written yet — CLI agent, please confirm which.
7. **Relationship to the `Lab` GitHub repo** (existing, separate, has the actual `nexus-kernel` / router code referenced in the AI handoff notes) — does it merge into this repo, stay separate and get referenced, or something else?

## Basic secret scan (round 1)

Ran a pattern scan (AWS keys, PEM private key headers, OpenAI-style `sk-` tokens, Slack tokens, GitHub tokens) across every file in the round-1 zip. Nothing matched. This is a shallow, non-exhaustive check — not a substitute for a real scan before anything sensitive-adjacent gets pushed, and it says nothing about content that isn't a well-known key format.

## Session log

- **Session 1 (2026-07-16, chat interface):** Read round-1 zip and GitHub profile/repo. Drafted this scaffold. GitHub write access broken all session — see `handoffs/HANDOFF_2026-07-16_chat-session-1.md` for full detail. Nothing pushed.
