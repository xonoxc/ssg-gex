from generators.page_gen import generate_page
from utils.files.managers import cleanup_dir, copy_dir_contents

from constants import (
    CONTENT_DIR_PATH,
    DEST_STATIC_DIR_PATH,
    SOURCE_STATIC_DIR_PATH,
    TEMPLATE_FILE_PATH,
)


def build() -> None:
    print("setting up static assets")

    print("Initializing build......")
    generate_page(
        from_path=CONTENT_DIR_PATH / "index.md",
        template_path=TEMPLATE_FILE_PATH,
        dest_path=DEST_STATIC_DIR_PATH,
    )
    print("Build successfull!!")


def setup_static_content() -> None:
    cleanup_dir(
        DEST_STATIC_DIR_PATH,
    )
    copy_dir_contents(src=SOURCE_STATIC_DIR_PATH, dest=DEST_STATIC_DIR_PATH)
