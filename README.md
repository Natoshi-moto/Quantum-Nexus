# Quantum Nexus

This is the canonical, self-documenting home of the Nexus project. If you are a new builder — human or AI — **this file is the only thing you need to read first.**

## What Nexus is

A research and infrastructure project spanning: an append-only, hash-verified archive of the project's own founding AI conversations (`genesis/`); a whole-system whitepaper and technical spec; defensive-security design work (sandboxing untrusted agents, P2P task exchange, hardware attestation); and a cross-model verification discipline where multiple AI providers (Claude, ChatGPT, Gemini, DeepSeek, Grok) check each other's work rather than self-report being trusted.

This repo is the record of that work. It is not, itself, a claim that everything in it is finished, correct, or safe to treat as authoritative — see `AGENTS.md` and `GENESIS_CONSTITUTION` (pending import) for the rules that govern that.

## Where things live

| Folder | Contents | Status |
|---|---|---|
| `genesis/` | Append-only capture archive of the founding AI conversations (`NEXUS-GENESIS-0001`) — hash-chained, non-executable evidence | pending import |
| `whitepaper/` | The whole-system whitepaper and technical spec | pending import |
| `audit-packs/` | Per-provider packages so any AI (Claude, Gemini, DeepSeek, Grok, etc.) can independently verify project claims | pending import |
| `design/` | Defensive-security design docs (Station, Watchtower, P2P attestation) | pending import |
| `handoffs/` | Dated session handoff notes from any agent (CLI or chat) that touched the project | pending import |
| `transcripts/` | Index of every session/round that touched this project, with links where linkable | pending import |
| `external/` | Third-party code this project depends on or references, kept separate from original work | pending import |

"Pending import" means: the content exists in the working `.zip` snapshot but hasn't been moved into the repo yet, because a few structural decisions need the human's sign-off first. See `SYNC_LEDGER.md` for exactly what's outstanding.

## The sync model (PC folder ↔ .zip ↔ this repo)

The human keeps a general working folder (`Quantum-Nexus`) on their PC. That folder is a broader workspace and **is not itself trusted as repo-ready** — it may contain material that should never reach a public repo. The single, deliberate crossing point from PC → GitHub is a versioned `.zip` snapshot (currently `Quantum_Nexus_v0_0_0.zip`) that the human exports and hands to whichever AI is doing the sync pass that round.

Rule: nothing reaches this repo except through that named, versioned zip. Not the general folder directly. Every round, the zip version and the repo's HEAD commit should agree — see `SYNC_LEDGER.md` for the running record and any flagged drift.

## Working rules

See `AGENTS.md` for the full builder contract. Short version: verify before claiming, non-execution firewall on all archived/raw content, append-only history, flag a concern once then execute the human's call, log every session.
