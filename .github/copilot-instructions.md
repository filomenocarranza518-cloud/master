# Project AI Instructions

## Mission

Maintain this repository as an AI-ready Python project framework with a working example application.

## Code Rules

- Use the `src/` layout for all production code.
- Keep the example app simple, but keep the framework reusable.
- Add or update tests for behavior changes.
- Update docs when workflow, architecture, or commands change.
- Prefer standard library solutions unless a dependency clearly improves the framework.

## Quality Gate

Before proposing completion, run:

```bash
python -m pytest
python -m ruff check .
python -m black --check .
python scripts/healthcheck.py
```

## Shared Context Files

Read these first when working on a larger task:

- `README.md`
- `docs/architecture.md`
- `docs/ai-stack.md`
- `docs/runbooks/ai-fallback.md`

## If a Tool Fails

1. Run `python scripts/context_snapshot.py`
2. Read `docs/runbooks/ai-fallback.md`
3. Continue with another available assistant or with the VS Code tasks
