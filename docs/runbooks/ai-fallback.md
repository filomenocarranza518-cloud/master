# AI Fallback Runbook

## When to Use This

Use this runbook when one of the following happens:

- an AI extension stops responding
- authentication fails
- a rate limit blocks work
- the current assistant loses context
- an external AI service is unavailable

## Recovery Steps

1. Run a local health check:

```bash
python scripts/healthcheck.py
```

2. Generate a fresh Markdown context snapshot:

```bash
python scripts/context_snapshot.py
```

3. Read the current project memory:

- `README.md`
- `docs/architecture.md`
- `docs/ai-stack.md`
- `.github/copilot-instructions.md`

4. Continue with the next available path:

- Codex in VS Code
- GitHub Copilot Chat
- VS Code dev container
- direct terminal commands and VS Code tasks

5. If Git is available, rely on the local hooks:

- `pre-commit` refreshes the context snapshot before commit
- `pre-push` runs tests before the push leaves the machine

## Important Rule

Do not keep critical context only inside a chat window. If a decision matters, write it into `docs/` or `prompts/`.
