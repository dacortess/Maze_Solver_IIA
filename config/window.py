import pygame, os

class Window():

    def __init__(self):
        self.width, self.height = 800, 600
        self.caption = "Maze Solver"
        self.fps = 60
        self.background = self.set_background()
        self.window = pygame.display.set_mode((self.width, self.height))

    def start(self):
        pygame.display.set_caption(self.caption)
        image = pygame.image.load(os.path.join('.\src\img', 'icon.jpg'))
        return pygame.display.set_icon(image)

    def set_caption(self, caption):
        self.caption = caption

    def set_background(self):
        image = pygame.image.load(os.path.join('.\src\img', 'bg_ex.png'))

        bg = pygame.transform.scale(image, (800, 600))

        return bg

    def blit(self, object, coordinates):
        self.window.blit(object, coordinates)