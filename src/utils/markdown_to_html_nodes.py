from nodes.htmlnode import HTMLNode
from nodes.parentnode import ParentNode
from nodes.leafnode import LeafNode
from utils.markdown_to_blocks import markdown_to_blocks
from nodes.blocks.block_types import block_to_blocktype, BlockType
from utils.text_to_nodes import text_to_nodes
from utils.text_to_html import text_node_to_html
import re


def markdown_to_html_nodes(markdown: str) -> HTMLNode:
    markdown_blocks = markdown_to_blocks(markdown)
    children = []

    for block in markdown_blocks:
        block_type = block_to_blocktype(block)
        html_node = block_to_html_node(block, block_type)
        children.append(html_node)

    return ParentNode("div", children)


def block_to_html_node(block: str, block_type: BlockType) -> HTMLNode:
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)

        case BlockType.QUOTE:
            return quote_to_html_node(block)

        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html_node(block)

        case BlockType.ORDERED_LIST:
            return ordered_list_to_html_node(block)


def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_nodes(text)
    return [text_node_to_html(node) for node in text_nodes]


def paragraph_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    text = " ".join(lines).strip()
    children = text_to_children(text)
    return ParentNode("p", children)


def heading_to_html_node(block: str) -> HTMLNode:
    match = re.match(r"^(#{1,6}) (.+)$", block)
    if not match:
        raise ValueError("Invalid heading format")

    level = len(match.group(1))
    text = match.group(2).strip()
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    if not (lines[0].startswith("```") and lines[-1].startswith("```")):
        raise ValueError("Invalid code block format")

    code_text = "\n".join(lines[1:-1]).strip()
    code_node = LeafNode(code_text + "\n", "code")
    return ParentNode("pre", [code_node])


def quote_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    quote_lines = []

    for line in lines:
        if line.startswith(">"):
            quote_lines.append(line[1:].strip())
        else:
            quote_lines.append(line.strip())

    text = " ".join(quote_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)


def unordered_list_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    list_items = []

    for line in lines:
        if line.startswith("- "):
            text = line[2:].strip()
            children = text_to_children(text)
            list_items.append(ParentNode("li", children))

    return ParentNode("ul", list_items)


def ordered_list_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    list_items = []

    for line in lines:
        match = re.match(r"^\d+\. (.+)$", line)
        if match:
            text = match.group(1).strip()
            children = text_to_children(text)
            list_items.append(ParentNode("li", children))

    return ParentNode("ol", list_items)
