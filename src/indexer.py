from pathlib import Path
from typing import List

def chunk_python(content: str, max_chunk_size: int = 2000) -> List[str]:
    pass

def chunk_mark_down(content: str, max_chunk_size: int = 2000) -> List[str]:
    print(content)
    return content


def main() -> None:

    root_path = Path("data/raw/")
    py_files : List = list(root_path.rglob("*.py"))
    md_files : List = list(root_path.rglob("*.md"))

    for i in range(3):
        content = md_files[i].read_text(encoding="utf-8")
        chunk_mark_down(content)

if __name__ == "__main__":
    main()
