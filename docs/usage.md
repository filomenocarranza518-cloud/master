# Usage

## Install Dependencies

```bash
python scripts/bootstrap.py
```

## Run the Example App

```bash
python src/main.py 3 4
python sum_two_numbers.py 3 4
```

## Run Tests

```bash
python -m pytest
```

## Run Quality Checks

```bash
python -m ruff check .
python -m black --check .
python scripts/healthcheck.py
```

## Install Git Hooks

```bash
python -m pre_commit install --hook-type pre-commit --hook-type pre-push
```

## Open in a Dev Container

This repository includes `.devcontainer/devcontainer.json` so VS Code can recreate the environment with the recommended extensions and setup commands.

## Fix Formatting

```bash
python -m black .
```

## Generate a Context Snapshot

```bash
python scripts/context_snapshot.py
```

## Create a New Project from This Framework

```bash
python scripts/scaffold_project.py --name my-project --path ..\my-project
```
