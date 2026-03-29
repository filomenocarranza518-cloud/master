# Feature Implementation Prompt

Use this prompt with any coding assistant:

```text
Implement the requested feature inside the existing src/ layout.
Add or update tests in tests/.
Update README.md and docs/ if behavior or workflow changes.
Run or describe the expected commands:
- python -m pytest
- python -m ruff check .
- python -m black --check .
Keep changes small, reviewable, and production-minded.
```
