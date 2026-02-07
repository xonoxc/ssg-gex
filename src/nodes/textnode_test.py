from nodes.textnode import TextNode, TextType


class TestTextNode:
    def test_eq(self) -> None:
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        assert node == node2

    def test_not_eq(self) -> None:
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.PLAIN)

        assert node2 != node
