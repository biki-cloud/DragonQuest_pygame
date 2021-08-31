from PIL import Image


def resize(img_path: str, x: int, y: int) -> None:
    """
    画像のサイズを変更し保存する。

    :param img_path: 画像のパス
    :param x: 縦のサイズ
    :param y: 横のサイズ
    :return:
    """
    img = Image.open(img_path)
    img_resize = img.resize((x, y))
    img_resize.save(img_path)


def automatic_set_img_size(img_path: str, height: int, width: int, ratio: int = 5) -> None:
    """
    自動でいい感じの大きさで画像を保存する。

    :param img_path: 画像のパス
    :param height: 画像の高さ
    :param width: 画像の広さ
    :param ratio: 等倍
    :return:
    """
    h, w = (int(height / ratio), int(width / ratio))
    resize(img_path=img_path, x=h, y=w)
