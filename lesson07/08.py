from importlib import import_module

Dog = import_module("06").Dog

class DogKai(Dog):
    def __init__(self, name="dog", age=0):
        self.name = name
        self.age = age
        self.bark = "bow"

data = [
    ["dog1", 3],
    ["dog2", 5],
    ["dog3", 7]
]

for name, age in data:
    dog = DogKai(name, age)

    dog.show()
    dog.barking()