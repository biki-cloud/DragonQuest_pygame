import pygame

from handle_image import resize
from set import SCREEN_WIDTH, SCREEN_HEIGHT, BRAVER_IMG_PATH, SLIME_IMG_PATH, FIELD_IMG_PATH


def automatic_set_img_size(img_path: str, height: int, width: int, ratio: object = 5) -> None:
    h, w = (int(height / ratio), int(width / ratio))
    resize(img_path=img_path, x=h, y=w)


def put_to_screen(img, x, y):
    screen.blit(img, (x, y))


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dragon quest monster')

icon = pygame.image.load(SLIME_IMG_PATH)
pygame.display.set_icon(icon)

bg_img = pygame.image.load(FIELD_IMG_PATH)

automatic_set_img_size(BRAVER_IMG_PATH, screen.get_height(), screen.get_width())
braver_img = pygame.image.load(BRAVER_IMG_PATH)

automatic_set_img_size(SLIME_IMG_PATH, screen.get_height(), screen.get_width())
enemy_img = pygame.image.load(SLIME_IMG_PATH)

running: bool = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # i don't understand how to keypress
        if event.type == pygame.KEYDOWN:
            print('key press')
            if event.key == pygame.K_UP:
                print('KEYUP')
            if event.key == pygame.K_DOWN:
                print('KEYDOWN')
            if event.key == pygame.K_LEFT:
                print('KEYLEFT')
            if event.key == pygame.K_RIGHT:
                print('KEYRIGHT')

    put_to_screen(bg_img, 0, 0)
    put_to_screen(braver_img, 300, 400)
    put_to_screen(enemy_img, 500, 700)
    pygame.display.update()
