import pygame

from handle_image import automatic_set_img_size


class Character(object):
    def __init__(self, name: str, img_path: str, screen_h: int, screen_w: int) -> object:
        self.name = name
        self._img_path = img_path
        automatic_set_img_size(img_path, screen_h, screen_w)
        self.pg_img = pygame.image.load(img_path)
