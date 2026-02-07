from typing import List, Dict


class HTMLNode:
    tag: str | None
    value: str | None
    children: List["HTMLNode"] | None
    props: Dict[str, str] | None

    # constrcutor
    def __init__(
        self,
        tag: str | None,
        value: str | None,
        children: List["HTMLNode"] | None,
        props: Dict[str, str] | None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # to html convers the tag to html string, if the tag is None,
    # it returns the value,
    # otherwise it returns the tag with the children and props
    def to_html(self) -> str:
        if self.tag is None:
            return self.value or ""

        props_str = ""
        if self.props:
            props_str = self.stringified_props()

        children_str = ""
        if self.children:
            children_str = self.stringified_children()

        # Include value if it exists, after children
        content_str = children_str
        if self.value:
            content_str += self.value

        return self.to_string_rep(
            props_str,
            content_str,
        )

    # helper method to convert props dict to string
    def stringified_props(self) -> str:
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def stringified_children(self) -> str:
        if not self.children:
            return ""
        return "".join(child.to_html() for child in self.children)

    # return final tag string reperation
    def to_string_rep(
        self,
        props_str: str,
        children_str: str,
    ) -> str:
        return f"<{self.tag}{props_str}>{children_str}</{self.tag}>"

    # string representation of the node, for debugging purposes
    def __repr__(self) -> str:
        return self.to_string_rep(
            props_str=self.stringified_props(), children_str=self.stringified_children()
        )
