from importlib import import_module

Dog = import_module("06").Dog

class DogShibainu(Dog):
    def __init__(self, name="dog", age=0):
        self.name = name
        self.age = age
        self.bark = "growl"

dog = DogShibainu("むぎ", 3)

dog.show()
dog.barking()