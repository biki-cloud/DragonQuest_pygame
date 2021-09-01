from config import get_img_path
from objects.building import Building


class Carve(Building):
    def __init__(self):
        img_path = get_img_path("carve.jpg")
        super().__init__(img_path)
