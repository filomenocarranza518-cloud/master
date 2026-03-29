# Decisions

## ADR-001: Shared Markdown Is the Source of Operational Truth

All important workflow, architecture, and recovery knowledge must live in version-controlled Markdown files.

## ADR-002: AI Work Must Have a Backup Path

No task should depend on a single assistant or extension. Every workflow must remain executable through scripts, tasks, and docs.

## ADR-003: Quality Checks Must Be Automated

Formatting, linting, and tests are enforced through local tooling, `pre-commit`, and GitHub Actions rather than manual memory.

## ADR-004: The Framework Must Be Reusable

This repository is both a working project and the template for future projects. Improvements to the workflow should be reusable by default.
