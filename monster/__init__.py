from pygame_object import PygameObject


class Slime(PygameObject):
    def __init__(self, name: str, img_path: str, screen_h: int, screen_w: int, x: int = None, y: int = None,
                 stride: int = None):
        super().__init__(name, img_path, screen_h, screen_w, x, y, stride)
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
