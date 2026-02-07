from textnode import TextNode, TextType


def main() -> None:
    new_text_node = TextNode(text="some text", text_type=TextType.PLAIN)
    print(new_text_node)


if __name__ == "__main__":
    main()
