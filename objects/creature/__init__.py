import pygame

from config import SCREEN_H, SCREEN_W
from img_handler import automatic_set_img_size


class Creature(object):
    """
    生き物の親クラス
    子クラスにhumanやmonsterがある。
    """

    def __init__(self, name: str, img_path: str, x: int = None, y: int = None,
                 stride: int = None):
        """
        :param name: 生き物の名前
        :param img_path: 画像のパス
        :param x: スクリーンのどの場所に配置するか
        :param y: スクリーンのどの場所に配置するか
        :param stride: 動く場合の一歩の大きさ
        """
        self._name = name
        self._img_path = img_path
        automatic_set_img_size(img_path, SCREEN_H, SCREEN_W)
        self._pg_img = pygame.image.load(img_path)
        self._stride = stride if stride is not None else 20
        self._x = x if x is not None else (SCREEN_W / 2)
        self._y = y if y is not None else (SCREEN_H / 2)

    """
    up, down, left, right関数は呼び出すとキャラクターが動く。
    """

    def up(self) -> None:
        self._y -= self._stride

    def down(self) -> None:
        self._y += self._stride

    def left(self) -> None:
        self._x -= self._stride

    def right(self) -> None:
        self._x += self._stride

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def pg_img(self) -> pygame.surface:
        return self._pg_img

    @property
    def img_path(self) -> str:
        return self._img_path

    @property
    def name(self) -> str:
        return self._name
