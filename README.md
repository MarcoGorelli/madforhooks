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
