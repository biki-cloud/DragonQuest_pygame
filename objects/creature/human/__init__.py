from config import get_img_path
from objects.creature import Creature


class Braver(Creature):
    def __init__(self, name: str, x: int = None, y: int = None,
                 stride: int = None):
        img_path = get_img_path("braver.png")
        super().__init__(name, img_path, x, y, stride)


class Witch(Creature):
    def __init__(self, name: str, x: int = None, y: int = None,
                 stride: int = None):
        img_path = get_img_path("braver.png")
        super().__init__(name, img_path, x, y, stride)
