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
        dicts = []
        others = []

        for x in doc["dependencies"]:
            if isinstance(x, dict):
                dicts.append(x)
            else:
                others.append(x)
        others.sort(key=lambda x: str(x))
        for d in dicts:
            for v in d.values():
                if isinstance(v, list):
                    v.sort(key=lambda x: str(x))
        dicts.sort(key=lambda x: str(x))
        doc["dependencies"].clear()
        doc["dependencies"].extend(others)
        doc["dependencies"].extend(dicts)

        yaml.dump(doc, path)


if __name__ == "__main__":
    main()
