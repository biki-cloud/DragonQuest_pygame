from creature.character import Character


class Braver(Character):
    def __init__(self, name, img_path, screen_h, screen_w):
        super().__init__(name, img_path, screen_h, screen_w)
        self.stride = 0.5
