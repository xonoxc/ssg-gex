from nodes.textnode import TextNode, TextType
from utils.text_to_html import text_node_to_html


def test_text():
    node = TextNode("This is a text node", TextType.PLAIN)
    html_node = text_node_to_html(node)

    assert html_node.tag is None
    assert html_node.value == "This is a text node"
