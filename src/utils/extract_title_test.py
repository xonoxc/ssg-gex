import pytest
from utils.extract_title import extract_title_h1


def test_basic_h1():
    md = "# Hello World"
    assert extract_title_h1(md) == "Hello World"


def test_h1_with_extra_whitespace():
    md = "#    Hello World    "
    assert extract_title_h1(md) == "Hello World"


def test_h1_not_first_line():
    md = """
    Some intro text

    # Title Here

    More content
    """
    assert extract_title_h1(md) == "Title Here"


def test_multiple_headings_returns_first_h1():
    md = """
    # First Title
    # Second Title
    """
    assert extract_title_h1(md) == "First Title"


def test_ignores_h2():
    md = "## Not an H1"
    with pytest.raises(Exception):
        extract_title_h1(md)


def test_no_heading_raises():
    md = "Just plain text"
    with pytest.raises(Exception):
        extract_title_h1(md)


def test_empty_string_raises():
    with pytest.raises(Exception):
        extract_title_h1("")


def test_hash_without_space_not_valid_h1():
    md = "#Invalid"
    with pytest.raises(Exception):
        extract_title_h1(md)


def test_leading_spaces_before_hash():
    md = "   # Indented Title"
    # Depending on your spec:
    # If you allow leading spaces → assert title
    # If you don't → expect exception
    assert extract_title_h1(md) == "Indented Title"
