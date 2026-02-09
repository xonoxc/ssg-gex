from nodes.textnode import TextNode, TextType
from nodes.leafnode import LeafNode


def text_node_to_html(node: TextNode):
    match node.text_type:
        case TextType.PLAIN:
            return LeafNode(value=node.text)

        case TextType.BOLD_TEXT:
            return LeafNode(tag="b", value=node.text)

        case TextType.ITALIC_TEXT:
            return LeafNode(tag="i", value=node.text)

        case TextType.CODE_TEXT:
            return LeafNode(tag="code", value=node.text)

        case TextType.LINK_TEXT:
            return LeafNode(
                tag="a",
                value=node.text,
                props={"href": node.url} if node.url else None,
            )

        case TextType.IMAGE_TEXT:
            return LeafNode(
                tag="img",
                value=node.text,
                props={"src": node.url} if node.url else None,
            )
