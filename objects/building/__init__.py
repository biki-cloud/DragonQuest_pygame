from typing import Tuple

import pygame

from config import SCREEN_H, SCREEN_W
from img_handler import resize


class Building(object):
    def __init__(self, building_img_path: str):
        self._img_path = building_img_path
        resize(self.img_path, int(SCREEN_H / 10), int(SCREEN_W / 10))
        self._pg_img = pygame.image.load(self.img_path)
        self._center = self._pg_img.get_size()
        self._x = None
        self._y = None

    @property
    def img_path(self) -> str:
        return self._img_path

    @property
    def pg_img(self) -> pygame.surface:
        return self._pg_img

    @property
    def center(self) -> Tuple[float, float]:
        return self._center

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x: int):
        self._x = x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y: int):
        self._y = y
