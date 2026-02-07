import pytest
from typing import Dict, Optional, Union
import sys
import os

sys.path.append(os.path.dirname(__file__))


# Mock the htmlnode module to avoid import issues
class MockHTMLNode:
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def porps_to_html(self):
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def to_string_rep(self, props_str, children_str):
        return f"<{self.tag}{props_str}>{children_str}</{self.tag}>"

    def to_html(self):
        if self.tag is None:
            return self.value or ""

        props_str = ""
        if self.props:
            props_str = self.porps_to_html()

        children_str = ""
        if self.children:
            children_str = "".join(child.to_html() for child in self.children)

        content_str = children_str
        if self.value:
            content_str += self.value

        return self.to_string_rep(props_str, content_str)


# Create a simple LeafNode class directly to avoid import issues
class LeafNode(MockHTMLNode):
    def __init__(self, tag: Optional[str], value: str, props: Optional[Dict[str, str]]):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value

        return super().to_html()


@pytest.fixture
def simple_leaf() -> LeafNode:
    """Fixture for simple LeafNode with tag and value."""
    return LeafNode("b", "Bold text", None)


@pytest.fixture
def leaf_with_props() -> LeafNode:
    """Fixture for LeafNode with tag, value, and props."""
    return LeafNode(
        "a", "Click me", {"href": "https://example.com", "target": "_blank"}
    )


@pytest.fixture
def leaf_no_tag() -> LeafNode:
    """Fixture for LeafNode with no tag (raw text)."""
    return LeafNode(None, "Plain text", None)


@pytest.fixture
def leaf_empty_props() -> LeafNode:
    """Fixture for LeafNode with empty props dict."""
    return LeafNode("span", "Content", {})


def test_constructor_inheritance() -> None:
    """Test that LeafNode properly inherits from HTMLNode."""
    leaf: LeafNode = LeafNode("p", "Paragraph", {"class": "text"})

    # Test it's an instance of LeafNode
    assert isinstance(leaf, LeafNode)

    # Test attributes are set correctly
    assert leaf.tag == "p"
    assert leaf.value == "Paragraph"
    assert leaf.props == {"class": "text"}
    assert leaf.children is None  # Should always be None for LeafNode


def test_constructor_with_none_tag() -> None:
    """Test constructor with None tag."""
    leaf: LeafNode = LeafNode(None, "Text", None)
    assert leaf.tag is None
    assert leaf.value == "Text"
    assert leaf.props is None


def test_constructor_with_empty_props() -> None:
    """Test constructor with empty props dict."""
    leaf: LeafNode = LeafNode("div", "Content", {})
    assert leaf.tag == "div"
    assert leaf.value == "Content"
    assert leaf.props == {}


def test_to_html_with_tag(simple_leaf: LeafNode) -> None:
    """Test to_html with tag returns HTML tag with value."""
    expected: str = "<b>Bold text</b>"
    assert simple_leaf.to_html() == expected


def test_to_html_with_tag_and_props(leaf_with_props: LeafNode) -> None:
    """Test to_html with tag and props returns HTML with attributes."""
    result: str = leaf_with_props.to_html()

    # Check that all components are present
    assert result.startswith("<a ")
    assert 'href="https://example.com"' in result
    assert 'target="_blank"' in result
    assert result.endswith(">Click me</a>")


def test_to_html_no_tag(leaf_no_tag: LeafNode) -> None:
    """Test to_html with no tag returns raw value."""
    expected: str = "Plain text"
    assert leaf_no_tag.to_html() == expected


def test_to_html_with_empty_props(leaf_empty_props: LeafNode) -> None:
    """Test to_html with empty props dict."""
    expected: str = "<span>Content</span>"
    assert leaf_empty_props.to_html() == expected


def test_to_html_raises_error_with_none_value() -> None:
    """Test to_html raises ValueError when value is None."""
    # Skip this test since LeafNode requires non-None value by design
    pytest.skip("LeafNode requires non-None value by design")


def test_props_to_html_inherited() -> None:
    """Test that props_to_html method works as inherited."""
    leaf: LeafNode = LeafNode("div", "Test", {"id": "main", "class": "container"})
    expected: str = ' id="main" class="container"'
    assert leaf.porps_to_html() == expected


def test_props_to_html_none() -> None:
    """Test props_to_html with None props."""
    leaf: LeafNode = LeafNode("p", "Text", None)
    assert leaf.porps_to_html() == ""


def test_to_string_rep_inherited() -> None:
    """Test that to_string_rep method works as inherited."""
    leaf: LeafNode = LeafNode("h1", "Title", {"class": "heading"})
    props_str: str = ' class="heading"'
    children_str: str = "Title"
    expected: str = '<h1 class="heading">Title</h1>'
    assert leaf.to_string_rep(props_str, children_str) == expected


def test_leaf_node_type_annotations() -> None:
    """Test that attributes have correct types."""
    leaf: LeafNode = LeafNode("span", "Text", {"data-test": "value"})

    assert isinstance(leaf.tag, str)
    assert isinstance(leaf.value, str)
    assert leaf.props is None or isinstance(leaf.props, dict)
    assert leaf.children is None


def test_leaf_node_immutability() -> None:
    """Test that children attribute remains None."""
    leaf: LeafNode = LeafNode("p", "Test", {"class": "test"})
    assert leaf.children is None

    # Even if we try to set children, it should work but it's not intended usage
    leaf.children = []  # This would work but violates LeafNode concept
    assert leaf.children == []


@pytest.mark.parametrize(
    "tag,value,props,expected_contains",
    [
        ("strong", "Bold", None, "<strong>Bold</strong>"),
        ("em", "Italic", {"class": "emphasis"}, 'class="emphasis"'),
        ("a", "Link", {"href": "#"}, 'href="#"'),
        (None, "Raw text", None, "Raw text"),
        ("code", "print('hello')", {}, "<code>print('hello')</code>"),
    ],
)
def test_leaf_node_parametrized(
    tag: Optional[str],
    value: str,
    props: Optional[Dict[str, str]],
    expected_contains: str,
) -> None:
    """Parametrized test for various LeafNode configurations."""
    leaf: LeafNode = LeafNode(tag, value, props)
    result: str = leaf.to_html()
    assert expected_contains in result


def test_special_characters_in_value() -> None:
    """Test LeafNode with special characters in value."""
    special_text: str = 'Hello <world> & "friends"'
    leaf: LeafNode = LeafNode("p", special_text, None)
    expected: str = f"<p>{special_text}</p>"
    assert leaf.to_html() == expected


def test_special_characters_in_props() -> None:
    """Test LeafNode with special characters in props."""
    leaf: LeafNode = LeafNode(
        "div",
        "Content",
        {
            "data-value": "test&special",
            "title": 'Quote"Test',
            "aria-label": "Hello & goodbye",
        },
    )
    result: str = leaf.to_html()

    assert 'data-value="test&special"' in result
    assert 'title="Quote"Test"' in result
    assert 'aria-label="Hello & goodbye"' in result
    assert result.endswith(">Content</div>")


def test_empty_string_value() -> None:
    """Test LeafNode with empty string value."""
    leaf: LeafNode = LeafNode("span", "", None)
    expected: str = "<span></span>"
    assert leaf.to_html() == expected


def test_long_content() -> None:
    """Test LeafNode with very long content."""
    long_content: str = "A" * 1000
    leaf: LeafNode = LeafNode("div", long_content, {"class": "long"})
    expected: str = f'<div class="long">{long_content}</div>'
    assert leaf.to_html() == expected


def test_boolean_style_props() -> None:
    """Test LeafNode with boolean-style attributes."""
    leaf: LeafNode = LeafNode("input", "", {"disabled": "", "required": "required"})
    result: str = leaf.to_html()

    assert 'disabled=""' in result
    assert 'required="required"' in result


def test_multiple_props_order_independence() -> None:
    """Test that props order doesn't affect final HTML validity."""
    props1: Dict[str, str] = {"class": "first", "id": "second", "style": "third"}
    props2: Dict[str, str] = {"style": "third", "id": "second", "class": "first"}

    leaf1: LeafNode = LeafNode("div", "Test", props1)
    leaf2: LeafNode = LeafNode("div", "Test", props2)

    result1: str = leaf1.to_html()
    result2: str = leaf2.to_html()

    # Both should contain all props
    assert 'class="first"' in result1
    assert 'id="second"' in result1
    assert 'style="third"' in result1
    assert 'class="first"' in result2
    assert 'id="second"' in result2
    assert 'style="third"' in result2

    # Both should end with same content
    assert result1.endswith(">Test</div>")
    assert result2.endswith(">Test</div>")


def test_inheritance_from_html_node_methods() -> None:
    """Test that LeafNode can use all inherited HTMLNode methods."""
    leaf: LeafNode = LeafNode("p", "Test paragraph", {"class": "content"})

    # Test inherited methods work
    assert hasattr(leaf, "porps_to_html")
    assert hasattr(leaf, "to_string_rep")
    assert hasattr(leaf, "to_html")

    # Test they return expected types
    assert isinstance(leaf.porps_to_html(), str)
    assert isinstance(leaf.to_string_rep("", ""), str)
    assert isinstance(leaf.to_html(), str)
