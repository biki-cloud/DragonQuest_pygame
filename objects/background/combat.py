from config import get_img_path
from objects.background import BackGround


class Combat(BackGround):
    def __init__(self):
        img_path = get_img_path("combat1.jpg")
        super().__init__(img_path)
