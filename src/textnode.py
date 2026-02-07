from enum import Enum
from typing import Self


class TextType(Enum):
    PLAIN = "plain"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
    LINK_TEXT = "link_text"
    IMAGE_TEXT = "image_text"


class TextNode:
    text: str
    text_type: TextType
    url: str | None

    def __init__(
        self: Self,
        text: str,
        text_type: TextType,
        url: str | None = None,
    ) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self: Self, value: object) -> bool:
        return (
            (
                self.text == value.text
                and self.text_type == value.text_type
                and self.url == value.url
            )
            if isinstance(value, TextNode)
            else NotImplemented
        )

    def __repr__(self: Self) -> str:
        return f"TextNode({self.text},{self.text_type.value},{self.url})"
