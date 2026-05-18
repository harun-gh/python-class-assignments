import os
print(f"python's current working directry: {os.getcwd()}")

print(f"the file's full path: {__file__}")

filename = os.path.basename(__file__)
print(f"filename: {filename}")

dirname = os.path.dirname(__file__)
print(f"dirname: {dirname}")

print(f"join() usage correct: {os.path.join(dirname, filename) == __file__}")