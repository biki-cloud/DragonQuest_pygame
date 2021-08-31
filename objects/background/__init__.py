import pygame

from img_handler import resize
from config import SCREEN_H, SCREEN_W


class BackGround(object):
    def __init__(self, img_path: str):
        self._img_path = img_path
        resize(self.img_path, SCREEN_H, SCREEN_W)
        self._pg_img = pygame.image.load(self.img_path)

    @property
    def img_path(self) -> str:
        return self._img_path

    @property
    def pg_img(self) -> pygame.surface:
        return self._pg_img
