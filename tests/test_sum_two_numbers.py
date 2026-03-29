import pytest

from sum_two_numbers.cli import add_numbers, main


def test_add_numbers_returns_total() -> None:
    assert add_numbers(3.0, 4.0) == 7.0


def test_main_prints_sum(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["10", "5"])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.strip() == "The sum is: 15.0"


def test_main_requires_two_arguments() -> None:
    with pytest.raises(SystemExit) as error:
        main([])

    assert error.value.code == 2
