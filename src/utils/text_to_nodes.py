from typing import List
from nodes.textnode import TextNode, TextType
from utils.asset_splitters import split_asset_nodes, AssetType
from utils.split_nodes_delemeter import split_nodes_delemeter


def text_to_nodes(text: str) -> List[TextNode]:
    nodes = [TextNode(text=text, text_type=TextType.PLAIN)]
    nodes = split_nodes_delemeter(
        nodes,
        "**",
        TextType.BOLD_TEXT,
    )
    nodes = split_nodes_delemeter(nodes, "_", TextType.BOLD_TEXT)
    nodes = split_nodes_delemeter(
        nodes,
        "`",
        TextType.BOLD_TEXT,
    )

    nodes = split_asset_nodes(nodes, asset_type=AssetType.IMAGE)
    nodes = split_asset_nodes(
        nodes,
        asset_type=AssetType.LINK,
    )

    return nodes
