"""Differential observable-contract test for fixed Claude commits and Codex."""

import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CODEX = ROOT / "experiments" / "provider_handshake" / "codex_hello.py"
SOURCE_PATH = "experiments/provider_handshake/claude_hello.py"
TEST_PATH = "tests/test_claude_hello.py"
CLAUDE_CASES = (
    (
        "Claude Code attempt 1",
        "244a30a6f4f82084514d61614fe326ab9d15213f",
        "959a780b435239331b7f4d994919506a16f5ff977de6f1c95c738fe401c3316e",
        "3d37af11c1613027baaa0f2402e243ee7567e2fa32b48c840b6153cde00b6124",
    ),
    (
        "Claude Code attempt 2",
        "e46aac801df78cf2e59d72332478625694e7fc53",
        "298dddfc01f0a3716de00e671890beade31aba2e44408b1fe84b7d33e9f57290",
        "b012b1dece884a6748f932cdfd74069f1d41d8103cd1466910ff1e8300cfe00c",
    ),
)


def git_bytes(commit, path):
    result = subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=ROOT,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise AssertionError(result.stderr.decode("utf-8", errors="replace"))
    return result.stdout


def run(script, *arguments, cwd=None, env=None):
    return subprocess.run(
        [sys.executable, str(script), *arguments],
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )


def normalized_success(provider, result):
    lines = result.stdout.splitlines()
    prefix = "Hello from "
    identity = lines[0][len(prefix):] if len(lines) == 1 and lines[0].startswith(prefix) else None
    return {
        "provider": provider,
        "identity": identity,
        "success": result.returncode == 0,
        "one_line": len(lines) == 1 and result.stdout.endswith("\n"),
        "stderr_empty": result.stderr == "",
    }


class TestProviderHandshakeDifferential(unittest.TestCase):
    def test_fixed_commits_and_codex_share_observable_contract(self):
        cases = []
        with tempfile.TemporaryDirectory() as outer:
            for index, (provider, commit, source_hash, test_hash) in enumerate(CLAUDE_CASES):
                root = Path(outer) / f"claude_{index}"
                source = root / SOURCE_PATH
                test = root / TEST_PATH
                source.parent.mkdir(parents=True)
                test.parent.mkdir(parents=True)
                source_bytes = git_bytes(commit, SOURCE_PATH)
                test_bytes = git_bytes(commit, TEST_PATH)
                self.assertEqual(hashlib.sha256(source_bytes).hexdigest(), source_hash)
                self.assertEqual(hashlib.sha256(test_bytes).hexdigest(), test_hash)
                source.write_bytes(source_bytes)
                test.write_bytes(test_bytes)

                suite = subprocess.run(
                    [sys.executable, "-m", "unittest", "-v", TEST_PATH],
                    cwd=root,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(suite.returncode, 0, suite.stdout + suite.stderr)
                cases.append((provider, source, root))

            cases.append(("Codex", CODEX, ROOT))
            normalized = []
            for provider, source, cwd in cases:
                first = run(source, cwd=cwd)
                second = run(source, cwd=cwd)
                self.assertEqual(
                    (first.returncode, first.stdout, first.stderr),
                    (second.returncode, second.stdout, second.stderr),
                )
                contract = normalized_success(provider, first)
                self.assertEqual(contract["identity"], provider.split(" attempt")[0])
                normalized.append(contract)

                module_dir = source.parent
                imported = subprocess.run(
                    [sys.executable, "-c", f"import sys; sys.path.insert(0, {str(module_dir)!r}); import {source.stem}"],
                    cwd=cwd,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual((imported.returncode, imported.stdout, imported.stderr), (0, "", ""))

                rejected_once = run(source, "unexpected", cwd=cwd)
                rejected_twice = run(source, "different", cwd=cwd)
                self.assertNotEqual(rejected_once.returncode, 0)
                self.assertEqual(rejected_once.stdout, "")
                self.assertNotEqual(rejected_once.stderr, "")
                self.assertEqual(
                    (rejected_once.returncode, rejected_once.stdout, rejected_once.stderr),
                    (rejected_twice.returncode, rejected_twice.stdout, rejected_twice.stderr),
                )

            observable = [
                (item["success"], item["one_line"], item["stderr_empty"])
                for item in normalized
            ]
            self.assertTrue(all(value == (True, True, True) for value in observable))


if __name__ == "__main__":
    unittest.main()
