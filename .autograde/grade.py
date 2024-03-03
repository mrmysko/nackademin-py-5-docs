from pathlib import Path
import pytest

MARKDOWN_TEST_MD = Path(__file__).parent.parent.joinpath("uppgift.md")


def test_markdown():
    with open(MARKDOWN_TEST_MD) as f:
        lines = f.readlines()
    assert len(lines) > 60, "För få rader i uppgift.md. Du behöver skriva utförligare."
