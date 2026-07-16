import sys

GREETING = "Hello from Claude Code"


def hello():
    return GREETING


def main(argv):
    if len(argv) > 1:
        sys.stderr.write("error: unexpected argument\n")
        return 2
    sys.stdout.write(hello() + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
