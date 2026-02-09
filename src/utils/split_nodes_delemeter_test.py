import pytest
from nodes.textnode import TextNode, TextType
from errors.syntax import MarkdownSyntaxError
from utils.split_nodes_delemeter import split_nodes_delemeter


def test_basic_delimiter_splitting():
    """Test basic delimiter splitting functionality"""
    old_nodes = [TextNode("Hello *world* test", TextType.PLAIN)]
    result = split_nodes_delemeter(old_nodes, "*", TextType.BOLD_TEXT)

    assert len(result) == 3
    assert result[0].text == "Hello "
    assert result[0].text_type == TextType.PLAIN
    assert result[1].text == "world"
    assert result[1].text_type == TextType.BOLD_TEXT
    assert result[2].text == " test"
    assert result[2].text_type == TextType.PLAIN


def test_multiple_delimiters():
    """Test text with multiple delimiter pairs"""
    old_nodes = [TextNode("*bold* and *another*", TextType.PLAIN)]
    result = split_nodes_delemeter(old_nodes, "*", TextType.BOLD_TEXT)

    assert len(result) == 3
    assert result[0].text_type == TextType.BOLD_TEXT
    assert result[0].text == "bold"
    assert result[1].text_type == TextType.PLAIN
    assert result[1].text == " and "
    assert result[2].text_type == TextType.BOLD_TEXT
    assert result[2].text == "another"


def test_no_delimiters():
    """Test text without any delimiters"""
    old_nodes = [TextNode("plain text", TextType.PLAIN)]
    result = split_nodes_delemeter(old_nodes, "*", TextType.BOLD_TEXT)

    assert len(result) == 1
    assert result[0].text == "plain text"
    assert result[0].text_type == TextType.PLAIN


def test_empty_sections():
    """Test handling of empty sections"""
    old_nodes = [TextNode("**", TextType.PLAIN)]
    result = split_nodes_delemeter(old_nodes, "*", TextType.BOLD_TEXT)

    assert len(result) == 0


def test_text_starting_with_delimiter():
    """Test text that starts with delimiter"""
    old_nodes = [TextNode("*bold* text", TextType.PLAIN)]
    result = split_nodes_delemeter(old_nodes, "*", TextType.BOLD_TEXT)

    assert len(result) == 2
    assert result[0].text_type == TextType.BOLD_TEXT
    assert result[0].text == "bold"
    assert result[1].text_type == TextType.PLAIN
    assert result[1].text == " text"


def test_text_ending_with_delimiter():
    """Test text that ends with delimiter"""
    old_nodes = [TextNode("text *bold*", TextType.PLAIN)]
    result = split_nodes_delemeter(old_nodes, "*", TextType.BOLD_TEXT)

    assert len(result) == 2
    assert result[0].text_type == TextType.PLAIN
    assert result[0].text == "text "
    assert result[1].text_type == TextType.BOLD_TEXT
    assert result[1].text == "bold"


def test_unmatched_delimiter_error():
    """Test error for unmatched delimiters"""
    old_nodes = [TextNode("*unclosed", TextType.PLAIN)]

    with pytest.raises(MarkdownSyntaxError, match="missing closing delemeter for \\*"):
        split_nodes_delemeter(old_nodes, "*", TextType.BOLD_TEXT)


def test_unmatched_delimiter_error_opening():
    """Test error for missing opening delimiter"""
    old_nodes = [TextNode("unclosed*", TextType.PLAIN)]

    with pytest.raises(MarkdownSyntaxError, match="missing closing delemeter for \\*"):
        split_nodes_delemeter(old_nodes, "*", TextType.BOLD_TEXT)


def test_mixed_node_types():
    """Test with mixed plain and non-plain nodes"""
    old_nodes = [
        TextNode("plain *text*", TextType.PLAIN),
        TextNode("already bold", TextType.BOLD_TEXT),
        TextNode("*another plain*", TextType.PLAIN),
    ]
    result = split_nodes_delemeter(old_nodes, "*", TextType.BOLD_TEXT)

    assert len(result) == 4
    # First node split
    assert result[0].text_type == TextType.PLAIN
    assert result[0].text == "plain "
    assert result[1].text_type == TextType.BOLD_TEXT
    assert result[1].text == "text"
    # Second node unchanged
    assert result[2].text_type == TextType.BOLD_TEXT
    assert result[2].text == "already bold"
    # Third node split
    assert result[3].text_type == TextType.BOLD_TEXT
    assert result[3].text == "another plain"


def test_italic_delimiter():
    """Test with different delimiter (italic)"""
    old_nodes = [TextNode("_italic text_", TextType.PLAIN)]
    result = split_nodes_delemeter(old_nodes, "_", TextType.ITALIC_TEXT)

    assert len(result) == 1
    assert result[0].text_type == TextType.ITALIC_TEXT
    assert result[0].text == "italic text"


def test_code_delimiter():
    """Test with code delimiter"""
    old_nodes = [TextNode("`code` block", TextType.PLAIN)]
    result = split_nodes_delemeter(old_nodes, "`", TextType.CODE_TEXT)

    assert len(result) == 2
    assert result[0].text_type == TextType.CODE_TEXT
    assert result[0].text == "code"
    assert result[1].text_type == TextType.PLAIN
    assert result[1].text == " block"


def test_empty_input_list():
    """Test with empty input list"""
    old_nodes = []
    result = split_nodes_delemeter(old_nodes, "*", TextType.BOLD_TEXT)

    assert len(result) == 0


def test_consecutive_delimiters():
    """Test text with consecutive delimiters"""
    old_nodes = [TextNode("*a**b*", TextType.PLAIN)]
    result = split_nodes_delemeter(old_nodes, "*", TextType.BOLD_TEXT)

    assert len(result) == 2
    assert result[0].text_type == TextType.BOLD_TEXT
    assert result[0].text == "a"
    assert result[1].text_type == TextType.BOLD_TEXT
    assert result[1].text == "b"


def test_spaces_around_delimiters():
    """Test delimiters with spaces around them"""
    old_nodes = [TextNode("text * with spaces * around", TextType.PLAIN)]
    result = split_nodes_delemeter(old_nodes, "*", TextType.BOLD_TEXT)

    assert len(result) == 3
    assert result[0].text_type == TextType.PLAIN
    assert result[0].text == "text "
    assert result[1].text_type == TextType.BOLD_TEXT
    assert result[1].text == " with spaces "
    assert result[2].text_type == TextType.PLAIN
    assert result[2].text == " around"


def test_single_character_content():
    """Test single character content between delimiters"""
    old_nodes = [TextNode("*x*", TextType.PLAIN)]
    result = split_nodes_delemeter(old_nodes, "*", TextType.BOLD_TEXT)

    assert len(result) == 1
    assert result[0].text_type == TextType.BOLD_TEXT
    assert result[0].text == "x"


def test_multiple_nodes():
    """Test multiple plain nodes"""
    old_nodes = [
        TextNode("first *bold*", TextType.PLAIN),
        TextNode("second *bold*", TextType.PLAIN),
    ]
    result = split_nodes_delemeter(old_nodes, "*", TextType.BOLD_TEXT)

    assert len(result) == 4
    assert result[0].text_type == TextType.PLAIN
    assert result[0].text == "first "
    assert result[1].text_type == TextType.BOLD_TEXT
    assert result[1].text == "bold"
    assert result[2].text_type == TextType.PLAIN
    assert result[2].text == "second "
    assert result[3].text_type == TextType.BOLD_TEXT
    assert result[3].text == "bold"
