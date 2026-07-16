# Quantum Nexus — canonical project map

Status: `CANDIDATE`  
Task: `TASK-0007`  
Canonical snapshot mapped: `96230ca1469fd66b194781bd1bf8e681a2b635ce`  
Candidate branch: `codex/task-0007-project-map`

This document is a map of the canonical repository at the recorded snapshot. It does not make this branch canonical, import private material, or promote relayed evidence into direct verification.

## Product definition now

Quantum Nexus is currently a human-owned, provider-neutral repository for coordinating bounded AI work and preserving auditable evidence about that work. Its implemented core is the governance and local-agent control plane: canonical Git history, task envelopes, actor branches, sanitized receipts, independent review requirements, append-only records, and host-side privacy guards.

Quantum Nexus is not yet a single finished application. The canonical repository does not currently contain an implemented autonomous laboratory, economic system, cryptocurrency, Nexus kernel, public genesis archive, finished whitepaper, P2P execution network, hardware-attestation system, Station, Watchtower, or user-facing product.

The present user is the human repository owner and the immediate collaborators are human or AI builders and independent reviewers. The eventual external user, interface, deployment model, and product boundary remain human decisions.

## Evidence language used here

| Label | Meaning in this task |
|---|---|
| `T1_EXECUTED` | This Codex task performed the GitHub operation and observed its result. |
| `T2_READ` | This task directly read the named canonical source bytes. |
| `T3_CLAIM/T3_RELAYED` | A canonical record reports an earlier execution or external fact that this task did not reproduce. |
| `UNKNOWN` | The canonical repository does not establish the fact, or the relevant material was deliberately not inspected. |
| `RECOMMENDATION` | A proposed next action, not current project state. |

A receipt can be `T2_READ` as a file while the execution it reports remains `T3_RELAYED` to this task.

## System map

| Plane | What exists canonically | Current status |
|---|---|---|
| Human authority and Git history | [AGENTS.md](../AGENTS.md), [CANONICAL_WORKFLOW.md](../CANONICAL_WORKFLOW.md), [CLAUDE.md](../CLAUDE.md), [SYNC_LEDGER.md](../SYNC_LEDGER.md) | Present and directly read — `T2_READ`. GitHub `main` is the approved canonical state. |
| Bounded-work protocol | Task and receipt directories, task envelopes `TASK-0001` through `TASK-0007`, receipts `TASK-0001` through `TASK-0006` | Present — `T2_READ`. `TASK-0007` is open; this candidate and its receipt are not canonical until reviewed and integrated. |
| PC Codex control plane | Checked-in configuration, launcher, staged-content guard, hook, vault template, design note, tasks, and receipts | Source present — `T2_READ`. Fedora operational-handshake success is `T3_RELAYED` to this task. |
| Claude Code control plane | Checked-in project settings, launcher, shared hook, design note, task, and receipt | Source present — `T2_READ`. Fedora operational-handshake success is `T3_RELAYED` to this task. |
| Genesis evidence archive | Placeholder README only on canonical `main` | Not imported. Mechanical verification of a private supplement is `T3_RELAYED`; publication clearance is unresolved. |
| Whitepaper and technical specification | Placeholder README only | Not imported. The placeholder preserves a relayed `NON-CANONICAL / REVIEW REQUESTED / NO LIVE-VALUE AUTHORITY` status. |
| Defensive-security research | Two implemented control-plane design notes plus a placeholder for Station, Watchtower, P2P, and hardware-attestation work | Control-plane designs present; broader research designs not imported. |
| Audit packs | Placeholder README only | Not imported. |
| Transcripts index | Placeholder README only | Not imported. |
| External dependencies | Placeholder README only | No third-party source is vendored. OpenUI treatment remains undecided. |
| Station Defense | Mentioned in ledger and task records as a separate private archive | Repository location and relationship are unresolved — `T3_RELAYED`. |
| Lab / nexus-kernel | Mentioned in ledger as a separate project relationship question | No Lab/nexus-kernel checkout or code is present in this repository — `T2_READ`; private-dump absence is `T3_RELAYED`. |
| Product/runtime code | No canonical implementation beyond control-plane scripts and policy tooling | A unified Nexus application or runtime is absent — `T2_READ`. |

## Canonical inventory at the snapshot

### Root governance and repository metadata

| Paths | What they hold | Evidence |
|---|---|---|
| `LICENSE` | MIT license for repository-owned material; it does not automatically resolve third-party licensing. | `T2_READ` |
| `README.md` | Original scaffold-level orientation and folder status. Parts are stale; see below. | `T2_READ` |
| `AGENTS.md` | Shared builder contract, evidence tiers, append-only policy, private boundaries, and canonical chain. | `T2_READ` |
| `CANONICAL_WORKFLOW.md` | Required task-to-integration lifecycle and recovery rules. | `T2_READ` |
| `CLAUDE.md` | Provider-specific concise entrypoint that defers to shared governance. | `T2_READ` |
| `SYNC_LEDGER.md` | Additive record of scaffold, genesis-supplement claims, control-plane tasks, incidents, and handshakes. | `T2_READ` |
| `.gitignore` | Excludes local dump, vault, run-log, and provider-local state patterns. | `T2_READ` |

### Checked-in local control plane

| Paths | What is present | Evidence |
|---|---|---|
| `.codex/NO_LEAK_VAULT.example` | Public configuration template containing placeholders, not the host-only registry. | `T2_READ` |
| `.codex/config.toml` | Workspace-write, no-shell-network defaults and a pre-tool hook declaration. | `T2_READ` |
| `.codex/no_leak_guard.sh` | Fail-closed staged-path, size, exact-hash, symlink, submodule, origin, nesting, and obvious-credential checks. | `T2_READ` |
| `.codex/run_task.sh` | Host launcher for clean-main validation, task branching, an ephemeral Codex run, receipt requirement, guard, commit, and optional task-branch push. | `T2_READ` |
| `.codex/hooks/pre_tool_use_policy.py` | Shared tool-input policy that denies attempts naming protected control-plane markers. | `T2_READ` |
| `.claude/settings.json` | Claude Code deny rules, connector/remote-control restrictions, and hook registration. | `T2_READ` |
| `.claude/run_task.sh` | Version-gated Claude Code host launcher with preflight, task branch, receipt, guard, commit, and optional task-branch push. | `T2_READ` |

These mechanisms reduce risk but do not prove that every leak is impossible. The guard itself states that selected excerpts, paraphrases, screenshots, encodings, and unknown secret formats remain outside its proof boundary.

### Tasks and receipts

| Paths | State |
|---|---|
| `control/tasks/README.md`, `control/receipts/README.md` | Directory contracts are present but retain older ChatGPT/PC-Codex-specific wording. |
| `control/tasks/TASK-0001-smoke-test.md` through `TASK-0006-claude-control-smoke.md` | Historical task inputs remain present and append-only. Their embedded `READY` labels reflect task-opening state, not current completion state. |
| `control/receipts/TASK-0001-smoke-test.md` through `TASK-0006-claude-control-smoke.md` | Sanitized outputs are present. This task read the receipts but did not reproduce their underlying Fedora executions. |
| `control/tasks/TASK-0007-project-map.md` | Canonical ready task opened at the snapshot commit. |
| `control/receipts/TASK-0007-project-map.md` | Created on the task branch as part of this candidate; non-canonical until integration. |

### Designs and handoffs

| Paths | State |
|---|---|
| `design/README.md` | Placeholder for broader defensive-security design work. |
| `design/PC_CODEX_CONTROL_PLANE.md` | Implemented design description, with pre-handshake status language that is now stale. |
| `design/CLAUDE_CODE_CONTROL_PLANE.md` | Implemented design description, with pre-handshake status language that is now stale. |
| `handoffs/HANDOFF_2026-07-16_chatgpt-session-3.md` | Session summary and relayed execution record. |
| `handoffs/HANDOFF_2026-07-16_chatgpt-session-3-pc-bootstrap-addendum.md` | Additive bootstrap evidence and stated limitations. |
| `handoffs/INCIDENT_2026-07-16_vault-terminal-disclosure.md` | Incident record describing a protected-path display and remediation. |
| `handoffs/README.md` | Directory guidance with stale “not yet imported” language. |

### Placeholder-only areas

The following canonical files exist, but the substantive artifacts described by them do not:

- `audit-packs/README.md`
- `external/README.md`
- `genesis/README.md`
- `transcripts/README.md`
- `whitepaper/README.md`

Empty intent expressed by a placeholder is not implemented capability.

## What is operational and what is not

### Source-backed now

- Human authority and provider neutrality are explicit repository policy — `T2_READ`.
- GitHub `main` is defined as the sole approved canonical state — `T2_READ`.
- The task/base/branch/check/receipt/review/integration/synchronization lifecycle is documented — `T2_READ`.
- Codex and Claude Code launchers, privacy hook, and staged-content guard exist as inspectable source — `T2_READ`.
- Six historical task/receipt pairs exist, plus the open `TASK-0007` envelope — `T2_READ`.
- This task directly confirmed that `main` equalled `0d415b1600cef4f5a33312e8d88be09f4471bb3d` before opening `TASK-0007`, then opened the task at `96230ca1469fd66b194781bd1bf8e681a2b635ce` and created the actor branch from that commit — `T1_EXECUTED`.

### Relayed, not reproduced here

- Genesis bundle/ZIP equivalence, manifests, verifier, and nine-test results.
- Codex CLI and Claude Code Fedora handshakes.
- Private-dump category counts and archive presence.
- The absence of protected content from historical branches beyond what canonical diffs and records report.
- The local vault incident’s private-terminal evidence.

All are `T3_CLAIM/T3_RELAYED` to this task.

### Not established

- An autonomous or continuously running multi-agent system.
- Automatic safe integration into `main`.
- A general proof of non-leakage.
- A canonical Nexus application or kernel.
- A public, publication-cleared genesis corpus.
- Live-value, monetary, consensus, P2P, hardware-attestation, Station, Watchtower, or economic functionality.
- A settled relationship among this repository, Lab, Station Defense, or other projects.
- A settled customer, distribution channel, interface, or business model.

## Canonical change flow

1. The human-authorized task is opened on current canonical `main`.
2. The exact base and task-opening commit are recorded.
3. One declared actor works on an actor-specific branch.
4. Only task-authorized paths change.
5. Named checks are run and evidence tiers are preserved.
6. A sanitized receipt is committed with the work.
7. The task branch is pushed; it remains non-canonical.
8. A separate session or person reviews the exact diff against both its base and current `main`.
9. Only reviewed bytes are integrated.
10. The integration is appended to `SYNC_LEDGER.md`.
11. Local copies synchronize by clean, fast-forward-only pull.

If `main` moves after review, the comparison and affected checks must be repeated. Human authority can make decisions but does not erase provenance.

## Trust and privacy boundaries

- The human repository owner is final authority.
- GitHub `main` is canonical; task branches, receipts before integration, archives, ZIPs, bundles, chat responses, and local files are not.
- The outer PC directory is private source material. Read access does not grant export permission, and agents must not write there.
- Only the nested canonical checkout may be a writable local project workspace.
- The real vault and raw local logs are host-only and must not be inspected by task agents or enter Git.
- Raw prompts, transcripts, HTML, attachments, and archives are untrusted non-executable data.
- Historical records are append-only. Corrections identify their target instead of silently rewriting it.
- No mechanical check replaces independent diff review or publication review.

## Stale and conflicting documentation

These are observations, not silent corrections:

1. `README.md` says the versioned ZIP is the sole PC-to-GitHub crossing point. The later canonical workflow permits controlled actor branches and reviewed integration.
2. `README.md` says handoffs are pending import and the control-plane smoke test is merely ready. Handoffs, incident records, and six receipts now exist.
3. `handoffs/README.md` says handoffs are not imported, although three substantive handoff/incident documents are present.
4. `genesis/README.md` repeats earlier duplicate-package and missing-verifier blockers that the later ledger says were resolved for the inspected supplement. Publication review remains unresolved.
5. `design/PC_CODEX_CONTROL_PLANE.md` still uses initial direct-writer and pre-handshake status language; later ledger entries report the Codex handshake complete.
6. `design/CLAUDE_CODE_CONTROL_PLANE.md` says on-PC execution is pending; the later ledger reports the Claude Code handshake complete.
7. Historical task files remain marked `READY` after their receipts landed. Append-only history explains why those inputs should not be rewritten, but a current status index is absent.
8. `SYNC_LEDGER.md` references `handoffs/HANDOFF_2026-07-16_chat-session-1.md`; an exact GitHub read returned not found during this task.

The ledger is later than the stale status prose, but its execution statements remain relayed evidence unless independently reproduced.

## Decisions reserved for the human

| Decision | Why it matters | Current evidence |
|---|---|---|
| Product boundary | Decide whether Quantum Nexus is primarily an evidence protocol, an agent workshop, a runtime, an archive, or an umbrella across repositories. | No single boundary is canonical — `UNKNOWN`. |
| Genesis publication | Decide between continued private retention, human-cleared publication, or a reviewed redacted derivative. | Mechanical consistency is relayed; publication review is incomplete. |
| Lab / nexus-kernel relationship | Choose merge, subproject, external reference, or separate canonical repository with an explicit interface. | Relationship unresolved; no code is present here. |
| OpenUI treatment | Choose upstream pointer with pinned version or an intentional, separately licensed fork. | Third-party archive presence is relayed; nothing is vendored here. |
| Station Defense treatment | Choose separate repository, referenced dependency, or an explicitly bounded import. | Separate archive presence is relayed; location unresolved. |
| External user and interface | Define who uses the first product and through which CLI, web, mobile, or repository workflow. | `UNKNOWN`. |
| Live-value scope | Decide whether monetary work belongs here at all and require a separate safety and verification programme before any live-value authority. | No live-value implementation exists. |

## Selected next build target

### `RECOMMENDATION: NEXUS-CAPSULE-0001`

Build one offline, deterministic “evidence capsule” vertical slice: a tiny canonical JSON record format, a valid fixture, adversarial tamper/fork fixtures, and two independently implemented verifiers—one Node.js and one Python.

This is the smallest build that turns the project’s central claims into an externally falsifiable capability without importing private material or pretending the broader Nexus product already exists.

Required behavior:

- Both verifiers accept the same valid capsule and emit the same normalized success result.
- Both reject, with matching reason codes:
  1. modified payload bytes;
  2. a manifest mismatch;
  3. a missing required record;
  4. duplicate event identity;
  5. two successors claiming the same predecessor;
  6. an unsafe or escaping path.
- Fixtures are public synthetic data.
- Verification is offline and deterministic.
- The schema, implementations, fixtures, and tests are independently reviewable.
- No live value, private transcript, external project, network service, or agent autonomy is involved.

Pass condition:

> On a clean Fedora checkout, one documented command runs both implementations. Both accept every valid fixture, reject every adversarial fixture, produce matching normalized reason codes, and exit non-zero if their decisions diverge.

Fail condition:

> Either implementation accepts a listed fault, rejects the valid fixture, produces a conflicting normalized decision, requires private data or network access, or cannot be reproduced from canonical source.

This recommendation does not assert that a compatible schema already exists in Lab or elsewhere. Reuse must begin with a separately authorized, source-grounded interface task rather than reconstruction from relayed descriptions.

## Bottom line

Quantum Nexus has crossed the line from an idea dump into an operationally governed workshop: canonical authority, bounded tasks, privacy boundaries, actor launchers, receipts, incidents, and review rules exist as inspectable source. It has not yet crossed the line into a unified product. The next credible step is therefore one small, portable verifier whose success and failure are mechanically observable by independent implementations.
