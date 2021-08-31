from objects.creature import Creature
from config import get_img_path

class Slime(Creature):
    def __init__(self, name: str, x: int = None, y: int = None,
                 stride: int = None):
        img_path = get_img_path("slime.png")
        super().__init__(name, img_path, x, y, stride)
        self._monster_rank = 1
        self._attack = 1

    @property
    def monster_rank(self):
        return self._monster_rank

    @monster_rank.setter
    def monster_rank(self, rank: int):
        self._monster_rank = rank

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, attack: int):
        self._attack = attack
