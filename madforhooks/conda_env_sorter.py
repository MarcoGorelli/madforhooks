"""Sort dependencies in conda environment files."""

import argparse
from pathlib import Path
from typing import Optional, Sequence

import ruamel.yaml

yaml = ruamel.yaml.YAML()


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Sort dependencies in conda environment files."""
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    args = parser.parse_args(argv)
    for path in args.paths:
        doc = yaml.load(path)
        last_one = doc["dependencies"][-1]
        if isinstance(last_one, ruamel.yaml.comments.CommentedMap):
            doc["dependencies"].pop(-1)
        doc["dependencies"].sort()
        doc["dependencies"].append(last_one)

        yaml.dump(doc, path)


if __name__ == "__main__":
    main()
