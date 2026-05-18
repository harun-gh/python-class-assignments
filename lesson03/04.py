import os

def show_file(path):
    try:
        if os.path.isfile(path):
            print(path)
        elif os.path.isdir(path):
            dir = sorted(os.listdir(path))

            for file in dir:
                show_file(os.path.join(path, file))

    except PermissionError:
        return

show_file("/home/haruto/")