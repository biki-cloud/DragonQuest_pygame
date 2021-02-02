class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Braver(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
