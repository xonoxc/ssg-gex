import pytest
from typing import List, Dict, Optional
from htmlnode import HTMLNode


@pytest.fixture
def empty_node() -> HTMLNode:
    """Fixture for empty HTMLNode."""
    return HTMLNode(None, None, None, None)


@pytest.fixture
def text_node() -> HTMLNode:
    """Fixture for text-only HTMLNode."""
    return HTMLNode(None, "Hello World", None, None)


@pytest.fixture
def tag_node() -> HTMLNode:
    """Fixture for tag-only HTMLNode."""
    return HTMLNode("div", None, None, None)


@pytest.fixture
def tag_with_value_node() -> HTMLNode:
    """Fixture for HTMLNode with tag and value."""
    return HTMLNode("p", "This is a paragraph", None, None)


@pytest.fixture
def node_with_props() -> HTMLNode:
    """Fixture for HTMLNode with properties."""
    return HTMLNode("a", None, None, {"href": "https://example.com"})


@pytest.fixture
def node_with_children() -> HTMLNode:
    """Fixture for HTMLNode with children."""
    return HTMLNode(
        "ul",
        None,
        [HTMLNode("li", "Item 1", None, None), HTMLNode("li", "Item 2", None, None)],
        None,
    )


@pytest.fixture
def complex_node() -> HTMLNode:
    """Fixture for complex HTMLNode with all attributes."""
    return HTMLNode(
        "div",
        "Content",
        [
            HTMLNode("p", "Paragraph", None, {"class": "text"}),
            HTMLNode("span", "Span text", None, {"id": "highlight"}),
        ],
        {"class": "container", "id": "main"},
    )


def test_constructor_initialization() -> None:
    """Test that constructor properly initializes all attributes."""
    node: HTMLNode = HTMLNode("h1", "Title", [], {"class": "heading"})
    assert node.tag == "h1"
    assert node.value == "Title"
    assert node.children == []
    assert node.props == {"class": "heading"}


def test_constructor_with_none_values() -> None:
    """Test constructor with None values."""
    node: HTMLNode = HTMLNode(None, None, None, None)
    assert node.tag is None
    assert node.value is None
    assert node.children is None
    assert node.props is None


def test_to_html_with_no_tag(text_node: HTMLNode, empty_node: HTMLNode) -> None:
    """Test to_html when tag is None returns value or empty string."""
    assert text_node.to_html() == "Hello World"
    assert empty_node.to_html() == ""


def test_to_html_with_tag_no_value_no_children_no_props(tag_node: HTMLNode) -> None:
    """Test to_html with tag but no value, children, or props."""
    expected: str = "<div></div>"
    assert tag_node.to_html() == expected


def test_to_html_with_tag_and_value(tag_with_value_node: HTMLNode) -> None:
    """Test to_html with tag and value but no children or props."""
    expected: str = "<p>This is a paragraph</p>"
    assert tag_with_value_node.to_html() == expected


def test_to_html_with_tag_and_props(node_with_props: HTMLNode) -> None:
    """Test to_html with tag and props but no children."""
    expected: str = '<a href="https://example.com"></a>'
    assert node_with_props.to_html() == expected


def test_to_html_with_tag_and_children(node_with_children: HTMLNode) -> None:
    """Test to_html with tag and children but no props."""
    expected: str = "<ul><li>Item 1</li><li>Item 2</li></ul>"
    assert node_with_children.to_html() == expected


def test_to_html_complex_node(complex_node: HTMLNode) -> None:
    """Test to_html with tag, value, children, and props."""
    expected: str = '<div class="container" id="main"><p class="text">Paragraph</p><span id="highlight">Span text</span>Content</div>'
    assert complex_node.to_html() == expected


def test_stringified_props() -> None:
    """Test stringified_props method converts props dict to HTML attributes string."""
    node: HTMLNode = HTMLNode("div", None, None, {"class": "test", "id": "example"})
    expected: str = ' class="test" id="example"'
    assert node.stringified_props() == expected


def test_stringified_props_empty_props() -> None:
    """Test stringified_props with empty props dict."""
    node: HTMLNode = HTMLNode("div", None, None, {})
    expected: str = ""
    assert node.stringified_props() == expected


def test_stringified_props_none_props() -> None:
    """Test stringified_props with None props."""
    node: HTMLNode = HTMLNode("div", None, None, None)
    expected: str = ""
    assert node.stringified_props() == expected


def test_stringified_props_special_characters() -> None:
    """Test stringified_props with special characters in values."""
    node: HTMLNode = HTMLNode(
        "div", None, None, {"data-value": "test&special", "title": 'Quote"Test'}
    )
    expected: str = ' data-value="test&special" title="Quote"Test"'
    assert node.stringified_props() == expected


def test_to_string_rep() -> None:
    """Test to_string_rep method creates complete HTML tag string."""
    node: HTMLNode = HTMLNode("div", None, None, None)
    props_str: str = ' class="container"'
    children_str: str = "<p>Hello</p>"
    expected: str = '<div class="container"><p>Hello</p></div>'
    assert node.to_string_rep(props_str, children_str) == expected


def test_to_string_rep_no_props() -> None:
    """Test to_string_rep with empty props."""
    node: HTMLNode = HTMLNode("span", None, None, None)
    props_str: str = ""
    children_str: str = "Text content"
    expected: str = "<span>Text content</span>"
    assert node.to_string_rep(props_str, children_str) == expected


def test_nested_children_to_html() -> None:
    """Test to_html with deeply nested children."""
    nested_node: HTMLNode = HTMLNode(
        "html",
        None,
        [
            HTMLNode("head", None, [HTMLNode("title", "Page Title", None, None)], None),
            HTMLNode(
                "body",
                None,
                [
                    HTMLNode(
                        "div",
                        None,
                        [HTMLNode("p", "Nested paragraph", None, {"class": "content"})],
                        {"id": "main"},
                    )
                ],
                None,
            ),
        ],
        None,
    )

    expected: str = '<html><head><title>Page Title</title></head><body><div id="main"><p class="content">Nested paragraph</p></div></body></html>'
    assert nested_node.to_html() == expected


def test_empty_children_list() -> None:
    """Test to_html with empty children list."""
    node: HTMLNode = HTMLNode("div", None, [], {"class": "empty"})
    expected: str = '<div class="empty"></div>'
    assert node.to_html() == expected


def test_boolean_props() -> None:
    """Test to_html with boolean-style attributes."""
    node: HTMLNode = HTMLNode(
        "input", None, None, {"disabled": "", "required": "required"}
    )
    expected: str = '<input disabled="" required="required"></input>'
    assert node.to_html() == expected


def test_large_content() -> None:
    """Test to_html with large content."""
    large_content: str = "A" * 10000
    node: HTMLNode = HTMLNode("div", large_content, None, None)
    expected: str = f"<div>{large_content}</div>"
    assert node.to_html() == expected


@pytest.mark.parametrize(
    "tag,value,children,props,expected",
    [
        ("b", "Bold text", None, None, "<b>Bold text</b>"),
        ("i", None, None, None, "<i></i>"),
        (None, "Plain text", None, None, "Plain text"),
        (
            "span",
            None,
            [HTMLNode("strong", "Strong", None, None)],
            None,
            "<span><strong>Strong</strong></span>",
        ),
    ],
)
def test_to_html_parametrized(
    tag: Optional[str],
    value: Optional[str],
    children: Optional[List[HTMLNode]],
    props: Optional[Dict[str, str]],
    expected: str,
) -> None:
    """Parametrized test for to_html method."""
    node: HTMLNode = HTMLNode(tag, value, children, props)
    assert node.to_html() == expected


def test_multiple_props_order() -> None:
    """Test that props order doesn't affect output."""
    node1: HTMLNode = HTMLNode(
        "div", None, None, {"class": "test", "id": "example", "style": "color:red"}
    )
    node2: HTMLNode = HTMLNode(
        "div", None, None, {"style": "color:red", "class": "test", "id": "example"}
    )

    # Both should contain all attributes
    output1: str = node1.to_html()
    output2: str = node2.to_html()

    # Both should contain all attributes
    assert 'class="test"' in output1
    assert 'id="example"' in output1
    assert 'style="color:red"' in output1
    assert 'class="test"' in output2
    assert 'id="example"' in output2
    assert 'style="color:red"' in output2


def test_attribute_types() -> None:
    """Test that all attributes have correct types."""
    node: HTMLNode = HTMLNode("p", "test", [], {"class": "test"})

    assert isinstance(node.tag, str)
    assert isinstance(node.value, str)
    assert isinstance(node.children, list)
    assert isinstance(node.props, dict)

    # Test with None values
    empty_node: HTMLNode = HTMLNode(None, None, None, None)
    assert empty_node.tag is None
    assert empty_node.value is None
    assert empty_node.children is None
    assert empty_node.props is None


def test_to_html_return_type() -> None:
    """Test that to_html always returns a string."""
    test_nodes: List[HTMLNode] = [
        HTMLNode(None, None, None, None),
        HTMLNode("div", None, None, None),
        HTMLNode("p", "test", None, None),
        HTMLNode("a", None, None, {"href": "test"}),
        HTMLNode("ul", None, [HTMLNode("li", "item", None, None)], None),
    ]

    for node in test_nodes:
        result: str = node.to_html()
        assert isinstance(result, str)
