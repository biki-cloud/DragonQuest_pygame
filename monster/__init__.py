from character import Character

class Slime(Character):
    def __init__(self, name, img_path, screen_h, screen_w):
        super().__init__(name, img_path, screen_h, screen_w)
        self.monster_rank = 1
