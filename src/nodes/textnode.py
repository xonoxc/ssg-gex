from enum import Enum


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

    # constrcutor
    def __init__(
        self,
        text: str,
        text_type: TextType,
        url: str | None = None,
    ) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    # equality check operators enabled classinstanc1 == classinstance2 check for
    # testing
    def __eq__(self, value: object) -> bool:
        return (
            (
                self.text == value.text
                and self.text_type == value.text_type
                and self.url == value.url
            )
            if isinstance(value, TextNode)
            else NotImplemented
        )

    # returns a string reperesntation of the class
    def __repr__(self) -> str:
        return f"TextNode({self.text},{self.text_type.value},{self.url})"
