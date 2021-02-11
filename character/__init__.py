from typing import Tuple

import pygame

from handle_image import automatic_set_img_size


class Character(object):
    def __init__(self, name: str, img_path: str, screen_h: int, screen_w: int):
        self._name = name
        self._img_path = img_path
        automatic_set_img_size(img_path, screen_h, screen_w)
        self._pg_img = pygame.image.load(img_path)
        self._center = self.pg_img.get_size()

    @property
    def center(self) -> Tuple[float, float]:
        return self._center

    @property
    def pg_img(self) -> pygame.surface:
        return self._pg_img

    @property
    def img_path(self) -> str:
        return self._img_path

    @property
    def name(self) -> str:
        return self._name
