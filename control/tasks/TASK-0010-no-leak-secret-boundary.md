# TASK-0010 — no-leak secret-pattern token boundary regression

Status: `READY`

## Authority

The human repository owner authorized material hardening discovered during the cross-provider handshake audit on 2026-07-16.

## Recorded base

- canonical repository: `Natoshi-moto/Quantum-Nexus`
- canonical branch: `main`
- base before this task was opened: `7a815bf194ccf1d23a2116526e633d9d2262cf8a`
- declared actor: Codex in ChatGPT Work
- actor branch: `codex/task-0010-no-leak-secret-boundary`

## Triggering evidence

The TASK-0009 host run staged its accurate receipt and was stopped by:

`NO_LEAK BLOCKED: a staged file matches an obvious credential or private-key pattern`

Direct source inspection established that the canonical expression `sk-[A-Za-z0-9_-]{20,}` matched the word-internal substring `sk-0009-...` inside the literal branch name `pc/task-0009-codex-cross-provider-review-and-implementation`.

This task treats that as a false positive requiring a boundary fix. It does not waive the scanner or authorize bypassing the stopped TASK-0009 run.

## Objective

Add a minimal lexical boundary to the OpenAI-style `sk-` alternative so that:

- a standalone or delimiter-prefixed synthetic `sk-` token shape still matches;
- an `sk-` substring embedded inside an alphanumeric word such as `task-...` or `risk-...` does not match;
- every other existing credential/private-key alternative remains byte-for-byte unchanged.

Add a regression test that executes the exact expression extracted from the guard source.

## Writable paths

- `.codex/no_leak_guard.sh`
- `tests/test_no_leak_secret_pattern.sh`
- `control/receipts/TASK-0010-no-leak-secret-boundary.md`

No other path is authorized.

## Required verification

1. `bash -n .codex/no_leak_guard.sh`
2. `bash -n tests/test_no_leak_secret_pattern.sh`
3. `bash tests/test_no_leak_secret_pattern.sh`
4. Confirm the test constructs synthetic credential shapes at runtime so the test source itself does not contain a scanner-triggering literal.
5. Confirm the original alternatives for AWS access-key IDs, PEM private-key headers, GitHub tokens, GitHub fine-grained tokens, and Slack tokens are unchanged.
6. Confirm only the three authorized paths differ from the task-opening commit.
7. Read all three branch files back from GitHub after committing.
8. Do not access the host-only vault, local-run logs, outer dump, or private material.

## Required test cases

Must match:

- standalone synthetic OpenAI-style `sk-` shape with at least 20 allowed characters;
- the same shape after a space, quote, equals sign, slash, and underscore;
- synthetic forms of every other pre-existing scanner alternative.

Must not match:

- `task-0009-codex-cross-provider-review-and-implementation`;
- `risk-0000000000000000000000000000`;
- shorter-than-threshold `sk-` text;
- ordinary prose containing `task-`.

## Receipt

Create `control/receipts/TASK-0010-no-leak-secret-boundary.md` containing:

- task ID, actor, branch, base, and verdict;
- exact changed paths;
- triggering false positive;
- exact old and new `sk-` alternatives;
- commands and observed results with evidence tiers;
- limitations and readiness for independent review.

## Forbidden

- Do not read or modify the real vault or local-run logs.
- Do not weaken, delete, bypass, or globally disable secret scanning.
- Do not change non-`sk-` alternatives.
- Do not modify or commit TASK-0009 work.
- Do not merge, force-update, or rewrite history.
- Do not claim the stopped TASK-0009 run passed its host workflow.
