from pandas import DataFrame, read_csv
from matplotlib import pyplot
from os import path

file_path = path.join(path.dirname(__file__), "c03.csv")
prefs = ["島根県", "広島県", "東京都"]

pyplot.rcParams["font.family"] = "Noto Sans CJK JP"
pyplot.rcParams["font.size"] = 8

pyplot.title("指定された都道府県の人口", fontname="Noto Sans CJK JP")

def get_population(pref: str)->DataFrame:
    frame: DataFrame

    with open(file_path, encoding="CP932") as f:
        population = read_csv(f, encoding="CP932")

        frame = population.query(f"都道府県名=='{pref}' and 年齢5歳階級 == '総数'")
        frame = frame.filter(items=["西暦（年）", "人口（総数）"])
        frame["西暦（年）"] = frame["西暦（年）"].astype("int")
        frame["人口（総数）"] = frame["人口（総数）"].astype("int")

    return frame

def main():
    for pref in prefs:
        frame = get_population(pref)

        pyplot.plot(
            frame["西暦（年）"],
            frame["人口（総数）"],
            label=pref
        )

    pyplot.xlabel("年")
    pyplot.ylabel("人口")
    pyplot.xticks(rotation = 90)
    pyplot.legend()
    pyplot.show()

if __name__ == "__main__":
    main()