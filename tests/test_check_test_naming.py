from typing import Any

import pytest

from madforhooks.check_test_naming import check_test_naming


@pytest.mark.parametrize(
    "src, expected_out, expected_ret",
    [
        (
            "def foo(): pass\n",
            "t.py:1:0 found test function which does not start with 'test'\n",
            1,
        ),
        (
            "class Foo:\n    def test_foo(): pass\n",
            "t.py:1:0 found test class which does not start with 'Test'\n",
            1,
        ),
        ("def test_foo(): pass\n", "", 0),
        (
            "class TestFoo:\n    def fob(): pass\n",
            "t.py:2:4 found test function which does not start with 'test'\n",
            1,
        ),
        ("class TestFoo:\n    def test_foo(): pass\n", "", 0),
        ("class TestFoo:\n    def foo(): pass\n", "", 0),
        (
            "class Foo:\n    def fob(): pass\n",
            "t.py:1:0 found test class which does not start with 'Test'\n"
            "t.py:2:4 found test function which does not start with 'test'\n",
            1,
        ),
        (
            "def foo():\n    pass\ndef test_foo():\n    foo()\n",
            "",
            0,
        ),
        (
            "class Foo:  # not a test\n"
            "    pass\n"
            "def test_foo():\n"
            "    Class.foo()\n",
            "",
            0,
        ),
        ("@pytest.fixture\ndef foo(): pass\n", "", 0),
        ("@pytest.fixture()\ndef foo(): pass\n", "", 0),
    ],
)
def test_main(capsys: Any, src: str, expected_out: str, expected_ret: int) -> None:
    ret = check_test_naming(src, "t.py")
    out, _ = capsys.readouterr()
    assert out == expected_out
    assert ret == expected_ret
