import sys
import pygame
from config.window import Window
from components.button import Button
from components.font import Font
from components.logic import Logic
from components import utils

class Game():
    def __init__(self):
        self.window = Window()
        self.clock = pygame.time.Clock()
        self.font = Font()
        self.logic = Logic()
        self.step = 0
    
    def start_game(self):
        self.window.start()
        self.main()
    
    def increase_step(self):
        self.step += 1

    def decrease_step(self):
        self.step -= 1

    def main(self):

        while self.step >= 0:

            self.window.blit(self.window.background, (0,0))

            MOUSE = pygame.mouse.get_pos()

            TITLE_TEXT = self.font.tilte.render("MAZE SOLVER", True, "Black")
            TITLE_RECT = TITLE_TEXT.get_rect(center=(400,100))

            self.window.blit(TITLE_TEXT, TITLE_RECT)

            SELECT_MAZE = Button(image=None, pos=(200,395),
                                    text_input="Select Maze", font=self.font.subtitle, 
                                    base_color="#000000", hovering_color="#FFFFFF")

            UPLOAD_MAZE = Button(image=None, pos=(600,395),
                                    text_input="Upload Maze", font=self.font.subtitle, 
                                    base_color="#000000", hovering_color="#FFFFFF")

            for button in [SELECT_MAZE, UPLOAD_MAZE]:
                button.change_color(MOUSE)
                button.update(self.window)

            self.clock.tick(self.window.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.step == 0:
                    if SELECT_MAZE.input_check(MOUSE):
                        self.select_maze()
                    if UPLOAD_MAZE.input_check(MOUSE):
                        self.upload_maze()
                    
            pygame.display.update()
    
    def select_maze(self):
        from os.path import abspath

        self.increase_step()

        while self.step >= 1:

            self.window.blit(self.window.background, (0,0))

            MOUSE = pygame.mouse.get_pos()

            TITLE_TEXT = self.font.tilte.render("MAZE SOLVER", True, "Black")
            TITLE_RECT = TITLE_TEXT.get_rect(center=(400,100))

            self.window.blit(TITLE_TEXT, TITLE_RECT)

            INFO_TEXT = self.font.info.render("Select the maze to evaluate", True, "Black")
            INFO_RECT = INFO_TEXT.get_rect(center=(400,200))

            self.window.blit(INFO_TEXT, INFO_RECT)

            MAZE_5X5 = Button(image=None, pos=(200,285),
                            text_input="Maze 5x5", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")

            MAZE_10X10 = Button(image=None, pos=(200,345),
                            text_input="Maze 10x10", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")

            MAZE_50X50 = Button(image=None, pos=(200,405),
                            text_input="Maze 50x50", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")

            MAZE_100X100 = Button(image=None, pos=(600,320),
                            text_input="Maze 100x100", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")

            MAZE_400X400 = Button(image=None, pos=(600,380),
                            text_input="Maze 400x400", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")
            
            BACK_BTN = Button(image=None, pos=(40,580),
                            text_input="Back", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")
            
            for button in [MAZE_5X5, MAZE_10X10, MAZE_50X50, MAZE_100X100, MAZE_400X400, BACK_BTN]:
                button.change_color(MOUSE)
                button.update(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.step == 1:
                    if MAZE_5X5.input_check(MOUSE):
                        self.logic.set_maze(abspath('./logic/files/maze_5x5.csv'))
                        self.select_algorithm()
                    if MAZE_10X10.input_check(MOUSE):
                        self.logic.set_maze(abspath('./logic/files/maze_10x10.csv'))
                        self.select_algorithm()
                    if MAZE_50X50.input_check(MOUSE):
                        self.logic.set_maze(abspath('./logic/files/maze_50x50.csv'))
                        self.select_algorithm()
                    if MAZE_100X100.input_check(MOUSE):
                        self.logic.set_maze(abspath('./logic/files/maze_100x100.csv'))
                        self.select_algorithm()
                    if MAZE_400X400.input_check(MOUSE):
                        self.logic.set_maze(abspath('./logic/files/maze_400x400.csv'))
                        self.select_algorithm()
                    if BACK_BTN.input_check(MOUSE):
                        self.decrease_step()

            pygame.display.update()
    
    def select_algorithm(self):
        
        self.increase_step()

        while self.step >= 2:

            self.window.blit(self.window.background, (0,0))

            MOUSE = pygame.mouse.get_pos()

            TITLE_TEXT = self.font.tilte.render("MAZE SOLVER", True, "Black")
            TITLE_RECT = TITLE_TEXT.get_rect(center=(400,100))

            self.window.blit(TITLE_TEXT, TITLE_RECT)

            INFO_TEXT = self.font.info.render("Select the search algorithm to use", True, "Black")
            INFO_RECT = INFO_TEXT.get_rect(center=(400,200))

            self.window.blit(INFO_TEXT, INFO_RECT)

            DFS = Button(image=None, pos=(400,250),
                            text_input="DFS", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")

            BFS = Button(image=None, pos=(400,310),
                            text_input="BFS", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")

            IDFS = Button(image=None, pos=(400,380),
                            text_input="Iterative DFS", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")

            UCS = Button(image=None, pos=(400,440),
                            text_input="Uniform Cost Search", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")

            GREEDY = Button(image=None, pos=(400,500),
                            text_input="Greedy", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")

            ASTAR = Button(image=None, pos=(400,560),
                            text_input="A*", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")
            
            BACK_BTN = Button(image=None, pos=(40,580),
                            text_input="Back", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")
            
            for button in [DFS, BFS, IDFS, UCS, GREEDY, ASTAR, BACK_BTN]:
                button.change_color(MOUSE)
                button.update(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.step == 2:
                    if DFS.input_check(MOUSE):
                        self.logic.set_algorithm('DFS')
                        self.set_language()
                    if BFS.input_check(MOUSE):
                        self.logic.set_algorithm('BFS')
                        self.set_language()
                    if IDFS.input_check(MOUSE):
                        self.logic.set_algorithm('IDFS')
                        self.set_language()
                    if UCS.input_check(MOUSE):
                        self.logic.set_algorithm('UCS')
                        self.set_language()
                    if GREEDY.input_check(MOUSE):
                        self.logic.set_algorithm('GREEDY')
                        self.set_language()
                    if ASTAR.input_check(MOUSE):
                        self.logic.set_algorithm('A*')
                        self.set_language()
                    if BACK_BTN.input_check(MOUSE):
                        self.decrease_step()

            pygame.display.update()

    def set_language(self):
        self.increase_step()

        while self.step >= 3:

            self.window.blit(self.window.background, (0,0))

            MOUSE = pygame.mouse.get_pos()

            TITLE_TEXT = self.font.tilte.render("MAZE SOLVER", True, "Black")
            TITLE_RECT = TITLE_TEXT.get_rect(center=(400,100))

            self.window.blit(TITLE_TEXT, TITLE_RECT)

            INFO_TEXT = self.font.info.render("Select the language to execute the algorithm", True, "Black")
            INFO_RECT = INFO_TEXT.get_rect(center=(400,200))

            self.window.blit(INFO_TEXT, INFO_RECT)

            CPP = Button(image=None, pos=(200,395),
                            text_input="C++", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")

            JULIA = Button(image=None, pos=(600,395),
                            text_input="Julia", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")
            
            BACK_BTN = Button(image=None, pos=(40,580),
                            text_input="Back", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")
            
            for button in [CPP, JULIA, BACK_BTN]:
                button.change_color(MOUSE)
                button.update(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.step == 3:
                    if CPP.input_check(MOUSE):
                        self.logic.set_language('C++')
                        self.loading_page()
                    if JULIA.input_check(MOUSE):
                        self.logic.set_language('Julia')
                        self.loading_page()
                    if BACK_BTN.input_check(MOUSE):
                        self.decrease_step()

            pygame.display.update()
    
    def cpp_process(self):
        #import subprocess
        #subprocess.run(["./{script}".format(script=self.logic.algorithm), "{file}".format(file=self.logic.maze)])
        pass

    def julia_process(self):
        #import subprocess
        #subprocess.run(["julia", "{script}.jl".format(script=self.logic.algorithm), "{file}".format(file=self.logic.maze)])
        pass

    def loading_page(self):

        IS_LOADING = True

        if self.logic.language == 'C++': self.cpp_process()
        if self.logic.language == 'Julia': self.julia_process()

        while IS_LOADING:

            self.window.blit(self.window.background, (0,0))

            TITLE_TEXT = self.font.tilte.render("MAZE SOLVER", True, "Black")
            TITLE_RECT = TITLE_TEXT.get_rect(center=(400,100))

            self.window.blit(TITLE_TEXT, TITLE_RECT)

            LOADING_TEXT = self.font.subtitle.render("Loading...", True, "Black")
            LOADING_RECT = LOADING_TEXT.get_rect(center=(400,300))

            self.window.blit(LOADING_TEXT, LOADING_RECT)

            INFO_TEXT = self.font.info.render(utils.read_copy('loading_copy.txt').format(
                                            language = self.logic.language, algorithm = self.logic.algorithm, 
                                            maze = self.logic.maze.split('\\')[-1]), True, "Black")

            INFO_RECT = INFO_TEXT.get_rect(center=(400,400))

            self.window.blit(INFO_TEXT, INFO_RECT)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def upload_maze(self):
        self.increase_step()

        SHOW_CONTINUE = False

        while self.step >= 1:

            self.window.blit(self.window.background, (0,0))

            MOUSE = pygame.mouse.get_pos()

            TITLE_TEXT = self.font.tilte.render("MAZE SOLVER", True, "Black")
            TITLE_RECT = TITLE_TEXT.get_rect(center=(400,100))

            self.window.blit(TITLE_TEXT, TITLE_RECT)

            INFO_TEXT = self.font.info.render("Upload the maze to evaluate", True, "Black")
            INFO_RECT = INFO_TEXT.get_rect(center=(400,200))

            self.window.blit(INFO_TEXT, INFO_RECT)

            UPLOAD = Button(image=None, pos=(400,300),
                            text_input="Click to upload", font=self.font.subtitle, 
                            base_color="#000000", hovering_color="#FFFFFF")

            CONTINUE = Button(image=None, pos=(400,450),
                            text_input="Continue", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")
            
            BACK_BTN = Button(image=None, pos=(40,580),
                            text_input="Back", font=self.font.text, 
                            base_color="#000000", hovering_color="#FFFFFF")
            
            for button in [UPLOAD, BACK_BTN]:
                button.change_color(MOUSE)
                button.update(self.window)

            if SHOW_CONTINUE:
                CONTINUE.change_color(MOUSE)
                CONTINUE.update(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.step == 1:
                    if UPLOAD.input_check(MOUSE):
                        maze_file = utils.open_file()
                        print(maze_file)
                        SHOW_CONTINUE = True if len(maze_file) > 0 else False
                        self.logic.set_maze(maze_file)
                    if CONTINUE.input_check(MOUSE):
                        self.select_algorithm()
                    if BACK_BTN.input_check(MOUSE):
                        self.decrease_step()

            pygame.display.update()

