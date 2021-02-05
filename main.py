import pygame

from allies.human import Braver
from enemy.monster import Slime
from field.background import BackGround
from log import get_log
from set import SCREEN_WIDTH, SCREEN_HEIGHT, BRAVER_IMG_PATH, SLIME_IMG_PATH, FIELD_IMG_PATH, COMBAT_IMG_PATH


def put_to_screen(img, x, y):
    screen.blit(img, (x, y))


if __name__ == '__main__':

    pygame.init()
    logging = get_log.get_logger()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Dragon quest monster')

    icon = pygame.image.load(SLIME_IMG_PATH)
    pygame.display.set_icon(icon)

    field = BackGround(FIELD_IMG_PATH, screen.get_height(), screen.get_width())

    combat = BackGround(COMBAT_IMG_PATH, screen.get_height(), screen.get_width())

    braver = Braver('mike', BRAVER_IMG_PATH, screen.get_height(), screen.get_width())

    slime = Slime('kororo', SLIME_IMG_PATH, screen.get_height(), screen.get_width())

    is_running: bool = True
    while is_running:
        screen.fill((0, 0, 0))
        back_ground = field.pg_img
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    logging.debug('key up')
                    braver.up()
                if event.key == pygame.K_DOWN:
                    logging.debug('key down')
                    braver.down()
                if event.key == pygame.K_LEFT:
                    logging.debug('key left')
                    braver.left()
                if event.key == pygame.K_RIGHT:
                    logging.debug('key right')
                    braver.right()
                    back_ground = combat.pg_img

            put_to_screen(back_ground, 0, 0)
            put_to_screen(braver.pg_img, braver.x, braver.y)
            put_to_screen(slime.pg_img, 500, 700)
            pygame.display.update()
