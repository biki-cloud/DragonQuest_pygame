import pygame

from handle_image import automatic_set_img_size


class PygameObject(object):
    def __init__(self, name: str, img_path: str, screen_h: int, screen_w: int, x: int = None, y: int = None,
                 stride: int = None):
        self._name = name
        self._img_path = img_path
        automatic_set_img_size(img_path, screen_h, screen_w)
        self._pg_img = pygame.image.load(img_path)
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

    @property
    def pg_img(self) -> pygame.surface:
        return self._pg_img

    @property
    def img_path(self) -> str:
        return self._img_path

    @property
    def name(self) -> str:
        return self._name
