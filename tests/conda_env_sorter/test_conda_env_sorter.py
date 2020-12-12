"""Test conda-env-sorter."""

import shutil
from pathlib import Path
from typing import TYPE_CHECKING

from madforhooks.conda_env_sorter import main

ROOT = Path(__file__).parent.parent.parent

TESTFILE = Path("tests") / "conda_env_sorter/data/environment-dev-py38.yml"

if TYPE_CHECKING:
    from _pytest.pytester import Testdir


def test_main(testdir: "Testdir") -> None:
    """Check dependencies are sorted."""
    shutil.copy(str(ROOT / TESTFILE), str(Path(str(testdir)) / TESTFILE.name))
    main([str(Path(str(testdir)) / TESTFILE.name)])
    result = (Path(str(testdir)) / TESTFILE.name).read_text()
    expected = """\
name: pymc3-dev-py38
channels:
- conda-forge
- defaults
dependencies:
- h5py>=2.7
- ipython>=7.16
- libblas=*=*mkl
- mkl-service
- nbsphinx>=0.4
- numpydoc>=0.9
- pre-commit>=2.8.0
- pytest-cov>=2.5
- pytest>=3.0
- python-graphviz
- python=3.8
- recommonmark>=0.4
- sphinx-autobuild>=0.7
- sphinx>=1.5
- watermark
"""
    assert result == expected
