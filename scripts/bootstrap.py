from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def build_env() -> dict[str, str]:
    env = dict(os.environ)
    common_git_paths = [
        Path(r"C:\Program Files\Git\cmd"),
        Path(r"C:\Program Files\Git\bin"),
    ]
    additions = [str(path) for path in common_git_paths if path.exists()]
    if additions:
        env["PATH"] = ";".join(additions + [env.get("PATH", "")])
    return env


def run(command: list[str]) -> None:
    subprocess.run(command, check=True, cwd=PROJECT_ROOT, env=build_env())


def main() -> int:
    run([sys.executable, "-m", "pip", "install", "-r", "requirements-dev.txt"])
    run(
        [
            sys.executable,
            "-m",
            "pre_commit",
            "install",
            "--hook-type",
            "pre-commit",
            "--hook-type",
            "pre-push",
        ]
    )
    print("Workspace bootstrapped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
