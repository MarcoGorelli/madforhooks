[![Build Status](https://github.com/MarcoGorelli/madforhooks/workflows/tox/badge.svg)](https://github.com/MarcoGorelli/madforhooks/actions?workflow=tox)
[![codecov](https://codecov.io/gh/MarcoGorelli/madforhooks/branch/main/graph/badge.svg?token=KrZeKo2xwD)](https://codecov.io/gh/MarcoGorelli/madforhooks)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/MarcoGorelli/madforhooks/main.svg)](https://results.pre-commit.ci/latest/github/MarcoGorelli/madforhooks/main)

# MadForHooks

Random assorted [pre-commit](https://github.com/pre-commit/pre-commit) hooks.

## Usage

Put this in the `repos` section of your `.pre-commit-config.yaml` file:

```yaml
-   repo: https://github.com/MarcoGorelli/madforhooks
    rev: 0.1.1
    hooks:
    -   id: conda-env-sorter
```

## Hooks available

### conda-env-sorter

Sort the dependencies in your conda environment file(s).
