from nodes.htmlnode import HTMLNode
from typing import List, Dict


class ParentNode(HTMLNode):
    # constrcutor
    def __init__(
        self,
        tag: str,
        children: List["HTMLNode"],
        props: Dict[str, str] | None = None,
    ) -> None:
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")

        if self.children is None:
            raise ValueError("ParentNode must have children")

        if self.tag is None:
            return self.value or ""

        props_str = ""
        if self.props:
            props_str = self.stringified_props()

        children_str = ""
        if self.children:
            children_str = self.stringified_children()

        return self.to_string_rep(
            props_str,
            children_str,
        )
