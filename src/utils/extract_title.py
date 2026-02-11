# this function take the markdown files and extract the title from it, the title is the first line that starts with "# "
def extract_title_h1(markdown: str) -> str:
    markdownlines = markdown.strip().splitlines()

    for line in markdownlines:
        if line.startswith("# "):
            return line.strip("#").strip()

    raise FileNotFoundError("title string not found")
