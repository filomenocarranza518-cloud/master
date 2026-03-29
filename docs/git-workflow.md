# Git Workflow

## Branch Strategy

- `main` is the protected integration branch
- use `feature/<name>` for new work
- use `fix/<name>` for bug fixes
- use `docs/<name>` for documentation-only work

## Pull Request Rules

- open a pull request into `main`
- ensure CI is green
- keep changes small and reviewable
- update docs when workflow or behavior changes

## Ownership

- `CODEOWNERS` defines the default reviewer ownership
- workflow changes should include doc updates in the same pull request

## Local Safety Net

- install hooks with `python -m pre_commit install --hook-type pre-commit --hook-type pre-push`
- `pre-commit` creates a context snapshot before commit
- `pre-push` runs tests before the push leaves the machine
