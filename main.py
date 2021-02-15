import pygame

from building import Building
from field import BackGround
from human import Braver
from log import get_log
from monster import Slime
from set import SCREEN_WIDTH, SCREEN_HEIGHT, BRAVER_IMG_PATH, SLIME_IMG_PATH, FIELD_IMG_PATH, COMBAT_IMG_PATH, \
    CARVE_IMG_PATH


def put_to_screen(img, x, y):
    screen.blit(img, (x, y))


if __name__ == '__main__':

    pygame.init()
    log = get_log.get_logger()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Dragon Quest Monster')

    icon = pygame.image.load(SLIME_IMG_PATH)
    pygame.display.set_icon(icon)

    field = BackGround(FIELD_IMG_PATH, screen.get_height(), screen.get_width())
    combat = BackGround(COMBAT_IMG_PATH, screen.get_height(), screen.get_width())

    carve = Building(CARVE_IMG_PATH, screen.get_height(), screen.get_width())
    carve.x, carve.y = 150, 100

    braver = Braver('mike', BRAVER_IMG_PATH, screen.get_height(), screen.get_width())

    slime = Slime('riml', SLIME_IMG_PATH, screen.get_height(), screen.get_width())

    is_running: bool = True
    frame_count = 0
    back_ground = field.pg_img
    while is_running:
        # log.debug(f'frame count: {frame_count}')
        screen.fill((0, 0, 0))
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
            put_to_screen(back_ground, 0, 0)
            put_to_screen(carve.pg_img, carve.x, carve.y)
            put_to_screen(braver.pg_img, braver.x, braver.y)
            put_to_screen(slime.pg_img, 500, 700)
            pygame.display.update()
        frame_count += 1
