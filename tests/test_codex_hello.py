"""Contract tests for the Codex provider handshake."""

import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "experiments" / "provider_handshake" / "codex_hello.py"
EXPECTED = "Hello from Codex"


def load_module(path=SCRIPT):
    spec = importlib.util.spec_from_file_location("codex_hello", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestCodexHello(unittest.TestCase):
    def run_cli(self, *arguments, cwd=None, env=None, script=SCRIPT):
        return subprocess.run(
            [sys.executable, str(script), *arguments],
            cwd=cwd or ROOT,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )

    def assert_success(self, result):
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, EXPECTED + "\n")
        self.assertEqual(result.stderr, "")

    def test_callable_exact_contract(self):
        self.assertEqual(load_module().greeting(), EXPECTED)

    def test_ordinary_cli(self):
        self.assert_success(self.run_cli())

    def test_isolated_environment_and_unrelated_cwd(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_cli(
                cwd=directory,
                env={"PATH": os.environ.get("PATH", ""), "PYTHONNOUSERSITE": "1"},
            )
        self.assert_success(result)

    def test_repeatability(self):
        first = self.run_cli()
        second = self.run_cli()
        self.assertEqual(
            (first.returncode, first.stdout, first.stderr),
            (second.returncode, second.stdout, second.stderr),
        )
        self.assert_success(first)

    def test_import_is_silent(self):
        result = subprocess.run(
            [sys.executable, "-c", "import codex_hello"],
            cwd=SCRIPT.parent,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual((result.returncode, result.stdout, result.stderr), (0, "", ""))

    def test_unexpected_argument_is_deterministic(self):
        first = self.run_cli("unexpected")
        second = self.run_cli("different")
        self.assertEqual(first.returncode, 2)
        self.assertEqual(first.stdout, "")
        self.assertEqual(first.stderr, "codex_hello: unexpected argument\n")
        self.assertEqual(
            (first.returncode, first.stdout, first.stderr),
            (second.returncode, second.stdout, second.stderr),
        )

    def test_temporary_tamper_is_detected(self):
        source = SCRIPT.read_text(encoding="utf-8")
        changed = source.replace(EXPECTED, "Hello from Tampered Codex", 1)
        self.assertNotEqual(source, changed)
        with tempfile.TemporaryDirectory() as directory:
            altered = Path(directory) / "codex_hello.py"
            altered.write_text(changed, encoding="utf-8")
            result = self.run_cli(cwd=directory, script=altered)
        with self.assertRaises(AssertionError):
            self.assert_success(result)


if __name__ == "__main__":
    unittest.main()
