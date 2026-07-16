"""Tests for experiments/provider_handshake/claude_hello.py.

Covers the imported-callable contract, the CLI subprocess contract, the
addendum's additional determinism/isolation checks, and the required
negative control against a deliberately mutated, non-repository temporary
copy of the implementation.
"""

import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_PATH = os.path.join(
    REPO_ROOT, "experiments", "provider_handshake", "claude_hello.py"
)
MODULE_DIR = os.path.dirname(SCRIPT_PATH)

EXPECTED_GREETING = "Hello from Claude Code"
EXPECTED_STDOUT = "Hello from Claude Code\n"
EXPECTED_UNEXPECTED_ARG_STDERR = "claude_hello: unexpected argument\n"
EXPECTED_UNEXPECTED_ARG_EXIT_CODE = 2


def _load_module():
    spec = importlib.util.spec_from_file_location("claude_hello", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


claude_hello = _load_module()


def _assert_matches_exact_output_contract(proc):
    assert proc.stdout == EXPECTED_STDOUT, "stdout does not match contract"
    assert proc.stderr == "", "stderr is not empty"
    assert proc.returncode == 0, "exit status is not zero"


class TestClaudeHelloCallable(unittest.TestCase):
    def test_greeting_returns_expected_string(self):
        result = claude_hello.greeting()
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 22)
        self.assertEqual(result, EXPECTED_GREETING)

    def test_greeting_requires_no_arguments(self):
        result = claude_hello.greeting()
        self.assertEqual(result, EXPECTED_GREETING)


class TestClaudeHelloSubprocessContract(unittest.TestCase):
    def _run_cli(self, args=None):
        return subprocess.run(
            [sys.executable, SCRIPT_PATH] + (args or []),
            cwd=REPO_ROOT,
            env=dict(os.environ),
            capture_output=True,
            text=True,
        )

    def test_cli_exact_output_contract(self):
        proc = self._run_cli()
        _assert_matches_exact_output_contract(proc)

    def test_cli_two_independent_runs_are_byte_identical(self):
        first = self._run_cli()
        second = self._run_cli()
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual(first.stderr, second.stderr)
        self.assertEqual(first.returncode, second.returncode)

    def test_cli_unexpected_argument_is_rejected_deterministically(self):
        first = self._run_cli(["--unexpected"])
        second = self._run_cli(["--unexpected"])
        self.assertEqual(first.stdout, "")
        self.assertEqual(first.stderr, EXPECTED_UNEXPECTED_ARG_STDERR)
        self.assertEqual(first.returncode, EXPECTED_UNEXPECTED_ARG_EXIT_CODE)
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual(first.stderr, second.stderr)
        self.assertEqual(first.returncode, second.returncode)

    def test_import_in_fresh_subprocess_has_no_side_effects(self):
        proc = subprocess.run(
            [sys.executable, "-c", "import claude_hello"],
            cwd=MODULE_DIR,
            env=dict(os.environ),
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.stdout, "")
        self.assertEqual(proc.stderr, "")
        self.assertEqual(proc.returncode, 0)

    def test_cli_absolute_paths_isolated_temp_cwd_no_user_site_no_pythonpath(self):
        interpreter = os.path.abspath(sys.executable)
        script = os.path.abspath(SCRIPT_PATH)
        env = {"PYTHONNOUSERSITE": "1"}
        if "PATH" in os.environ:
            env["PATH"] = os.environ["PATH"]
        with tempfile.TemporaryDirectory() as tmp_dir:
            self.assertNotIn(REPO_ROOT, tmp_dir)
            proc = subprocess.run(
                [interpreter, script],
                cwd=tmp_dir,
                env=env,
                capture_output=True,
                text=True,
            )
        _assert_matches_exact_output_contract(proc)


class TestClaudeHelloNegativeControl(unittest.TestCase):
    def test_altered_temporary_copy_is_rejected_by_the_contract(self):
        with open(SCRIPT_PATH, "r", encoding="utf-8") as source_file:
            original_source = source_file.read()

        mutated_source = original_source.replace(
            EXPECTED_GREETING, "Hello from Mutated Copy", 1
        )
        self.assertNotEqual(original_source, mutated_source)

        with tempfile.TemporaryDirectory() as tmp_dir:
            self.assertNotIn(REPO_ROOT, tmp_dir)
            mutated_path = os.path.join(tmp_dir, "claude_hello_mutated.py")
            with open(mutated_path, "w", encoding="utf-8") as mutated_file:
                mutated_file.write(mutated_source)

            proc = subprocess.run(
                [sys.executable, mutated_path],
                cwd=tmp_dir,
                env=dict(os.environ),
                capture_output=True,
                text=True,
            )

        with self.assertRaises(AssertionError):
            _assert_matches_exact_output_contract(proc)


if __name__ == "__main__":
    unittest.main()
