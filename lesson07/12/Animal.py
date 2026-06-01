class Animal:
    onomatopoeia: str
    name: str
    age: int

    def __init__(self, name: str, age: int, onomatopoeia: str)->None:
        self.name = name
        self.age = age
        self.onomatopoeia = onomatopoeia

