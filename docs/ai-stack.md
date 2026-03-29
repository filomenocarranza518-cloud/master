# AI Stack for VS Code

## Goal

Provide an AI-assisted workflow with backup paths so development can continue when a single extension, service, or login flow fails.

## Recommended Layers

### Primary coding agent

- OpenAI Codex in VS Code

### Secondary coding assistant

- GitHub Copilot Chat in VS Code

### Core editor support

- Python
- Pylance
- Black Formatter
- Ruff
- Markdown linting

### Shared memory

- `docs/`
- `prompts/`
- `.github/copilot-instructions.md`
- `docs/status/current-session.md`

## Recovery Principle

No single AI tool should be the only place where architecture, commands, or workflow knowledge exists.

If one assistant fails:

1. use the shared docs and prompts
2. run the VS Code tasks directly
3. generate a context snapshot
4. switch into the dev container if the host setup is unstable
5. continue with a secondary assistant

## Extension Recommendations

These are defined in `.vscode/extensions.json` so the workspace can prompt for the same editor stack each time it is opened.

## Operational Commands

```bash
python scripts/healthcheck.py
python scripts/context_snapshot.py
python -m pytest
python -m ruff check .
python -m black --check .
```
