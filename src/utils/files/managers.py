import shutil
from pathlib import Path


def copy_dir_contents(src: Path, dest: Path) -> None:
    if not src.exists():
        raise ValueError("Source static dir not found!")

    dest.mkdir(parents=True, exist_ok=True)

    for item in src.iterdir():
        target = dest / item.name

        if item.is_file():
            print(f"Copying file {item} -> {target}")
            shutil.copy2(item, target)
        elif item.is_dir():
            print(f"Copying tree {item} -> {target}")
            shutil.copytree(
                item,
                target,
                dirs_exist_ok=True,
            )


def cleanup_dir(path: Path) -> None:
    if not path.exists():
        path.mkdir()

    for item in path.iterdir():
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            cleanup_dir(item)
            item.rmdir()
