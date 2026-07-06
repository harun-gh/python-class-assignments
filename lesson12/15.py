import os
from matplotlib import pyplot
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
        except UnicodeDecodeError:
            print("Could not decode using the specified character encoding.")
    else:
        print("file does not exit")

    return dictionary

def add_pref(arg: dict, pref: str) -> None:
    try:
        n = arg[pref] + 1
        arg[pref] = n
    except KeyError:
        arg[pref] = 1

    return

def make_bar_graph(arg: dict) -> None:
    pyplot.rcParams["font.family"] = "Noto Sans CJK JP"
    pyplot.rcParams["font.size"] = 8

    pyplot.title("出身地の数")
    pyplot.xlabel("出身地", loc="left", rotation=0)
    pyplot.ylabel("人数", loc="top", rotation=0)
    pyplot.xticks(rotation=90)

    x: list[str] = []
    y: list[int] = []

    for key, value in arg.items():
        x.append(key)
        y.append(value)

    pyplot.bar(x, y)
    pyplot.show()

    print(arg)

def replace_key(arg: dict, source: str, destination: str) -> None:
    arg[destination] = arg.pop(source)

def main():
    path = Path(os.path.dirname(__file__), file_path)
    dictionary = read_file(path)
    replace_key(dictionary, "千葉県（千葉市、船橋市、松戸市、市川市、柏市以外）", "千葉県")
    make_bar_graph(dictionary)
    print("make graph")

if __name__ == "__main__":
    main()