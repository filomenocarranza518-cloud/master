from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

FRAMEWORK_FILES = {
    ".editorconfig": """root = true

[*.py]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 4

[*.md]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = false

[*.{json,toml,yml,yaml}]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 2
""",
    ".gitignore": """__pycache__/
*.py[cod]
*.egg-info/
.pytest_cache/
.ruff_cache/
.mypy_cache/
.coverage
.coverage.*
.env
dist/
build/
.venv/
venv/
.idea/
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/extensions.json
docs/status/
""",
    ".pre-commit-config.yaml": """repos:
  - repo: local
    hooks:
      - id: context-snapshot
        name: Context Snapshot
        entry: python scripts/context_snapshot.py
        language: system
        pass_filenames: false
        stages: [pre-commit]
      - id: ruff
        name: Ruff
        entry: python -m ruff check .
        language: system
        pass_filenames: false
        stages: [pre-commit]
      - id: black-check
        name: Black Check
        entry: python -m black --check .
        language: system
        pass_filenames: false
        stages: [pre-commit]
      - id: pytest
        name: Pytest
        entry: python -m pytest
        language: system
        pass_filenames: false
        stages: [pre-push]
""",
    ".devcontainer/devcontainer.json": """{
  "name": "__TITLE__",
  "image": "mcr.microsoft.com/devcontainers/python:1-3.12-bullseye",
  "customizations": {
    "vscode": {
      "extensions": [
        "openai.chatgpt",
        "GitHub.copilot",
        "GitHub.copilot-chat",
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.black-formatter",
        "charliermarsh.ruff",
        "DavidAnson.vscode-markdownlint"
      ]
    }
  },
  "postCreateCommand": "python scripts/bootstrap.py"
}
""",
    ".github/CODEOWNERS": "* __OWNER__\n",
    ".github/PULL_REQUEST_TEMPLATE.md": """## Summary

Describe the main change in one short paragraph.

## Checklist

- [ ] Tests were added or updated
- [ ] Docs were updated if behavior changed
- [ ] `python -m pytest` passes
- [ ] `python -m ruff check .` passes
- [ ] `python -m black --check .` passes
- [ ] Recovery and AI workflow docs were reviewed if the operating model changed
""",
    ".github/ISSUE_TEMPLATE/bug_report.md": """---
name: Bug report
about: Report a defect in code, tooling, workflow, or AI setup
title: "[bug] "
labels: bug
assignees: ""
---

## Problem

What happened?

## Steps to reproduce

1.
2.
3.

## Expected behavior

What should have happened?

## Context

- OS:
- Python version:
- VS Code version:
- AI tool in use:
""",
    ".github/ISSUE_TEMPLATE/feature_request.md": """---
name: Feature request
about: Propose a product, workflow, or framework improvement
title: "[feature] "
labels: enhancement
assignees: ""
---

## Goal

What are we trying to improve?

## Proposed change

Describe the feature or workflow improvement.
""",
    ".github/copilot-instructions.md": """# Project AI Instructions

## Mission

Maintain this repository as an AI-ready Python project
with strong docs, recovery paths, and automation.

## Code Rules

- Keep production code in `src/`
- Add or update tests for behavior changes
- Update docs when workflow or architecture changes
- Prefer simple, maintainable solutions

## Quality Gate

Before proposing completion, run:

```bash
python -m pytest
python -m ruff check .
python -m black --check .
python scripts/healthcheck.py
```
""",
    ".github/workflows/ci.yml": """name: CI

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

jobs:
  quality:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install -r requirements-dev.txt

      - name: Run tests
        run: python -m pytest

      - name: Run Ruff
        run: python -m ruff check .

      - name: Run Black
        run: python -m black --check .
""",
    ".vscode/extensions.json": """{
  "recommendations": [
    "openai.chatgpt",
    "GitHub.copilot",
    "GitHub.copilot-chat",
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-python.black-formatter",
    "charliermarsh.ruff",
    "DavidAnson.vscode-markdownlint"
  ]
}
""",
    ".vscode/settings.json": """{
  "editor.formatOnSave": true,
  "markdown.validate.enabled": true,
  "python.defaultInterpreterPath": "python",
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": [
    "tests"
  ],
  "python.testing.unittestEnabled": false,
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports": "explicit"
    }
  }
}
""",
    ".vscode/tasks.json": """{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Setup: Bootstrap Workspace",
      "type": "shell",
      "command": "python scripts/bootstrap.py",
      "problemMatcher": []
    },
    {
      "label": "Setup: Install Git Hooks",
      "type": "shell",
      "command": "python scripts/bootstrap.py",
      "problemMatcher": []
    },
    {
      "label": "Run: App",
      "type": "shell",
      "command": "python src/main.py",
      "problemMatcher": []
    },
    {
      "label": "Test: Pytest",
      "type": "shell",
      "command": "python -m pytest",
      "group": "test",
      "problemMatcher": []
    },
    {
      "label": "Lint: Ruff",
      "type": "shell",
      "command": "python -m ruff check .",
      "problemMatcher": []
    },
    {
      "label": "Format: Black",
      "type": "shell",
      "command": "python -m black .",
      "problemMatcher": []
    },
    {
      "label": "Health: Workspace Check",
      "type": "shell",
      "command": "python scripts/healthcheck.py",
      "problemMatcher": []
    },
    {
      "label": "Context: Snapshot Workspace",
      "type": "shell",
      "command": "python scripts/context_snapshot.py",
      "problemMatcher": []
    }
  ]
}
""",
    "README.md": """# __TITLE__

This project was generated from the AI-ready Python project framework.

## Core Flow

```text
ChatGPT -> designs and plans
Codex -> implements and refactors
VS Code -> edits, runs, and debugs
GitHub -> versions, reviews, and automates
Markdown -> documents and preserves context
```

## Quick Start

```bash
python scripts/bootstrap.py
python src/main.py
python -m pytest
```
""",
    "CONTRIBUTING.md": """# Contributing

## Local Setup

```bash
python scripts/bootstrap.py
```

## Branch Naming

- `feature/<name>`
- `fix/<name>`
- `docs/<name>`
""",
    "requirements.txt": "# Add runtime dependencies here.\n",
    "requirements-dev.txt": """black>=24.8.0
pre-commit>=4.0.0
pytest>=8.3.0
ruff>=0.6.9
""",
    "pyproject.toml": """[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]

[tool.black]
line-length = 88
target-version = ["py310"]

[tool.ruff]
line-length = 88
target-version = "py310"
src = ["src", "tests", "scripts"]

[tool.ruff.lint]
select = ["B", "E", "F", "I", "UP"]
""",
    "docs/README.md": """# Documentation Index

- `usage.md`
- `architecture.md`
- `ai-stack.md`
- `decisions.md`
- `roadmap.md`
- `git-workflow.md`
- `runbooks/ai-fallback.md`
""",
    "docs/usage.md": """# Usage

```bash
python scripts/bootstrap.py
python src/main.py
python -m pytest
python -m ruff check .
python -m black --check .
```
""",
    "docs/architecture.md": """# Architecture

## Purpose

This project follows the AI-ready Python framework.

## Layers

- application layer in `src/`
- workflow layer in `.vscode/` and `.github/`
- knowledge layer in `docs/` and `prompts/`
- resilience layer in `scripts/`
""",
    "docs/ai-stack.md": """# AI Stack

- primary assistant: Codex
- fallback assistant: GitHub Copilot Chat
- manual fallback: VS Code tasks, scripts, and docs
""",
    "docs/decisions.md": """# Decisions

## ADR-001

Shared Markdown is the source of operational truth.
""",
    "docs/roadmap.md": """# Roadmap

- add the first feature
- harden CI
- document production deployment
""",
    "docs/git-workflow.md": """# Git Workflow

- work in feature branches
- merge through pull requests
- keep CI green before merge
""",
    "docs/runbooks/ai-fallback.md": """# AI Fallback Runbook

1. Run `python scripts/healthcheck.py`
2. Run `python scripts/context_snapshot.py`
3. Read `docs/` and `.github/copilot-instructions.md`
4. Continue with another assistant or direct tasks
""",
    "prompts/feature-implementation.md": """# Feature Prompt

```text
Implement the requested feature in src/.
Add tests and update docs.
Run pytest, ruff, and black checks.
```
""",
    "prompts/bugfix.md": """# Bugfix Prompt

```text
Fix the bug, add a regression test, and explain the root cause.
```
""",
    "prompts/documentation.md": """# Documentation Prompt

```text
Update README.md and docs/ to match the current code and workflow.
```
""",
    "prompts/recovery.md": """# Recovery Prompt

```text
Read the docs and latest snapshot, then continue the task with minimal assumptions.
```
""",
    "scripts/bootstrap.py": """from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def build_env() -> dict[str, str]:
    env = dict(os.environ)
    common_git_paths = [
        Path(r"C:\\Program Files\\Git\\cmd"),
        Path(r"C:\\Program Files\\Git\\bin"),
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
""",
    "scripts/healthcheck.py": """from __future__ import annotations

import shutil
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def command_exists(command: str) -> bool:
    if shutil.which(command):
        return True

    if command == "git":
        common_git_paths = [
            Path(r"C:\\Program Files\\Git\\cmd\\git.exe"),
            Path(r"C:\\Program Files\\Git\\bin\\git.exe"),
        ]
        return any(path.exists() for path in common_git_paths)

    return False


def main() -> int:
    required = [
        PROJECT_ROOT / "README.md",
        PROJECT_ROOT / "src",
        PROJECT_ROOT / "tests",
        PROJECT_ROOT / "docs",
        PROJECT_ROOT / ".vscode" / "tasks.json",
        PROJECT_ROOT / ".github" / "workflows" / "ci.yml",
        PROJECT_ROOT / ".pre-commit-config.yaml",
    ]
    missing = [path for path in required if not path.exists()]
    if missing:
        print("Missing required files:")
        for path in missing:
            print(path)
        return 1

    missing_commands = [name for name in ("python", "git") if not command_exists(name)]
    if missing_commands:
        print(f"Missing commands: {', '.join(missing_commands)}")
        return 1

    print("Workspace structure is ready.")
    print(f"Python: {sys.version.split()[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
""",
    "scripts/context_snapshot.py": """from __future__ import annotations

import datetime as dt
import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
STATUS_DIR = PROJECT_ROOT / "docs" / "status"
SNAPSHOT_FILE = STATUS_DIR / "current-session.md"


def git_executable() -> str:
    common_git_paths = [
        Path(r"C:\\Program Files\\Git\\cmd\\git.exe"),
        Path(r"C:\\Program Files\\Git\\bin\\git.exe"),
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


def main() -> int:
    STATUS_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Workspace Context Snapshot",
        "",
        f"- Generated: {dt.datetime.now().astimezone().isoformat(timespec='seconds')}",
        f"- Branch: {run_git('branch', '--show-current')}",
        "",
        "## Git Status",
        "",
        "```text",
        run_git("status", "--short", "--branch"),
        "```",
        "",
    ]
    SNAPSHOT_FILE.write_text("\\n".join(lines), encoding="utf-8")
    print(f"Snapshot written to {SNAPSHOT_FILE.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
""",
    "src/main.py": """def main() -> int:
    print("Hello from __SLUG__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
""",
    "tests/conftest.py": """import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
""",
    "tests/test_smoke.py": """from main import main


def test_main_returns_zero() -> None:
    assert main() == 0
""",
}


def slugify(name: str) -> str:
    normalized = re.sub(r"[^a-zA-Z0-9]+", "-", name).strip("-").lower()
    return normalized or "python-project"


def render(template: str, *, owner: str, slug: str, title: str) -> str:
    return (
        template.replace("__OWNER__", owner)
        .replace("__SLUG__", slug)
        .replace("__TITLE__", title)
    )


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def try_format(target: Path) -> None:
    commands = [
        [sys.executable, "-m", "ruff", "check", ".", "--fix"],
        [sys.executable, "-m", "black", "."],
    ]

    for command in commands:
        try:
            subprocess.run(
                command, check=True, capture_output=True, text=True, cwd=target
            )
        except (FileNotFoundError, subprocess.CalledProcessError):
            return


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a new AI-ready starter project."
    )
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument("--path", required=True, help="Target directory")
    parser.add_argument(
        "--owner",
        default="@filomenocarranza518-cloud",
        help="Default CODEOWNERS entry",
    )
    args = parser.parse_args()

    slug = slugify(args.name)
    target = Path(args.path).resolve()
    target.mkdir(parents=True, exist_ok=True)

    for relative_path, template in FRAMEWORK_FILES.items():
        write_file(
            target / relative_path,
            render(template, owner=args.owner, slug=slug, title=args.name),
        )

    try_format(target)

    print(f"AI-ready project scaffold created at {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
