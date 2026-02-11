import re
from pathlib import Path

from utils.extract_title import extract_title_h1
from utils.markdown_to_html_nodes import markdown_to_html_nodes


def generate_page(from_path: Path, template_path: Path, dest_path: Path) -> None:
    print(f"Generating pages from {from_path} to {dest_path}.....")

    markdown_content = readfile(
        from_path,
    )
    template_content = readfile(file_path=template_path)

    page_title = extract_title_h1(markdown_content)
    html_content = markdown_to_html_nodes(markdown=markdown_content).to_html()

    generated_html = inject_variables(
        content=template_content,
        context={
            "Title": page_title,
            "Content": html_content,
        },
    )

    destination_file_path = dest_path / from_path.with_suffix(".html").name
    destination_file_path.write_text(
        generated_html,
        encoding="utf-8",
    )


# varaible pattern {{ varaible }} matches the names
VARIABLE_PATTERNS = re.compile(r"\{\{\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\}\}")


def inject_variables(content: str, context: dict[str, str]) -> str:
    def replace(match):
        key = match.group(1)
        if key not in context:
            raise KeyError(f"Missing variable: {key}")
        return str(context[key])

    return VARIABLE_PATTERNS.sub(replace, content)


def readfile(file_path: Path) -> str:
    content = ""
    try:
        content = file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied.")
    except UnicodeDecodeError:
        print("Error decoding the file with UTF-8.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return content
