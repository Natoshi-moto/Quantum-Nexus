# PC Codex control plane

Status: bootstrap design and executable guard for a Fedora PC. It does not claim that the user's PC is connected until the smoke task is run and its branch is read back from GitHub.

## Boundary

- The outer project directory is a readable **DUMP** and is never a writable root.
- The nested `Quantum-Nexus` Git checkout is the only writable workspace.
- ChatGPT is the initial direct writer to GitHub `main`.
- PC Codex performs one bounded task on a `pc/TASK-...` branch. It cannot write `.git/` or `.codex/` while running under Codex's `workspace-write` sandbox.
- Shell-command network access is disabled. The host launcher, not the model-driven shell, performs the final guarded Git commit and optional branch push.

## NO_LEAK vault

The real `.codex/NO_LEAK_VAULT` exists only on the PC and is ignored by Git. It binds the expected dump root, nested repo root, GitHub origin, maximum staged file size, protected dump paths, protected exact SHA-256 payloads, and forbidden repo path patterns.

The guard fails closed when the vault is missing or malformed. Before a host-side commit it rejects:

- a repo root outside the configured dump or a wrong GitHub origin;
- staged paths escaping the nested checkout;
- the vault, local run logs, common secret files, configured deny globs, symlinks, or submodules;
- files above the configured size limit;
- exact copies of files under configured protected dump paths;
- configured protected payload hashes;
- common credential and private-key formats.

It never prints matched content.

## Honest limit

No local pattern guard can prove the absence of every leak. Exact-file hashing does not catch paraphrases, selected excerpts, encrypted/encoded copies, screenshots, or unknown credential formats. Therefore PC branches are never merged automatically. ChatGPT reads the diff and receipt, applies the same evidence tiers, and only then writes an accepted change to `main`.

## Task lifecycle

1. ChatGPT commits a bounded `control/tasks/TASK-*.md` envelope to `main`.
2. The PC launcher starts only from a clean `main`, pulls fast-forward, creates a matching `pc/...` branch, and starts an ephemeral Codex run.
3. Codex edits only the nested checkout and writes a sanitized receipt.
4. The host launcher stages the result and runs the NO_LEAK guard.
5. If the guard passes, the host commits. It pushes only when the human supplied `--push`.
6. ChatGPT reads the branch from GitHub, verifies the diff and receipt, and decides whether to promote it.

The first run is a smoke test, not autonomous polling. A timer or daemon may be added only after the manual round trip is proven and logged.
