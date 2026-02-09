from typing import List
from nodes.htmlnode import HTMLNode
from errors.syntax import MarkdownSyntaxError
from nodes.textnode import TextNode, TextType


def split_nodes_delemeter(
    old_nodes: List[TextNode],
    delemeter: str,
    text_type: TextType,
) -> List[HTMLNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue

        split_nodes = []

        sections = node.text.split(delemeter)
        if len(sections) % 2 == 0:
            raise MarkdownSyntaxError(f"missing closing delemeter for {delemeter}")

        for i in range(len(sections)):
            if sections[i] == "":
                continue

            if i % 2 == 0:
                split_nodes.append(
                    TextNode(
                        text=sections[i],
                        text_type=TextType.PLAIN,
                    ),
                )
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        new_nodes.extend(split_nodes)

    return new_nodes
