import pygame

from config import get_config_json, get_img_path, SCREEN_H, SCREEN_W
from log import get_log
from objects.background.combat import Combat
from objects.background.glass import Glass
from objects.building.carve import Carve
from objects.creature.human.braver import Braver
from objects.creature.monster.slime import Slime


def put_to_screen(img, x, y):
    screen.blit(img, (x, y))


if __name__ == '__main__':

    config: dict = get_config_json()

    pygame.init()
    log = get_log.get_logger()

    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

    pygame.display.set_caption('Dragon Quest Monster')

    icon = pygame.image.load(get_img_path("slime.png"))
    pygame.display.set_icon(icon)

    glass = Glass()
    combat = Combat()

    carve = Carve()
    carve.x, carve.y = 150, 100

    braver = Braver('mike')
    braver.x, braver.y = 100, 100

    slime = Slime('riml')

    is_running: bool = True
    frame_count = 0
    back_ground = glass.pg_img
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
