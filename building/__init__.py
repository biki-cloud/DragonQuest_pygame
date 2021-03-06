import pygame

from handle_image import resize


class Building(object):
    def __init__(self, building_img_path: str, screen_h: int, screen_w: int):
        self.img_path = building_img_path
        resize(self.img_path, int(screen_h / 10), int(screen_w / 10))
        self.pg_img = pygame.image.load(self.img_path)
