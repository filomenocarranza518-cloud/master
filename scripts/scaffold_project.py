from __future__ import annotations

import argparse
import re
from pathlib import Path

README_TEMPLATE = """# {title}

This project was generated from the AI-ready Python project framework.

## Quick Start

```bash
python -m pip install -r requirements-dev.txt
python src/main.py
python -m pytest
```
"""

MAIN_TEMPLATE = """def main() -> int:
    print("Hello from {slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
"""

TEST_TEMPLATE = """from src.main import main


def test_main_returns_zero() -> None:
    assert main() == 0
"""

DOC_TEMPLATE = """# Project Docs

- Add architecture notes here.
- Add workflows and commands here.
- Add runbooks for failure recovery here.
"""

GITIGNORE_TEMPLATE = """__pycache__/
*.py[cod]
.pytest_cache/
.ruff_cache/
.env
.venv/
venv/
dist/
build/
"""

REQ_DEV_TEMPLATE = """pytest>=8.3.0
ruff>=0.6.9
black>=24.8.0
"""


def slugify(name: str) -> str:
    normalized = re.sub(r"[^a-zA-Z0-9]+", "-", name).strip("-").lower()
    return normalized or "python-project"


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a new starter project.")
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument("--path", required=True, help="Target directory")
    args = parser.parse_args()

    slug = slugify(args.name)
    target = Path(args.path).resolve()
    target.mkdir(parents=True, exist_ok=True)

    write_file(target / "README.md", README_TEMPLATE.format(title=args.name))
    write_file(target / "requirements.txt", "# Add runtime dependencies here.\n")
    write_file(target / "requirements-dev.txt", REQ_DEV_TEMPLATE)
    write_file(target / ".gitignore", GITIGNORE_TEMPLATE)
    write_file(target / "src" / "main.py", MAIN_TEMPLATE.format(slug=slug))
    write_file(target / "tests" / "test_smoke.py", TEST_TEMPLATE)
    write_file(target / "docs" / "README.md", DOC_TEMPLATE)

    print(f"Project scaffold created at {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
