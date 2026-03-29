# AI-Ready Python Project Framework

This repository is now a reusable Python project framework for working with AI-assisted development in a reliable, low-friction way.

## Core Flow

```text
ChatGPT -> designs and plans
Codex -> implements and refactors
VS Code -> edits, runs, and debugs
GitHub -> versions, reviews, and automates
Markdown -> documents and preserves context
```

## What This Framework Adds

- `src/` source layout with a working example CLI app
- `tests/` ready for `pytest`
- `docs/` for architecture, runbooks, and changelog
- `.github/` for CI, pull request templates, and AI instructions
- `.vscode/` for shared tasks, settings, and extension recommendations
- `.devcontainer/` for a reproducible container workspace
- `.pre-commit-config.yaml` for automatic local checks and snapshots
- `prompts/` for reusable AI prompts
- `scripts/` for bootstrapping, health checks, context snapshots, and scaffolding

## Project Structure

```text
.
|-- .github/
|   |-- ISSUE_TEMPLATE/
|   |-- workflows/
|   |-- CODEOWNERS
|   |-- copilot-instructions.md
|   `-- PULL_REQUEST_TEMPLATE.md
|-- .devcontainer/
|   `-- devcontainer.json
|-- .vscode/
|   |-- extensions.json
|   |-- settings.json
|   `-- tasks.json
|-- docs/
|   |-- ai-stack.md
|   |-- architecture.md
|   |-- changelog.md
|   |-- decisions.md
|   |-- git-workflow.md
|   |-- roadmap.md
|   |-- README.md
|   |-- usage.md
|   `-- runbooks/
|       `-- ai-fallback.md
|-- prompts/
|   |-- bugfix.md
|   |-- documentation.md
|   |-- feature-implementation.md
|   `-- recovery.md
|-- scripts/
|   |-- bootstrap.py
|   |-- context_snapshot.py
|   |-- healthcheck.py
|   `-- scaffold_project.py
|-- src/
|   |-- main.py
|   `-- sum_two_numbers/
|-- tests/
|   |-- conftest.py
|   `-- test_sum_two_numbers.py
|-- .editorconfig
|-- .gitignore
|-- .pre-commit-config.yaml
|-- CONTRIBUTING.md
|-- pyproject.toml
|-- README.md
|-- requirements-dev.txt
|-- requirements.txt
`-- sum_two_numbers.py
```

## Quick Start

1. Create and activate your environment.
2. Install the development dependencies.
3. Run the example app or the quality checks.

```bash
python scripts/bootstrap.py
python src/main.py 3 4
python -m pytest
python -m ruff check .
python -m black --check .
```

## Shared Workflow

### Design

Use ChatGPT to shape the idea, clarify scope, and decide tradeoffs.

Example prompt:

```text
Design a Python CLI tool for validating CSV files. Include architecture, tests, and docs.
```

### Build

Use Codex to implement the work directly in this structure.

Example prompt:

```text
Implement the CSV validator in src/main.py, add tests, and update the docs.
```

### Edit and Run

Use VS Code tasks to run tests, lint, format, generate context snapshots, and perform health checks.
If your local machine is unstable, the dev container reproduces the same environment and extensions.

### Version and Automate

Use GitHub for version history, pull requests, and CI via GitHub Actions.

### Document

Use Markdown to preserve architecture decisions, prompts, recovery steps, and user-facing docs.

## AI Resilience Layer

This framework includes a fallback strategy so work can continue even if one assistant or extension fails.

- Primary AI path: Codex in VS Code
- Secondary AI path: GitHub Copilot Chat in VS Code
- Shared context layer: `docs/`, `prompts/`, `.github/copilot-instructions.md`
- Recovery utilities: `python scripts/healthcheck.py` and `python scripts/context_snapshot.py`
- Automatic commit protection: `pre-commit` refreshes context and enforces local checks
- Manual fallback path: run tasks from `.vscode/tasks.json` without any AI dependency

Read [docs/ai-stack.md](docs/ai-stack.md) and [docs/runbooks/ai-fallback.md](docs/runbooks/ai-fallback.md) for the operational details.

## Reusing This Framework

You can use this repository as a template, or generate a new starter project with:

```bash
python scripts/scaffold_project.py --name my-project --path ..\my-project
```

## Documentation Index

- [docs/README.md](docs/README.md)
- [docs/architecture.md](docs/architecture.md)
- [docs/usage.md](docs/usage.md)
- [docs/ai-stack.md](docs/ai-stack.md)
- [docs/decisions.md](docs/decisions.md)
- [docs/roadmap.md](docs/roadmap.md)
- [docs/git-workflow.md](docs/git-workflow.md)
- [docs/runbooks/ai-fallback.md](docs/runbooks/ai-fallback.md)
- [docs/changelog.md](docs/changelog.md)
