#!/usr/bin/env python3
"""Fail closed before Codex tools can access private control-plane files."""

from __future__ import annotations

import json
import sys
from typing import Any, Iterable


PROTECTED_MARKERS = (
    ".codex",
    "no_leak_vault",
    "local-runs",
)


def strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, child in value.items():
            yield str(key)
            yield from strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from strings(child)


def deny() -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": (
                        "Private control-plane files are host-only and unavailable "
                        "to the task agent. Continue without inspecting them."
                    ),
                }
            },
            separators=(",", ":"),
        )
    )


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, TypeError):
        print("Private control-plane hook rejected malformed input.", file=sys.stderr)
        return 2

    tool_name = str(payload.get("tool_name", ""))
    if tool_name not in {"Bash", "apply_patch"}:
        return 0

    tool_input = payload.get("tool_input", {})
    normalized = "\n".join(strings(tool_input)).casefold()
    if any(marker in normalized for marker in PROTECTED_MARKERS):
        deny()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
