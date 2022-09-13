import pygame
from config.window import Window

class Game():
    def __init__(self):
        self.window = Window()
        self.clock = pygame.time.Clock()
        self.is_runnig = True
    
    def start_game(self):
        self.window.start()
        self.main()

    def main(self):
        
        while self.is_runnig:

            self.clock.tick(self.window.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_runnig = False