from utils.files.managers import cleanup_dir, copy_dir_contents
from constants import DEST_STATIC_DIR_PATH, SOURCE_STATIC_DIR_PATH


def main() -> None:
    cleanup_dir(
        DEST_STATIC_DIR_PATH,
    )
    copy_dir_contents(src=SOURCE_STATIC_DIR_PATH, dest=DEST_STATIC_DIR_PATH)


if __name__ == "__main__":
    main()
