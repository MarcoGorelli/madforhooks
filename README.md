[![Build Status](https://github.com/MarcoGorelli/madforhooks/workflows/tox/badge.svg)](https://github.com/MarcoGorelli/madforhooks/actions?workflow=tox)
[![codecov](https://codecov.io/gh/MarcoGorelli/madforhooks/branch/main/graph/badge.svg?token=KrZeKo2xwD)](https://codecov.io/gh/MarcoGorelli/madforhooks)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/MarcoGorelli/madforhooks/main.svg)](https://results.pre-commit.ci/latest/github/MarcoGorelli/madforhooks/main)

# MadForHooks

Random assorted [pre-commit](https://github.com/pre-commit/pre-commit) hooks.

## Usage

Put this in the `repos` section of your `.pre-commit-config.yaml` file:

```yaml
-   repo: https://github.com/MarcoGorelli/madforhooks
    rev: 0.4.1
    hooks:
    -   id: conda-env-sorter
    -   id: no-print-statements
    -   id: check-execution-order
    -   id: check-test-naming
```

Or, from the commandline:

```console
pip install madforhooks
python -m madforhooks.check_execution_order file1.ipynb file2.ipynb file3.ipynb
```

Example of how to run ``check-test-naming`` on your test directory:
```console
git ls-files | xargs python -m madforhooks.check_test_naming
```

## Hooks available

### conda-env-sorter

Sort the dependencies in your conda environment file(s).

### no-print-statements

Raise if print statements are found (unless they have `file=`).

### check-execution-order

Raise if notebook cells were executed out-of-order. Use `--strict` to ensure
strict monotonicity.

### check-test-naming

Check that test names start with `test`. This is useful for finding
tests which are meant to be running in CI, but which don't because they
are misnamed.

If there are any false positives, you prevent this tool from flagging them
by adding a `# not a test` comment one the line where the function/class is
defined.
