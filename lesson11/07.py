import pandas
from matplotlib import pyplot, ticker

frame1 = pandas.read_csv("chiba.csv", encoding="utf-8", names=["年月", "最高気温", "最低気温", "平均気温"])
frame2 = pandas.read_csv("data.csv", encoding="utf-8", names=["年月", "最高気温", "最低気温", "平均気温"])

dataframe = pandas.merge(frame1, frame2, on="年月")
x = dataframe["年月"]
y1 = dataframe["平均気温_x"]
y2 = dataframe["平均気温_y"]

fig, ax = pyplot.subplots()
ax.plot(x, y1, label="千葉市")
ax.plot(x, y2, label="松山市")
ax.xaxis.set_major_locator(ticker.MultipleLocator(12))

pyplot.rcParams["font.family"] = "Noto Sans CJK JP"
pyplot.rcParams["font.size"] = 8

pyplot.title("千葉市と松山市の平均気温", fontname="Noto Sans CJK JP")
pyplot.xlabel("年月", fontname="Noto Sans CJK JP")
pyplot.ylabel("気温 (℃)", fontname="Noto Sans CJK JP")
pyplot.xticks(rotation = 90)
pyplot.show()