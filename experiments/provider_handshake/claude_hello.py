"""Deterministic Claude Code hello-world handshake artifact.

Standard-library only. Importing this module has no side effects: it only
defines a constant and two functions, and only runs code when executed
directly as a script.
"""

import sys

GREETING = "Hello from Claude Code"

_UNEXPECTED_ARGUMENT_MESSAGE = "claude_hello: unexpected argument\n"
_UNEXPECTED_ARGUMENT_EXIT_CODE = 2


def greeting():
    """Return the deterministic 22-code-point greeting string."""
    return GREETING


def main(argv=None):
    """CLI entry point. Rejects any positional argument deterministically.

    Argument presence is inspected only to reject it; argument content is
    never read into or reflected by the greeting.
    """
    if argv is None:
        argv = sys.argv[1:]
    if argv:
        sys.stderr.write(_UNEXPECTED_ARGUMENT_MESSAGE)
        return _UNEXPECTED_ARGUMENT_EXIT_CODE
    sys.stdout.write(greeting() + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
