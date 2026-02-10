import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_blocktype(markdown: str) -> BlockType:
    lines = markdown.split("\n")

    if markdown.startswith("```") and markdown.endswith("```") and len(lines) >= 2:
        return BlockType.CODE

    if re.match(r"^#{1,6} ", markdown):
        return BlockType.HEADING

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    ordered = True
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            ordered = False
            break
    if ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
