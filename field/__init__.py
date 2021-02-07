from handle_image import resize
import pygame

class BackGround(object):
    def __init__(self, img_path: str, screen_h: int, screen_w: int):
        self.img_path = img_path
        resize(self.img_path, screen_h, screen_w)
        self.pg_img = pygame.image.load(self.img_path)
