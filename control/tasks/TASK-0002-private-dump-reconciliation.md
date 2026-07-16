# TASK-0002 — private-dump reconciliation

Status: `READY`

## Objective

Inspect the outer dump read-only and determine what project categories actually exist there, while exporting no protected material. Produce only the sanitized receipt named below. Do not import anything into the public repository.

## Writable paths

- `control/receipts/TASK-0002-private-dump-reconciliation.md` only.

## Required checks

Report only these bounded facts:

1. Whether the writable Git checkout is correctly nested inside the configured dump.
2. Count of duplicate genesis ZIP artifacts and count of duplicate genesis bundle artifacts.
3. Whether a genesis verifier and adversarial test suite are present inside any inspected package: `present`, `absent`, or `unknown`.
4. Whether a third-party UI source archive is present: boolean only.
5. Whether a separate Station Defense archive is present: boolean only.
6. Whether an actual Lab/nexus-kernel Git checkout is present inside this dump: boolean only.
7. Counts of top-level dump entries classified as: documentation, archive, Git bundle, executable/application, directory, or unknown.
8. A recommendation consisting only of opaque labels `IMPORT_CANDIDATE`, `REFERENCE_ONLY`, `PRIVATE_REVIEW_REQUIRED`, or `UNKNOWN`, with counts for each label.

## Forbidden

- Do not write anywhere outside the required receipt.
- Do not modify, unpack, rename, delete, move, commit, push, or execute dump content.
- Do not use network tools or commands.
- Do not include absolute or relative paths, filenames, usernames, hostnames, URLs, hashes, byte sizes, timestamps, excerpts, summaries of protected prose, archive member names, or credentials.
- Do not reveal the contents of `.codex/NO_LEAK_VAULT`.
- Do not infer absent material as present.

## Receipt

Create `control/receipts/TASK-0002-private-dump-reconciliation.md` containing:

- task ID and PASS/FAIL;
- evidence tier for every field;
- the eight bounded results above;
- any blocker in generic language only.

The receipt must contain no information outside this schema.
