import io
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from sum_two_numbers.cli import add_numbers, main


class SumTwoNumbersTests(unittest.TestCase):
    def test_add_numbers_returns_total(self) -> None:
        self.assertEqual(add_numbers(3.0, 4.0), 7.0)

    def test_main_prints_sum(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            exit_code = main(["10", "5"])

        self.assertEqual(exit_code, 0)
        self.assertEqual(output.getvalue().strip(), "The sum is: 15.0")

    def test_main_requires_two_arguments(self) -> None:
        error_output = io.StringIO()

        with redirect_stderr(error_output):
            with self.assertRaises(SystemExit) as error:
                main([])

        self.assertEqual(error.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
