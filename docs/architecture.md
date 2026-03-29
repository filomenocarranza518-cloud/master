# Architecture

## Purpose

This repository serves two roles:

1. a small working Python CLI application
2. a reusable framework for future AI-assisted Python projects

## Layers

### Application layer

- `src/main.py`: simple runnable entry point
- `src/sum_two_numbers/cli.py`: example CLI behavior
- `tests/`: automated validation for the app behavior

### Workflow layer

- `.vscode/`: shared IDE tasks, settings, and extension recommendations
- `.github/workflows/ci.yml`: automated checks on GitHub
- `.github/copilot-instructions.md`: shared assistant guidance

### Knowledge layer

- `README.md`: top-level project contract
- `docs/`: architecture, usage, recovery, and changelog
- `prompts/`: reusable instructions for AI sessions

### Resilience layer

- `scripts/healthcheck.py`: validates the local setup
- `scripts/context_snapshot.py`: writes a Markdown summary of the current workspace
- `docs/runbooks/ai-fallback.md`: tool failure recovery process

## Design Rules

- Keep the codebase runnable without any AI tool.
- Keep all operational knowledge in version-controlled Markdown files.
- Use automation for checks that should not depend on memory.
- Prefer shared workspace settings over machine-specific configuration.
- When an assistant changes system behavior, update docs and prompts in the same change.
