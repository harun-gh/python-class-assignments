import pandas
from matplotlib import pyplot, ticker

frame = pandas.read_csv("chiba.csv", encoding="utf-8", names=["年月", "最高気温", "最低気温", "平均気温"])

x = frame["年月"]
y1 = frame["最低気温"]
y2 = frame["最高気温"]

fig, ax = pyplot.subplots()
ax.plot(x, y1, label="最低気温")
ax.plot(x, y2, label="最高気温")
ax.xaxis.set_major_locator(ticker.MultipleLocator(12))

pyplot.rcParams["font.family"] = "Noto Sans CJK JP"
pyplot.rcParams["font.size"] = 8

pyplot.title("千葉県の最高気温と最低気温", fontname="Noto Sans CJK JP")
pyplot.xlabel("年月", fontname="Noto Sans CJK JP")
pyplot.ylabel("気温 (℃)", fontname="Noto Sans CJK JP")
pyplot.xticks(rotation = 90)
pyplot.show()