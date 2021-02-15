from pygame_object import PygameObject


class Braver(PygameObject):
    def __init__(self, name: str, img_path: str, screen_h: int, screen_w: int, x: int = None, y: int = None,
                 stride: int = None):
        super().__init__(name, img_path, screen_h, screen_w, x, y, stride)
