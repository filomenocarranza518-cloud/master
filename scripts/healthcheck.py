from __future__ import annotations

import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = [
    PROJECT_ROOT / "README.md",
    PROJECT_ROOT / "pyproject.toml",
    PROJECT_ROOT / "src",
    PROJECT_ROOT / "tests",
    PROJECT_ROOT / "docs",
    PROJECT_ROOT / ".github" / "workflows" / "ci.yml",
    PROJECT_ROOT / ".vscode" / "tasks.json",
]


def command_exists(command: str) -> bool:
    if shutil.which(command):
        return True

    if command == "git":
        common_git_paths = [
            Path(r"C:\Program Files\Git\cmd\git.exe"),
            Path(r"C:\Program Files\Git\bin\git.exe"),
        ]
        return any(path.exists() for path in common_git_paths)

    return False


def main() -> int:
    print("Health check")
    print(f"Python: {sys.version.split()[0]}")

    missing_commands = [
        command for command in ("git", "python") if not command_exists(command)
    ]
    if missing_commands:
        print(f"ERROR: Missing commands: {', '.join(missing_commands)}")
        return 1

    missing_paths = [path for path in REQUIRED_PATHS if not path.exists()]
    if missing_paths:
        print("ERROR: Missing required project files:")
        for path in missing_paths:
            print(f"- {path.relative_to(PROJECT_ROOT)}")
        return 1

    print("OK: Workspace structure is ready.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
