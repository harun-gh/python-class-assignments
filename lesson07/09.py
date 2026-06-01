from importlib import import_module

Dog = import_module("06").Dog

class DogGermanShepherd(Dog):
    def __init__(self, name="dog", age=0):
        self.name = name
        self.age = age
        self.bark = "wow wow"

data = [
    DogGermanShepherd("dog1", 3),
    DogGermanShepherd("dog2", 5),
    Dog("dog3", 7)
]

for dog in data:
    dog.show()
    dog.barking()