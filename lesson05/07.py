from os import path

file_path = path.join(path.dirname(__file__), "myIntroduction.txt")

with open(file_path, mode="w", encoding="utf-8") as file:
    file.write("千葉工業大学情報変革科学部認知情報科学科\n")
    file.write("学生番号: 26G2083\n")
    file.write("氏名: 中村 悠登(なかむら はると)\n")