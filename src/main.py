from __future__ import annotations

import sys
from pathlib import Path


def run() -> int:
    current_dir = Path(__file__).resolve().parent

    if str(current_dir) not in sys.path:
        sys.path.insert(0, str(current_dir))

    from sum_two_numbers.cli import main

    return main()


if __name__ == "__main__":
    raise SystemExit(run())
