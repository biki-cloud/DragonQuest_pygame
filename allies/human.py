from creature.character import Character


class Braver(Character):
    def __init__(self, name, img_path, screen_h, screen_w, x: int = None, y: int = None, stride: int = None):
        super().__init__(name, img_path, screen_h, screen_w)
        self._stride = stride if stride is not None else 20
        self._x = x if x is not None else (screen_w / 2)
        self._y = y if y is not None else (screen_h / 2)

    def up(self):
        self._y -= self._stride

    def down(self):
        self._y += self._stride

    def left(self):
        self._x -= self._stride

    def right(self):
        self._x += self._stride

    @property
    def stride(self) -> float:
        return self._stride

    @stride.setter
    def stride(self, stride: int) -> None:
        self._stride = stride

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
