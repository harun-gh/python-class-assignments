from Animal import Animal

class Dog(Animal):
    def __init__(self, name="tama", age=0):
        super().__init__(name, age, "wan wan")

    def show(self)->None:
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"onomatopoeia: {self.onomatopoeia}")

    def cry(self)->None:
        print(f"{self.__class__}: {self.name} {self.onomatopoeia}")