import pygame

pygame.font.init()

class Font():
    def __init__(self):
        self.tilte = pygame.font.SysFont('comicsans', 80)
        self.subtitle = pygame.font.SysFont('comicsans', 40)
        self.text = pygame.font.SysFont('comicsans', 30)
        self.info = pygame.font.SysFont('comicsans', 20)

    def get_font(self, size):
        return pygame.font.SysFont('comicsans', size)