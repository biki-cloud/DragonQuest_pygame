import pygame

from handle_image import resize


class BackGround(object):
    def __init__(self, img_path: str, screen_h: int, screen_w: int):
        self._img_path = img_path
        resize(self.img_path, screen_h, screen_w)
        self._pg_img = pygame.image.load(self.img_path)

    @property
    def img_path(self) -> str:
        return self._img_path

    @property
    def pg_img(self) -> pygame.surface:
        return self._pg_img
