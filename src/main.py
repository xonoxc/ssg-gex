from build import setup_static_content, build


def main() -> None:
    setup_static_content()
    build()


if __name__ == "__main__":
    main()
