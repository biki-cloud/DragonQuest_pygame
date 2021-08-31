import pygame

from img_handler import automatic_set_img_size
from config import SCREEN_H, SCREEN_W


class Creature(object):
    """
    生き物の親クラス
    """
    def __init__(self, name: str, img_path: str, x: int = None, y: int = None,
                 stride: int = None):
        """
        :param name:
        :param img_path:
        :param x:
        :param y:
        :param stride:
        """
        self._name = name
        self._img_path = img_path
        automatic_set_img_size(img_path, SCREEN_H, SCREEN_W)
        self._pg_img = pygame.image.load(img_path)
        self._stride = stride if stride is not None else 20
        self._x = x if x is not None else (SCREEN_W / 2)
        self._y = y if y is not None else (SCREEN_H / 2)

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
