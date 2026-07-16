# TASK-0001 — PC control-plane smoke test

Status: `READY`

## Objective

Prove that Codex is running from the nested `Quantum-Nexus` checkout with the configured origin and NO_LEAK boundary. Do not build or import project content.

## Writable paths

- `control/receipts/TASK-0001-smoke-test.md` only.

## Required checks

1. Run `.codex/no_leak_guard.sh --config-only`.
2. Confirm the current Git root equals the vault's `REPO_ROOT` without writing the absolute path to the receipt.
3. Confirm the normalized `origin` equals `Natoshi-moto/Quantum-Nexus`.
4. Record the current Git HEAD, current branch, Codex CLI version, and whether the working tree was clean at task start.
5. Confirm that no file outside the nested Git root was written.

## Forbidden

- Do not quote, summarize, hash, copy, attach, or export content from any `NO_EXPORT_PATH`.
- Do not modify project files, `.git/`, `.codex/`, the outer dump, or GitHub.
- Do not use network tools or commands.
- Do not include absolute local paths, usernames, hostnames, credentials, environment variables, or dump filenames in the receipt.

## Receipt

Create `control/receipts/TASK-0001-smoke-test.md` with evidence tiers and only these fields: task ID, PASS/FAIL, Git HEAD, branch, Codex CLI version, guard result, root-boundary result, origin result, outside-write result, and any blocker stated without sensitive local detail.
