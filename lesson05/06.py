import os

with open(__file__, mode="r", encoding="utf-8") as file:
    while (current_line_content := file.readline()) != "":
        print(current_line_content, end="")