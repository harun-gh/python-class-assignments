from matplotlib import pyplot
from numpy import arange, cos, tan

x = arange(-10, 10, 0.01)

y1 = cos(x)
y2 = tan(x)

pyplot.rcParams["font.family"] = "Noto Sans CJK JP"
pyplot.rcParams["font.size"] = 12

pyplot.figure()

pyplot.title("三角関数の描写")
pyplot.xlabel("ラジアン")
pyplot.ylabel("cos(β), tan(β)")
pyplot.grid(True)

pyplot.plot(x, y1, label="cos")
pyplot.plot(x, y2, label="tan")

pyplot.legend(title="三角関数", loc="upper left")
pyplot.show()