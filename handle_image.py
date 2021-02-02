from PIL import Image


def resize(img_path: str, x: int, y: int) -> None:
    img = Image.open(img_path)
    img_resize = img.resize((x, y))
    img_resize.save(img_path)
