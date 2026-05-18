from os import path

file_path = path.join(path.dirname(__file__), "myNewFile.txt")

try:
    with open(file_path, mode="x",encoding="utf-8") as file:
        file.write("新規ファイル\n情報変革科学部\n")
except FileExistsError as e:
    print(e)
    print("既にファイルが存在しています")