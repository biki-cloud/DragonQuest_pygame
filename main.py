import pygame

from config import get_config_json, get_img_path
from log import get_log
from objects.background.combat import Combat
from objects.background.glass import Glass
from objects.building.carve import Carve
from objects.creature.human import Braver
from objects.creature.monster.slime import Slime

"""
理想

braver = Braver()
witch = witch()
party = Party()
party.attend(braver, witch)

ゲームのスクリーンサイズとかもろもろの設定はjsonに記入し、initで読み込む方式にする。
game.init()

game.set_character(party or character)

game.start()

何歩か進んだら敵が出てくる。

main.pyは行数少なくしてゲームのシステム関係はsystemパッケージにかく
ゲームなので情報を保存しておいて続きからやれるようにしないといけない -> 今のところ保存方法はjsonで。
"""

SCREEN_RECT = pygame.Rect(0, 0, 640, 480)


def put_to_screen(img, x, y):
    screen.blit(img, (x, y))


def load_image(filename) -> pygame.Surface:
    image = pygame.image.load(filename)
    image = image.convert_alpha()
    return image


def get_image(sheet, x, y, width, height, use_color_key=False) -> pygame.Surface:
    image = pygame.Surface([width, height])
    image.blit(sheet, (0, 0), (x, y, width, height))
    image = image.convert_alpha()
    if use_color_key:
        color_key = image.get_at((0, 0))
        image.set_colorkey(color_key, pygame.RLEACCEL)
    # image = pygame.transform.scale(image, (32*2, 32*2))
    return image


DIR_DOWN = 0
DIR_LEFT = 1
DIR_RIGHT = 2
DIR_UP = 3
ANIME_WAIT_COUNT = 24


class Player(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        sheet = load_image(filename)
        self.images = [[], [], [], []]

        for row in range(0, 4):
            for col in [0, 1, 2, 1]:
                self.images[row].append(get_image(sheet, 0 + 32 * col, 0 + 32 * row, 32, 32, True))

        self.image = self.images[DIR_DOWN][0]
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_RECT.width // 2, SCREEN_RECT.height // 2)
        self.frame = 0
        self.anime_count = 0
        self.dir = DIR_DOWN

    def update(self):
        self.anime_count += 1
        if self.anime_count >= ANIME_WAIT_COUNT:
            self.anime_count = 0
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
        self.image = self.images[self.dir][self.frame]


class Map:
    def __init__(self, screen, filename):
        self.ncol = 20
        self.nrow = 15
        self.screen = screen
        self.map_data = []
        self.read_map(filename)
        self.sheet0 = load_image("./maptip1.png")
        self.sheet1 = load_image("./river.png")
        self.images = []
        self.images.append([self.sheet1, 0, 4])
        self.images.append([self.sheet0, 0, 0])

    def read_map(self, filename):
        with open("field01.map") as fi:
            line = fi.readline()
            self.ncol, self.nrow = [int(tok) for tok in line.split(",")]
            for row in range(self.nrow):
                line = fi.readline()
                self.map_data.append([int(tok) for tok in line.split(",")])

    def draw(self):
        for row, row_data in enumerate(self.map_data):
            for col, col_data in enumerate(row_data):
                sheet, x, y = self.images[col_data]
                screen.blit(sheet, (col * 32, row * 32), (x * 32, y * 32, 32, 32))


if __name__ == '__main__':

    config: dict = get_config_json()

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_RECT.size)
    pygame.display.set_caption('Dragon Quest Monster')

    player = Player("charecter.png")
    group = pygame.sprite.RenderUpdates()
    group.add(player)
    field_map = Map(screen, "field01.map")
    clock = pygame.time.Clock()

    log = get_log.get_logger()

    icon = pygame.image.load(get_img_path("slime.png"))
    pygame.display.set_icon(icon)

    glass = Glass()
    combat = Combat()

    carve = Carve()
    carve.x, carve.y = 150, 100

    braver = Braver('mike')
    braver.x, braver.y = 100, 100

    slime = Slime('riml')

    back_ground = glass.pg_img
    while True:
        clock.tick(60)
        screen.fill((0, 255, 0))
        field_map.draw()
        group.update()
        group.draw(screen)  # 画面にキャラが表示される
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    log.debug('key up')
                    braver.up()
                if event.key == pygame.K_DOWN:
                    log.debug('key down')
                    braver.down()
                if event.key == pygame.K_LEFT:
                    log.debug('key left')
                    braver.left()
                if event.key == pygame.K_RIGHT:
                    log.debug('key right')
                    braver.right()
                    back_ground = combat.pg_img
            log.debug(f'braver: {braver.x}, {braver.y}')
            log.debug(f'carve: {carve.x}, {carve.y}')
            if (braver.x, braver.y) == (carve.x, carve.y):
                log.debug('enter to carve!!!')
            # put_to_screen(back_ground, 0, 0)
            # put_to_screen(carve.pg_img, carve.x, carve.y)
            # put_to_screen(braver.pg_img, braver.x, braver.y)
            # put_to_screen(slime.pg_img, 500, 700)
            # put_to_screen(player, 100, 100)
            pygame.display.update()
