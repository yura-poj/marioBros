import pygame
from mario import Mario
from screen import Screen
import sys

pygame.init()

screen = Screen()
mario = Mario()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mario.move_left = True
            if event.key == pygame.K_RIGHT:
                mario.move_right = True
            if event.key == pygame.K_SPACE and mario.access_to_jump:
                mario.jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mario.move_left = False
            if event.key == pygame.K_RIGHT:
                mario.move_right = False
    mario.update()
    screen.screen.fill((0, 0, 0))
    screen.draw_mario(mario.x_cordinat, mario.y_cordinat)
    pygame.display.flip()