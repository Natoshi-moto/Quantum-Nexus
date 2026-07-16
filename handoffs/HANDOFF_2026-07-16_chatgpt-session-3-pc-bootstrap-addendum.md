# Session 3 addendum — PC Codex bootstrap

This addendum is additive. It does not rewrite the earlier session handoff.

## T1_EXECUTED in an isolated local test repository

- `.codex/no_leak_guard.sh --config-only` accepted a correctly nested dump/repo configuration and normalized GitHub origin.
- A safe staged text file passed.
- A staged file byte-identical to a configured protected dump file was blocked.
- A staged OpenAI-style credential pattern was blocked.
- A staged symlink/path escape was blocked.
- Block messages identified only the rule category; protected bytes were not printed.
- Both shell scripts passed `bash -n`. `shellcheck` was unavailable in this environment.

## Added to the public repository

- Repo-scoped `workspace-write` / no-shell-network defaults.
- Local-only NO_LEAK vault template and Git ignore rules.
- Fail-closed staged-content guard.
- Host launcher that starts from clean `main`, creates a `pc/TASK-...` branch, runs ephemeral Codex with no approval escape, requires a sanitized receipt, then stages and guards the result before any commit.
- Task and receipt directories plus `TASK-0001-smoke-test.md`.
- A design note that states the guard's limits and forbids automatic merge.

## Claim boundary

This is a tested bootstrap, not proof of connection to the user's Fedora PC. Connection exists only after the user creates the real local vault, runs the smoke launcher, pushes its `pc/...` branch, and this ChatGPT session reads the branch and receipt back from GitHub.

The guard catches configured paths, exact full-file copies, common secret formats, path escapes, symlinks, submodules, and oversized files. It cannot prove that paraphrases, excerpts, screenshots, encodings, or unknown secret formats are absent. Human/ChatGPT diff review remains mandatory before promotion to `main`.

<!-- FILE FOOTER
SCOPE: Additive PC control-plane bootstrap evidence for ChatGPT session 3.
LOAD-BEARING: Local tests passed; PC activation has not happened and is not claimed.
DECISIONS: Outer dump readable-only; nested repo writable; real NO_LEAK vault never enters Git; no automatic merge.
OPEN: Run and read back TASK-0001 on the user's PC.
LAST-EDIT: ChatGPT Work · 2026-07-16.
-->
