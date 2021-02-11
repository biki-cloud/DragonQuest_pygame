import pygame

from handle_image import resize


class Building(object):
    def __init__(self, building_img_path: str, screen_h: int, screen_w: int):
        self._img_path = building_img_path
        resize(self.img_path, int(screen_h / 10), int(screen_w / 10))
        self._pg_img = pygame.image.load(self.img_path)

    @property
    def img_path(self) -> str:
        return self._img_path

    @property
    def pg_img(self) -> pygame.surface:
        return self._pg_img
