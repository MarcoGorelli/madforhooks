from __future__ import annotations

import argparse
import ast
import sys
from typing import Sequence


class Visitor(ast.NodeVisitor):
    def __init__(self, file: str) -> None:
        self.file = file
        self.print_statements = False

    def visit_Call(self, node: ast.Call) -> None:
        if (
            isinstance(node.func, ast.Name)
            and node.func.id == "print"
            and "file" not in {keyword.arg for keyword in node.keywords}
        ):
            self.print_statements = True
            sys.stdout.write(
                f"{self.file}:{node.lineno}:{node.col_offset} "
                "found print statement\n"
            )
        self.generic_visit(node)


def no_print_statements(content: str, file: str) -> int:
    tree = ast.parse(content)
    visitor = Visitor(file)
    visitor.visit(tree)
    if visitor.print_statements:
        return 1
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    args = parser.parse_args(argv)
    retv = 0
    for file in args.files:
        with open(file, "rb") as fd:
            content_bytes = fd.read()
        content = content_bytes.decode()
        retv = retv or no_print_statements(content, file)

    return retv


if __name__ == "__main__":
    exit(main())
