# Contributing

## Local Setup

```bash
python scripts/bootstrap.py
```

## Before Opening a Pull Request

Run the full local quality gate:

```bash
python -m pytest
python -m ruff check .
python -m black --check .
python scripts/healthcheck.py
```

## Branch Naming

- `feature/<name>` for new work
- `fix/<name>` for bug fixes
- `docs/<name>` for documentation-only work

## Pull Request Policy

- target `main`
- keep each change focused
- update docs alongside workflow or behavior changes

## Documentation Rule

If behavior or workflow changes, update the relevant files in `docs/`, `README.md`, and the affected prompts or runbooks.

## AI Collaboration Rule

When using an AI assistant, keep the shared context up to date:

- refresh `docs/architecture.md` if the system shape changes
- refresh `.github/copilot-instructions.md` if coding conventions change
- run `python scripts/context_snapshot.py` before switching tools during an incident
