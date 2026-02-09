from typing import Dict, override
from nodes.htmlnode import HTMLNode


# this is a leaf node that does not contain
# another HTMLnode, it only contains a value, and it does not have a tag or props
class LeafNode(HTMLNode):
    tag: str | None
    value: str

    def __init__(
        self,
        tag: str | None,
        value: str,
        props: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(
            tag,
            value,
            children=None,
            props=props,
        )

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value

        return super().to_html()

    @override
    def __repr__(self) -> str:
        return f"<{self.tag}{self.props}>{self.value}</{self.tag}>"
