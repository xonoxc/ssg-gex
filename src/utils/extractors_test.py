from utils.extractors import extract_markdown_images, extract_markdown_links


def test_extract_markdown_images():
    """Test basic image extraction"""
    matches = extract_markdown_images(
        text="This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    assert matches == [("image", "https://i.imgur.com/zjjcJKZ.png")]


def test_extract_markdown_images_multiple():
    """Test extracting multiple images"""
    text = "Here's ![first](https://example.com/1.png) and ![second](https://example.com/2.jpg)"
    matches = extract_markdown_images(text)
    assert matches == [
        ("first", "https://example.com/1.png"),
        ("second", "https://example.com/2.jpg"),
    ]


def test_extract_markdown_images_no_matches():
    """Test text with no images"""
    matches = extract_markdown_images("This is just plain text with no images")
    assert matches == []


def test_extract_markdown_images_empty_alt():
    """Test image with empty alt text"""
    matches = extract_markdown_images(
        "Here's an empty alt ![](https://example.com/image.png)"
    )
    assert matches == [("", "https://example.com/image.png")]


def test_extract_markdown_images_special_chars():
    """Test image with special characters in alt text"""
    matches = extract_markdown_images(
        "![test-image_123](https://example.com/image.png)"
    )
    assert matches == [("test-image_123", "https://example.com/image.png")]


def test_extract_markdown_images_nested_brackets():
    """Test image with brackets in alt text"""
    matches = extract_markdown_images(
        "![alt with [brackets]](https://example.com/image.png)"
    )
    assert matches == [("alt with [brackets]", "https://example.com/image.png")]


def test_extract_markdown_links():
    """Test basic link extraction"""
    matches = extract_markdown_links(text="This is a [link](https://example.com)")
    assert matches == [("link", "https://example.com")]


def test_extract_markdown_links_multiple():
    """Test extracting multiple links"""
    text = "Here's [first](https://example.com/1) and [second](https://example.com/2)"
    matches = extract_markdown_links(text)
    assert matches == [
        ("first", "https://example.com/1"),
        ("second", "https://example.com/2"),
    ]


def test_extract_markdown_links_no_matches():
    """Test text with no links"""
    matches = extract_markdown_links("This is just plain text with no links")
    assert matches == []


def test_extract_markdown_links_empty_text():
    """Test link with empty display text"""
    matches = extract_markdown_links("Here's an empty [](https://example.com)")
    assert matches == [("", "https://example.com")]


def test_extract_markdown_links_special_chars():
    """Test link with special characters"""
    matches = extract_markdown_links("[test-link_123](https://example.com/page)")
    assert matches == [("test-link_123", "https://example.com/page")]


def test_extract_images_and_links_together():
    """Test that images are not extracted as links and vice versa"""
    text = "Image: ![img](https://img.com/img.png) Link: [link](https://link.com)"

    images = extract_markdown_images(text)
    links = extract_markdown_links(text)

    assert images == [("img", "https://img.com/img.png")]
    assert links == [("link", "https://link.com")]


def test_extract_markdown_images_complex_url():
    """Test image with complex URL containing query params"""
    matches = extract_markdown_images(
        "![image](https://example.com/image.png?size=large&format=webp)"
    )
    assert matches == [
        ("image", "https://example.com/image.png?size=large&format=webp")
    ]


def test_extract_markdown_links_complex_url():
    """Test link with complex URL containing query params"""
    matches = extract_markdown_links("[link](https://example.com/page?id=123&ref=home)")
    assert matches == [("link", "https://example.com/page?id=123&ref=home")]


def test_extract_markdown_images_with_parentheses_in_alt():
    """Test image with parentheses in alt text"""
    matches = extract_markdown_images(
        "![alt (with parentheses)](https://example.com/image.png)"
    )
    assert matches == [("alt (with parentheses)", "https://example.com/image.png")]


def test_extract_markdown_links_with_parentheses_in_text():
    """Test link with parentheses in display text"""
    matches = extract_markdown_links("[text (with parentheses)](https://example.com)")
    assert matches == [("text (with parentheses)", "https://example.com")]


def test_extract_markdown_images_consecutive():
    """Test consecutive images"""
    text = "![img1](url1)![img2](url2)"
    matches = extract_markdown_images(text)
    assert matches == [("img1", "url1"), ("img2", "url2")]


def test_extract_markdown_links_consecutive():
    """Test consecutive links"""
    text = "[link1](url1)[link2](url2)"
    matches = extract_markdown_links(text)
    assert matches == [("link1", "url1"), ("link2", "url2")]


def test_extract_markdown_images_edge_cases():
    """Test edge cases with malformed markdown"""
    # Missing closing parenthesis
    matches = extract_markdown_images("![image](https://example.com/image.png")
    assert matches == []

    # Missing opening bracket
    matches = extract_markdown_images("image](https://example.com/image.png)")
    assert matches == []


def test_extract_markdown_links_edge_cases():
    """Test edge cases with malformed markdown"""
    # Missing closing parenthesis
    matches = extract_markdown_links("[link](https://example.com/page")
    assert matches == []

    # Missing opening bracket
    matches = extract_markdown_links("link](https://example.com/page)")
    assert matches == []
