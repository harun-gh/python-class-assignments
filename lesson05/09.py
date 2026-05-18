from os import path

file_path = path.join(path.dirname(__file__), "hello.txt")

try:
    with open(file_path, mode="x", encoding="utf-8") as file:
        file.write("Hello, World!")

except FileExistsError:
    print("ファイルが存在してします。内容は以下の通りです")

    with open(file_path, mode="r", encoding="utf-8") as file:
        print(file.read())
