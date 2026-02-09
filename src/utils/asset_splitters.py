from enum import Enum
import re
from typing import List

from nodes.textnode import TextNode, TextType

IMAGE_PATTERN = re.compile(r"!\[((?:[^\[\]]+|\[[^\[\]]*\])*)\]\(([^()\s]+)\)")
LINK_PATTERN = re.compile(
    r"(?<!!)\[((?:[^\[\]]+|\[[^\[\]]*\])*)\]\(([^()\s]+)\)",
)


class AssetType(Enum):
    IMAGE = "image"
    LINK = "link"


def isImageAsset(type: AssetType) -> bool:
    return type is AssetType.IMAGE


def split_asset_nodes(
    old_nodes: List[TextNode],
    asset_type: AssetType,
) -> List[TextNode]:
    new_nodes = []

    is_image_asset = isImageAsset(asset_type)
    pattern = IMAGE_PATTERN if is_image_asset else LINK_PATTERN

    asset_enum_type = TextType.IMAGE_TEXT if is_image_asset else TextType.LINK_TEXT

    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue

        text = node.text
        last_index = 0

        for match in pattern.finditer(text):
            start, end = match.span()
            alt_text, url = match.groups()

            if start > last_index:
                new_nodes.append(
                    TextNode(text=text[last_index:start], text_type=TextType.PLAIN)
                )

            new_nodes.append(
                TextNode(
                    text=alt_text,
                    text_type=asset_enum_type,
                    url=url,
                )
            )

            last_index = end

        if last_index < len(text):
            new_nodes.append(
                TextNode(
                    text=text[last_index:],
                    text_type=TextType.PLAIN,
                )
            )

    return new_nodes
