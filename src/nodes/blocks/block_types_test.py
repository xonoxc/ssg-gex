from nodes.blocks.block_types import block_to_blocktype, BlockType


def test_paragraph_single_line():
    md = "This is a normal paragraph."
    assert block_to_blocktype(md) == BlockType.PARAGRAPH


def test_paragraph_multiline():
    md = "This is a paragraph\nthat spans multiple lines."
    assert block_to_blocktype(md) == BlockType.PARAGRAPH


def test_heading_levels():
    for level in range(1, 7):
        md = "#" * level + " Heading"
        assert block_to_blocktype(md) == BlockType.HEADING


def test_heading_invalid_no_space():
    md = "##Heading"
    assert block_to_blocktype(md) == BlockType.PARAGRAPH


def test_code_block_single_line_body():
    md = "```\ncode\n```"
    assert block_to_blocktype(md) == BlockType.CODE


def test_code_block_multiline_body():
    md = "```\nline one\nline two\nline three\n```"
    assert block_to_blocktype(md) == BlockType.CODE


def test_code_block_not_closed():
    md = "```\ncode"
    assert block_to_blocktype(md) == BlockType.PARAGRAPH


def test_quote_single_line():
    md = "> This is a quote"
    assert block_to_blocktype(md) == BlockType.QUOTE


def test_quote_multiline():
    md = "> line one\n> line two\n>line three"
    assert block_to_blocktype(md) == BlockType.QUOTE


def test_quote_invalid_mixed_lines():
    md = "> quoted line\nnot quoted"
    assert block_to_blocktype(md) == BlockType.PARAGRAPH


def test_unordered_list_single_item():
    md = "- item"
    assert block_to_blocktype(md) == BlockType.UNORDERED_LIST


def test_unordered_list_multiple_items():
    md = "- first\n- second\n- third"
    assert block_to_blocktype(md) == BlockType.UNORDERED_LIST


def test_unordered_list_invalid_missing_space():
    md = "-item"
    assert block_to_blocktype(md) == BlockType.PARAGRAPH


def test_ordered_list_valid():
    md = "1. first\n2. second\n3. third"
    assert block_to_blocktype(md) == BlockType.ORDERED_LIST


def test_ordered_list_invalid_start_not_one():
    md = "2. second\n3. third"
    assert block_to_blocktype(md) == BlockType.PARAGRAPH


def test_ordered_list_invalid_skip_number():
    md = "1. first\n3. third"
    assert block_to_blocktype(md) == BlockType.PARAGRAPH


def test_ordered_list_invalid_wrong_format():
    md = "1.first\n2.second"
    assert block_to_blocktype(md) == BlockType.PARAGRAPH


def test_mixed_list_is_not_list():
    md = "- item\n1. not same list"
    assert block_to_blocktype(md) == BlockType.PARAGRAPH
