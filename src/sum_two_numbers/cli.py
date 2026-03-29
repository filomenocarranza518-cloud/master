from __future__ import annotations

import argparse


def add_numbers(first: float, second: float) -> float:
    return first + second


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Add two numbers and print the result."
    )
    parser.add_argument("first", type=float, help="The first number.")
    parser.add_argument("second", type=float, help="The second number.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    total = add_numbers(args.first, args.second)
    print(f"The sum is: {total}")
    return 0
