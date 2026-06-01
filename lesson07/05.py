class Cat:
    def __init__(self, name="tama", age=0):
        self.name = name
        self.age = age

    def show(self):
        print(f"Cat name: {self.name} / age: {self.age}")

Cat().show()
Cat("tomato", 4).show()
Cat("banana", 2).show()
Cat("makura", 6).show()
