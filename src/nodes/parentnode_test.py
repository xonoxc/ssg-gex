from nodes.parentnode import ParentNode
from nodes.leafnode import LeafNode


def test_to_html_with_children():
    child_node = LeafNode(
        tag="span",
        value="child",
    )
    parent_node = ParentNode(
        tag="div",
        children=[child_node],
    )

    assert parent_node.to_html() == "<div><span>child</span></div>"


def test_to_html_with_grandchildren():
    grandchild_node = LeafNode(
        tag="b",
        value="grandchild",
    )
    child_node = ParentNode(
        tag="span",
        children=[grandchild_node],
    )
    parent_node = ParentNode(
        tag="div",
        children=[child_node],
    )

    assert parent_node.to_html() == "<div><span><b>grandchild</b></span></div>"
