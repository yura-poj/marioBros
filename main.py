import pygame
import sys



piksel = 16;

pygame.init()

screen = pygame.display.set_mode((32*piksel, 32*piksel))

def draw_mario(x,y):
    r = pygame.Rect(x * piksel, (y-2) * piksel, piksel, 3*piksel)
    pygame.draw.rect(screen, (255, 0, 0), r, 0)


draw_mario(0,31)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()