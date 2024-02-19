import pygame
class Screen:
    def __init__(self):
        self.piksel = 16
        self.screen = pygame.display.set_mode((32 * self.piksel, 32 * self.piksel))

    def draw_mario(self, x, y):
        y -= 2
        r = pygame.Rect(x * self.piksel, y * self.piksel, self.piksel, 3 * self.piksel)
        pygame.draw.rect(self.screen, (255, 0, 0), r, 0)
