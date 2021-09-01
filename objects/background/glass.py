from config import get_img_path
from objects.background import BackGround


class Glass(BackGround):
    def __init__(self):
        img_path = get_img_path("field1.jpg")
        super().__init__(img_path)
