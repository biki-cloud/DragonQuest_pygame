from PIL import Image


def resize(img_path: str, x: int, y: int) -> None:
    img = Image.open(img_path)
    img_resize = img.resize((x, y))
    img_resize.save(img_path)


def automatic_set_img_size(img_path: str, height: int, width: int, ratio: int = 5) -> None:
    h, w = (int(height / ratio), int(width / ratio))
    resize(img_path=img_path, x=h, y=w)
