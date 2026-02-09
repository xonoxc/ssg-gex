from nodes.textnode import TextNode, TextType
from utils.text_to_nodes import text_to_nodes


def test_plain_text_only():
    nodes = text_to_nodes("just normal text")

    assert nodes == [TextNode("just normal text", TextType.PLAIN)]


def test_inline_formatting():
    nodes = text_to_nodes("this is **bold** and _italic_ and `code`")

    assert nodes == [
        TextNode("this is ", TextType.PLAIN),
        TextNode("bold", TextType.BOLD_TEXT),
        TextNode(" and ", TextType.PLAIN),
        TextNode("italic", TextType.BOLD_TEXT),
        TextNode(" and ", TextType.PLAIN),
        TextNode("code", TextType.BOLD_TEXT),
    ]


def test_images_only():
    nodes = text_to_nodes("![img](url1) ![img2](url2)")

    assert nodes == [
        TextNode("img", TextType.IMAGE_TEXT, "url1"),
        TextNode(" ", TextType.PLAIN),
        TextNode("img2", TextType.IMAGE_TEXT, "url2"),
    ]


def test_links_only():
    nodes = text_to_nodes("[google](https://google.com) and [bing](https://bing.com)")

    assert nodes == [
        TextNode("google", TextType.LINK_TEXT, "https://google.com"),
        TextNode(" and ", TextType.PLAIN),
        TextNode("bing", TextType.LINK_TEXT, "https://bing.com"),
    ]


def test_mixed_content():
    nodes = text_to_nodes("hello **bold** ![img](url) see [link](dest)")

    assert nodes == [
        TextNode("hello ", TextType.PLAIN),
        TextNode("bold", TextType.BOLD_TEXT),
        TextNode(" ", TextType.PLAIN),
        TextNode("img", TextType.IMAGE_TEXT, "url"),
        TextNode(" see ", TextType.PLAIN),
        TextNode("link", TextType.LINK_TEXT, "dest"),
    ]


def test_no_empty_nodes_emitted():
    nodes = text_to_nodes("**bold**")

    assert nodes == [TextNode("bold", TextType.BOLD_TEXT)]


def test_node_order_is_preserved():
    text = "a **b** c ![d](u) e [f](v) g"
    nodes = text_to_nodes(text)

    texts = [node.text for node in nodes]
    assert texts == ["a ", "b", " c ", "d", " e ", "f", " g"]
