import tkinter as tk
from itertools import product

width = 640
height = 480
pixel_size = 4

calc_threshold = 100

root = tk.Tk()

canvas = tk.Canvas(root, width=width, height=height, bg="black")
canvas.pack()

for _x, _y in product(range(0, width, pixel_size), range(0, height, pixel_size)):
    cx = (_x - width / 2) * pixel_size / width
    cy = (_y - height / 2) * pixel_size / width

    zx = 0
    zy = 0

    # https://asanobuturi.github.io/blog/20220508/#入力された複素数がマンデルブロ集合に含まれるかどうかを判定する関数
    for iteration_count in range(calc_threshold):
        (zy, zx) = (2*zx*zy + cy, zx*zx - zy*zy + cx)

        if zx*zx + zy*zy > 4:
            ### なんでpythonには、labeled loopがないの...zigにあるのに...
            # color = "black"
            # continue
            break

    if iteration_count == calc_threshold - 1:
        color = "black"
    else:
        brightness = int(255 * iteration_count / 50)
        color = f"#{brightness:02x}{brightness:02x}{brightness:02x}" # python黒魔術多すぎ

    canvas.create_rectangle(
        _x,
        _y,
        _x + 4,
        _y + 4,
        fill=color,
        outline=color
    )

root.mainloop()