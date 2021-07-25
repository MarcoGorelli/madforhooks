"""Test conda-env-sorter."""

from pathlib import Path

from _pytest.capture import capsys
from _pytest.tmpdir import tmpdir

from madforhooks.no_print_statements import main, no_print_statements

ROOT = Path(__file__).parent.parent.parent


def test_main(capsys: capsys) -> None:
    src = "print(foo)"
    no_print_statements(src, "t.py")
    out, err = capsys.readouterr()
    assert out == "t.py:1:0 found print statement\n"


def test_main_noop(capsys: capsys) -> None:
    src = ""
    no_print_statements(src, "t.py")
    out, err = capsys.readouterr()
    assert out == ""


def test_main_print_with_file(capsys: capsys) -> None:
    src = "print(foo, file=bar)"
    no_print_statements(src, "t.py")
    out, err = capsys.readouterr()
    assert out == ""


def test_e2e(tmpdir: tmpdir, capsys: capsys) -> None:
    with open(tmpdir / "t.py", "w") as fd:
        fd.write("print(foo)\n")
    main((str(tmpdir / "t.py"),))
    out, err = capsys.readouterr()
    assert "t.py:1:0 found print statement\n" in out
