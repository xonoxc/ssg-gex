import re
from typing import List


def markdown_to_blocks(markdown: str) -> List[str]:
    markdown = markdown.strip()
    if not markdown:
        return []

    blocks = markdown.split(
        sep="\n\n",
    )

    return [re.sub(r"\n[ ]+", "\n", block.strip()) for block in blocks if block.strip()]
