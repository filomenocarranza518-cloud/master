# Bugfix Prompt

```text
Diagnose the bug, identify the root cause, and fix it in the smallest safe way.
Add or update a regression test in tests/.
Explain the failure mode and the fix.
Update docs only if behavior or workflow changed.
Run:
- python -m pytest
- python -m ruff check .
- python -m black --check .
```
