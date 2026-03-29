from __future__ import annotations

import datetime as dt
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
STATUS_DIR = PROJECT_ROOT / "docs" / "status"
SNAPSHOT_FILE = STATUS_DIR / "current-session.md"


def git_executable() -> str:
    common_git_paths = [
        Path(r"C:\Program Files\Git\cmd\git.exe"),
        Path(r"C:\Program Files\Git\bin\git.exe"),
    ]

    for candidate in common_git_paths:
        if candidate.exists():
            return str(candidate)

    return "git"


def run_git(*args: str) -> str:
    try:
        completed = subprocess.run(
            [git_executable(), *args],
            check=True,
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return "Unavailable"
    return completed.stdout.strip() or "No output"


def top_level_tree() -> list[str]:
    entries = []
    for path in sorted(PROJECT_ROOT.iterdir(), key=lambda item: item.name.lower()):
        if path.name in {".git", "__pycache__"}:
            continue
        suffix = "/" if path.is_dir() else ""
        entries.append(f"- {path.name}{suffix}")
    return entries


def main() -> int:
    STATUS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    lines = [
        "# Workspace Context Snapshot",
        "",
        f"- Generated: {timestamp}",
        f"- Branch: {run_git('branch', '--show-current')}",
        "",
        "## Git Status",
        "",
        "```text",
        run_git("status", "--short", "--branch"),
        "```",
        "",
        "## Recent Commits",
        "",
        "```text",
        run_git("log", "--oneline", "-5"),
        "```",
        "",
        "## Top-Level Tree",
        "",
        *top_level_tree(),
        "",
        "## Recovery Hint",
        "",
        (
            "Read README.md, docs/architecture.md, docs/ai-stack.md, and "
            "docs/runbooks/ai-fallback.md before switching AI tools."
        ),
        "",
    ]
    SNAPSHOT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Snapshot written to {SNAPSHOT_FILE.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
