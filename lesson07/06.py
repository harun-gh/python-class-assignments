class Dog:
    def __init__(self, name="dog", age=0):
        self.name = name
        self.age = age
        self.bark = "wan wan"

    def show(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"bark: {self.bark}")

    def barking(self):
        print(f"{self.__class__}: {self.name} {self.bark}")

if __name__ == "__main__":
    data = [
        ["dog1", 3],
        ["dog2", 5],
        ["dog3", 7]
    ]

    for name, age in data:
        Dog(name, age).barking()