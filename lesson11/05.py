import pandas
from matplotlib import pyplot, ticker

frame = pandas.read_csv("lesson11/data.csv", encoding="utf-8", names=["年月", "最高気温", "最低気温", "平均気温"])

x = frame["年月"]
y = frame["平均気温"]

fig, ax = pyplot.subplots()
ax.plot(x, y)
ax.xaxis.set_major_locator(ticker.MultipleLocator(12))

pyplot.rcParams["font.family"] = "Noto Sans CJK JP"
pyplot.rcParams["font.size"] = 8

pyplot.title("愛媛県松山市の平均気温", fontname="Noto Sans CJK JP")
pyplot.xlabel("年月", fontname="Noto Sans CJK JP")
pyplot.ylabel("気温 (℃)", fontname="Noto Sans CJK JP")
pyplot.plot(x, y)
pyplot.xticks(rotation = 90)
pyplot.show()