import pygame
import sys



piksel = 16;

pygame.init()

screen = pygame.display.set_mode((32*piksel, 32*piksel))

def draw_mario(x,y):
    r = pygame.Rect(x * piksel, (y-2) * piksel, piksel, 3*piksel)
    pygame.draw.rect(screen, (255, 0, 0), r, 0)

mario_x = 0
mario_y = 31

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mario_x -= 1
            elif event.key == pygame.K_RIGHT:
                mario_x += 1
    screen.fill((0, 0, 0))
    draw_mario(mario_x, mario_y)
    pygame.display.flip()