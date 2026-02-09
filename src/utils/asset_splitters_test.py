from nodes.textnode import TextNode
from utils.asset_splitters import AssetType, split_asset_nodes
from nodes.textnode import TextType


def test_split_images():
    node = TextNode(
        text="This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        text_type=TextType.PLAIN,
    )
    new_nodes = split_asset_nodes([node], asset_type=AssetType.IMAGE)

    assert [
        TextNode("This is text with an ", TextType.PLAIN),
        TextNode("image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and another ", TextType.PLAIN),
        TextNode(
            "second image", TextType.IMAGE_TEXT, "https://i.imgur.com/3elNhQu.png"
        ),
    ] == new_nodes


def test_split_images_multiple():
    node = TextNode(
        text="![one](url1) middle ![two](url2) end ![three](url3)",
        text_type=TextType.PLAIN,
    )

    new_nodes = split_asset_nodes([node], asset_type=AssetType.IMAGE)

    assert new_nodes == [
        TextNode("one", TextType.IMAGE_TEXT, "url1"),
        TextNode(" middle ", TextType.PLAIN),
        TextNode("two", TextType.IMAGE_TEXT, "url2"),
        TextNode(" end ", TextType.PLAIN),
        TextNode("three", TextType.IMAGE_TEXT, "url3"),
    ]


def test_split_images_at_start_and_end():
    node = TextNode(
        text="![start](url1) text in between ![end](url2)",
        text_type=TextType.PLAIN,
    )

    new_nodes = split_asset_nodes([node], asset_type=AssetType.IMAGE)

    assert new_nodes == [
        TextNode("start", TextType.IMAGE_TEXT, "url1"),
        TextNode(" text in between ", TextType.PLAIN),
        TextNode("end", TextType.IMAGE_TEXT, "url2"),
    ]


def test_split_images_no_images():
    node = TextNode(
        text="just plain boring text",
        text_type=TextType.PLAIN,
    )

    new_nodes = split_asset_nodes([node], asset_type=AssetType.IMAGE)

    assert new_nodes == [
        TextNode("just plain boring text", TextType.PLAIN),
    ]


def test_split_links_multiple():
    node = TextNode(
        text="visit [google](https://google.com) or [bing](https://bing.com)",
        text_type=TextType.PLAIN,
    )

    new_nodes = split_asset_nodes([node], asset_type=AssetType.LINK)

    assert new_nodes == [
        TextNode("visit ", TextType.PLAIN),
        TextNode("google", TextType.LINK_TEXT, "https://google.com"),
        TextNode(" or ", TextType.PLAIN),
        TextNode("bing", TextType.LINK_TEXT, "https://bing.com"),
    ]


def test_split_links_at_edges():
    node = TextNode(
        text="[start](url1) middle text [end](url2)",
        text_type=TextType.PLAIN,
    )

    new_nodes = split_asset_nodes([node], asset_type=AssetType.LINK)

    assert new_nodes == [
        TextNode("start", TextType.LINK_TEXT, "url1"),
        TextNode(" middle text ", TextType.PLAIN),
        TextNode("end", TextType.LINK_TEXT, "url2"),
    ]


def test_split_links_no_links():
    node = TextNode(
        text="absolutely no links here",
        text_type=TextType.PLAIN,
    )

    new_nodes = split_asset_nodes([node], asset_type=AssetType.LINK)

    assert new_nodes == [
        TextNode("absolutely no links here", TextType.PLAIN),
    ]
