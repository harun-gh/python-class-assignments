import os
from pathlib import Path

file_path = "hometown.csv"

def read_file(path: Path) -> dict:
    if path.is_file():
        try:
            with open(path, "r", encoding="shift_jis") as data:
                for line in data:
                    print(line)
        except AttributeError:
            print(f"Can't read {path}!")
    else:
        print("file does not exit")
    return {}

def main():
    path = Path(os.path.dirname(__file__), file_path)
    read_file(path)
    print("make graph")

if __name__ == "__main__":
    main()