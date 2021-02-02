import pygame
from handle_image import resize
import os


def automatic_set_img_size(img_path: str, screen):
    ratio = 5
    h, w = int(screen.get_height() / ratio), int(screen.get_width() / ratio)
    resize(img_path=img_path, x=h, y=w)


pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Dragon quest monster')
icon = pygame.image.load(os.path.join('monster', 'slime.png'))
pygame.display.set_icon(icon)

bg = pygame.image.load(os.path.join('field', 'field1.jpg'))

braver_img_path = os.path.join('human', 'braver.png')
automatic_set_img_size(braver_img_path, screen)
player_img = pygame.image.load(braver_img_path)

slime_img_path = os.path.join('monster', 'slime.png')
automatic_set_img_size(slime_img_path, screen)
enemy_img = pygame.image.load(slime_img_path)


def object_put_to_screen(img, x, y):
    screen.blit(img, (x, y))


running: bool = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # i don't understand how to keypress
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP:
                print('KEYUP')
            if event.type == pygame.K_DOWN:
                print('KEYDOWN')
            if event.type == pygame.K_LEFT:
                print('KEYLEFT')
            if event.type == pygame.K_RIGHT:
                print('KEYRIGHT')

    object_put_to_screen(bg, 0, 0)
    object_put_to_screen(player_img, 300, 400)
    object_put_to_screen(enemy_img, 500, 700)
    pygame.display.update()
