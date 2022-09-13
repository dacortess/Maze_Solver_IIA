import pygame, os

class Window():

    def __init__(self):
        self.width, self.height = 400, 600
        self.caption = "Maiz Solver"
        self.fps = 60
        #self.background = self.set_background()
        self.window = pygame.display.set_mode((self.width, self.height))

    def start(self):
        pygame.display.set_caption(self.caption)
        #image = pygame.image.load(os.path.join('.\src\images', 'icon.png'))
        #return pygame.display.set_icon(image)

'''
    def set_background(self):
        image = pygame.image.load(os.path.join('.\src\images', 'space.png'))

        bg = pygame.transform.rotate(pygame.transform.scale(
        image, (400, 600)), 0)

        return bg
    
    def blit(self, object, coordinates):
        self.window.blit(object, coordinates)
'''