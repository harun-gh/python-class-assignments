import os
from pathlib import Path

file_path = "hometown.csv"

def read_file(path: Path) -> dict:
    dictionary: dict[str, int] = {}

    if path.is_file():
        try:
            with open(path, "r", encoding="shift_jis") as data:
                for line in data:
                    add_pref(dictionary, line.strip())
        except AttributeError:
            print(f"Can't read {path}!")
    else:
        print("file does not exit")
    return {}

def add_pref(arg: dict, pref: str) -> None:
    try:
        n = arg[pref] + 1
        arg[pref] = n
    except KeyError:
        arg[pref] = 1

    return

def main():
    path = Path(os.path.dirname(__file__), file_path)
    read_file(path)
    print("make graph")

if __name__ == "__main__":
    main()