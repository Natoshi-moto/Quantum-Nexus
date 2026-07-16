import os
import subprocess
import sys
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMPL_PATH = os.path.join(
    REPO_ROOT, "experiments", "provider_handshake", "claude_hello.py"
)

EXPECTED_STDOUT = b"Hello from Claude Code\n"
EXPECTED_GREETING = "Hello from Claude Code"


def assert_exact_contract(stdout, stderr, returncode):
    if stdout != EXPECTED_STDOUT:
        raise AssertionError(f"stdout mismatch: {stdout!r}")
    if stderr != b"":
        raise AssertionError(f"stderr mismatch: {stderr!r}")
    if returncode != 0:
        raise AssertionError(f"exit status mismatch: {returncode!r}")


class TestClaudeHelloImport(unittest.TestCase):
    def test_hello_callable_returns_exact_greeting(self):
        sys.path.insert(0, os.path.dirname(IMPL_PATH))
        try:
            import claude_hello

            result = claude_hello.hello()
        finally:
            sys.path.pop(0)
        self.assertIsInstance(result, str)
        self.assertEqual(result, EXPECTED_GREETING)
        self.assertEqual(len(result), 22)

    def test_hello_callable_requires_no_arguments(self):
        sys.path.insert(0, os.path.dirname(IMPL_PATH))
        try:
            import claude_hello

            first = claude_hello.hello()
            second = claude_hello.hello()
        finally:
            sys.path.pop(0)
        self.assertEqual(first, second)

    def test_import_in_fresh_subprocess_has_no_side_effects(self):
        result = subprocess.run(
            [sys.executable, "-c", f"import sys; sys.path.insert(0, {os.path.dirname(IMPL_PATH)!r}); import claude_hello"],
            capture_output=True,
        )
        self.assertEqual(result.stdout, b"")
        self.assertEqual(result.stderr, b"")
        self.assertEqual(result.returncode, 0)


class TestClaudeHelloCLI(unittest.TestCase):
    def test_cli_exact_output_contract(self):
        result = subprocess.run(
            [sys.executable, IMPL_PATH],
            capture_output=True,
        )
        assert_exact_contract(result.stdout, result.stderr, result.returncode)

    def test_cli_two_independent_executions_are_byte_identical(self):
        first = subprocess.run([sys.executable, IMPL_PATH], capture_output=True)
        second = subprocess.run([sys.executable, IMPL_PATH], capture_output=True)
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual(first.stderr, second.stderr)
        self.assertEqual(first.returncode, second.returncode)
        assert_exact_contract(first.stdout, first.stderr, first.returncode)
        assert_exact_contract(second.stdout, second.stderr, second.returncode)

    def test_cli_unexpected_argument_is_rejected_deterministically(self):
        result = subprocess.run(
            [sys.executable, IMPL_PATH, "unexpected"],
            capture_output=True,
        )
        self.assertEqual(result.stdout, b"")
        self.assertEqual(result.stderr, b"error: unexpected argument\n")
        self.assertEqual(result.returncode, 2)

    def test_cli_isolated_environment_absolute_paths(self):
        abs_interpreter = os.path.abspath(sys.executable)
        abs_script = os.path.abspath(IMPL_PATH)
        self.assertTrue(os.path.isabs(abs_interpreter))
        self.assertTrue(os.path.isabs(abs_script))
        with tempfile.TemporaryDirectory() as unrelated_cwd:
            isolated_env = {
                "PATH": os.environ.get("PATH", ""),
                "PYTHONNOUSERSITE": "1",
            }
            result = subprocess.run(
                [abs_interpreter, abs_script],
                capture_output=True,
                cwd=unrelated_cwd,
                env=isolated_env,
            )
        assert_exact_contract(result.stdout, result.stderr, result.returncode)


class TestClaudeHelloNegativeControl(unittest.TestCase):
    def test_mutated_temporary_copy_is_rejected(self):
        with open(IMPL_PATH, "r", encoding="utf-8") as source:
            original_source = source.read()

        mutated_source = original_source.replace(
            "Hello from Claude Code", "Hello from Mutated Code"
        )
        self.assertNotEqual(mutated_source, original_source)

        with tempfile.TemporaryDirectory() as mutation_dir:
            mutated_path = os.path.join(mutation_dir, "mutated_claude_hello.py")
            with open(mutated_path, "w", encoding="utf-8") as mutated_file:
                mutated_file.write(mutated_source)

            result = subprocess.run(
                [sys.executable, mutated_path],
                capture_output=True,
            )

            with self.assertRaises(AssertionError):
                assert_exact_contract(result.stdout, result.stderr, result.returncode)


if __name__ == "__main__":
    unittest.main()
