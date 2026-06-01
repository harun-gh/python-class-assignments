from Animal import Animal

class Cat(Animal):
    def __init__(self, name="tama", age=0)->None:
        super().__init__(name, age, "meow")

    def show(self)->None:
        print(f"Cat name: {self.name} / age: {self.age}")