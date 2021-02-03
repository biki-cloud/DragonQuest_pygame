class Monster:
    def __init__(self, name):
        self.name = name


class Slime(Monster):
    def __init__(self, name):
        super().__init__(name)
