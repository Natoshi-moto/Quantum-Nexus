"""Deterministic, standard-library-only Codex handshake."""

import sys

GREETING = "Hello from Codex"
UNEXPECTED_ARGUMENT = "codex_hello: unexpected argument\n"


def greeting():
    """Return the exact Codex greeting without consulting external state."""
    return GREETING


def main(argv=None):
    """Emit the greeting, or deterministically reject unexpected arguments."""
    arguments = sys.argv[1:] if argv is None else argv
    if arguments:
        sys.stderr.write(UNEXPECTED_ARGUMENT)
        return 2
    sys.stdout.write(greeting() + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
