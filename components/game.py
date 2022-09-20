 # -*- coding: utf-8 -*-

from config.window import Window


class Game():
    """ Manage game."""

    def __init__(self) -> None:
        """
        Game constructor.

        Args: None

        Returns: None

        """
        from components.font import Font
        from components.logic import Logic
        from components.images import Images
        from pygame.time import Clock

        self.clock = Clock()
        self.font = Font()
        self.images = Images()
        self.window = None
        self.logic = Logic()
        self.step = 0
    
    # GAME CONFIG

    def start_game(self) -> None:
        """
        Init game configuration and start menu screen.

        Args: None

        Returns: None

        """
        self.main()
    
    def end_game(self) -> None:
        """
        End game and finish program.

        Args: None

        Returns: None

        """
        from sys import exit
        from pygame import quit

        quit()
        exit()
    
    def create_window(self, dimentions: tuple, caption: str) -> Window:
        """
        Create a new game window.

        Args: 
            dimentions: A Tuple(int, int) with the dimentions of the window.
            caption: A str with the caption of the window.

        Returns: None

        """
        from config.window import Window
        from pygame.transform import scale

        self.window = Window(dimentions, caption, scale(self.images.background, (dimentions)))
        self.window.start(self.images.icon)

    # MENU LOGIC

    def increase_step(self) -> None:
        """
        Increase menu state.

        Args: None

        Returns: None

        """
        self.step += 1

    def decrease_step(self, max: bool = None):
        """
        Decrease menu state.

        Args: None

        Returns: None

        """
        self.step -= 1
        if max: self.step = 0

    # BLIT SECTIONS

    def blit_background(self) -> None:
        """
        Blit background.

        Args: None

        Returns: None

        """
        from pygame.transform import scale

        self.window.blit(scale(self.window.background, (self.window.width, self.window.height)), (0,0))

    def blit_game_title(self) -> None:
        """
        Blit logo and title.

        Args: None

        Returns: None

        """
        self.blit_background()
        self.window.blit(self.images.icon, (100, 10))

        TITLE_TEXT1 = self.font.tilte.render("MAZE", True, "#FFFFFF")
        TITLE_TEXT2 = self.font.tilte.render("SOLVER", True, "#FFFFFF")

        TITLE_REC1 = TITLE_TEXT1.get_rect(center=(550,80))
        TITLE_REC2 = TITLE_TEXT2.get_rect(center=(550,180))

        self.window.blit(TITLE_TEXT1, TITLE_REC1)
        self.window.blit(TITLE_TEXT2, TITLE_REC2)

    def blit_buttons(self, MOUSE: tuple, buttons: tuple) -> list:
        """
        Blit buttons.

        Args: 
            MOUSE: A Tuple(int, int) with the mouse position
            buttons: A Tuple()

        Returns: None

        """
        from components.button import Button
        
        new_buttons = []
        for options in buttons:
            BUTTON = Button(*options)
            BUTTON.update(self.window, MOUSE)
            new_buttons.append(BUTTON)
        
        return new_buttons
    
    def blit_back_button(self, MOUSE: tuple, is_other: str = None) -> None:
        """
        Blit buttons.

        Args: 
            MOUSE: A Tuple(int, int) with the mouse position
            is_other: A str with the text for the button

        Returns: None

        """
        from components.button import Button
        from pygame.transform import scale

        BACK_BTN = Button(image=scale(self.images.buttons[0], (80, 40)), pos=(40,20),
                            text_input="Back" if is_other == None else is_other, font=self.font.text, 
                            base_color="#FFFFFF", hovering_color="#FFFFFF",
                            hovering_image=scale(self.images.buttons[2], (80, 40)))

        BACK_BTN.update(self.window, MOUSE)

        return BACK_BTN

    # MENU BUTTONS CONFIG

    def get_big_buttons(self, options: tuple) -> tuple:
        """
        Blit big buttons.

        Args: 
            options: A Tuple(Tuple(int, int), str) with the button position and text to blit

        Returns: 
            A Tuple(pygame.Surface, Tuple(int, int), str, pygame.font.Font, str, str, pygame.Surface)

        """
        new_options = []
        for option in options:
            new_options.append(
                (self.images.buttons[0], option[0], option[1], 
                self.font.subtitle, "#FFFFFF", "#FFFFFF", self.images.buttons[2])
            )
        return tuple(new_options)
    
    def get_medium_buttons(self, options: tuple) -> tuple:
        """
        Blit medium buttons.

        Args: 
            options: A Tuple(Tuple(int, int), str) with the button position and text to blit

        Returns: 
            A Tuple(pygame.Surface, Tuple(int, int), str, pygame.font.Font, str, str, pygame.Surface)
            
        """
        from pygame.transform import scale

        new_options = []
        for option in options:
            new_options.append(
                (scale(self.images.buttons[0], (200, 80)), 
                    option[0], option[1], self.font.text, "#FFFFFF", "#FFFFFF", 
                    scale(self.images.buttons[2], (200, 80)))
            )
        return tuple(new_options)
    
    def get_small_buttons(self, options: tuple) -> tuple:
        """
        Blit small buttons.

        Args: 
            options: A Tuple(Tuple(int, int), str) with the button position and text to blit

        Returns: 
            A Tuple(pygame.Surface, Tuple(int, int), str, pygame.font.Font, str, str, pygame.Surface)
            
        """
        from pygame.transform import scale

        new_options = []
        for option in options:
            new_options.append(
                (scale(self.images.buttons[0], (150, 80)), 
                    option[0], option[1], self.font.subtitle, "#FFFFFF", "#FFFFFF", 
                    scale(self.images.buttons[2], (150, 80)))
            )
        return tuple(new_options)

    # BLIT WINDOWS

    def main(self) -> None:
        """
        Show principal menu menu.

        Args: None

        Returns: None

        """
        from pygame.event import get as event_get
        from pygame.mouse import get_pos as mouse_pos
        from pygame.display import update as update_display
        from pygame import QUIT, MOUSEBUTTONUP

        self.create_window((800, 600), "Maze Solver")

        while self.step >= 0:

            self.blit_game_title()  

            MOUSE = mouse_pos()     

            BUTTONS = self.blit_buttons(MOUSE, self.get_big_buttons((
                                                    ((200,395), "Select Maze"),
                                                    ((600,395), "Upload Maze"))
                                        ))
            
            EXIT_BTN = self.blit_back_button(MOUSE, "Exit")

            self.clock.tick(self.window.fps)

            for event in event_get():
                if event.type == QUIT:
                    self.end_game()
                if event.type == MOUSEBUTTONUP and event.button == 1 and self.step == 0:
                    if BUTTONS[0].input_check(MOUSE):
                        self.select_maze()
                    if BUTTONS[1].input_check(MOUSE):
                        self.upload_maze()
                    if EXIT_BTN.input_check(MOUSE):
                        self.end_game()
                    
            update_display()
    
    def select_maze(self) -> None:
        """
        Show maze selection menu.

        Args: None

        Returns: None

        """
        from pygame.event import get as event_get
        from pygame.mouse import get_pos as mouse_pos
        from pygame.display import update as update_display
        from pygame import QUIT, MOUSEBUTTONUP
        from os.path import abspath

        self.increase_step()

        while self.step >= 1:

            self.blit_game_title()

            MOUSE = mouse_pos()

            INFO_TEXT = self.font.info.render("Select the maze to evaluate", True, "White")
            INFO_RECT = INFO_TEXT.get_rect(center=(400,300))

            self.window.blit(INFO_TEXT, INFO_RECT)
            
            BUTTONS = self.blit_buttons(MOUSE, self.get_medium_buttons((
                                                    ((150,400), "Maze 5x5"),
                                                    ((150,500), "Maze 10x10"),
                                                    ((400,450), "Maze 50x50"),
                                                    ((650,400), "Maze 100x100"),
                                                    ((650,500), "Maze 400x400"))
                                        ))
            
            BACK_BTN = self.blit_back_button(MOUSE)

            for event in event_get():
                if event.type == QUIT:
                    self.end_game()
                if event.type == MOUSEBUTTONUP and event.button == 1 and self.step == 1:
                    if BUTTONS[0].input_check(MOUSE):
                        self.logic.set_maze(abspath('./logic/files/maze_5x5.csv'))
                        self.select_algorithm()
                    if BUTTONS[1].input_check(MOUSE):
                        self.logic.set_maze(abspath('./logic/files/maze_10x10.csv'))
                        self.select_algorithm()
                    if BUTTONS[2].input_check(MOUSE):
                        self.logic.set_maze(abspath('./logic/files/maze_50x50.csv'))
                        self.select_algorithm()
                    if BUTTONS[3].input_check(MOUSE):
                        self.logic.set_maze(abspath('./logic/files/maze_100x100.csv'))
                        self.select_algorithm()
                    if BUTTONS[4].input_check(MOUSE):
                        self.logic.set_maze(abspath('./logic/files/maze_400x400.csv'))
                        self.select_algorithm()
                    if BACK_BTN.input_check(MOUSE):
                        self.decrease_step()

            update_display()
    
    def select_algorithm(self) -> None:
        """
        Show algorithm selection menu.

        Args: None

        Returns: None

        """
        from pygame.event import get as event_get
        from pygame.mouse import get_pos as mouse_pos
        from pygame.display import update as update_display
        from pygame import QUIT, MOUSEBUTTONUP
        
        self.increase_step()

        while self.step >= 2:

            self.blit_game_title()

            MOUSE = mouse_pos()

            INFO_TEXT = self.font.info.render("Select the search algorithm to use", True, "White")
            INFO_RECT = INFO_TEXT.get_rect(center=(400,300))

            self.window.blit(INFO_TEXT, INFO_RECT)

            BUTTONS = self.blit_buttons(MOUSE, self.get_medium_buttons((
                                                    ((150,400), "DFS"),
                                                    ((150,500), "BFS"),
                                                    ((400,400), "Iterative DFS"),
                                                    ((400,500), "Uniform Cost"),
                                                    ((650,400), "Greedy"),
                                                    ((650,500), "A*"))
                                        ))
            
            BACK_BTN = self.blit_back_button(MOUSE)

            for event in event_get():
                if event.type == QUIT:
                    self.end_game()
                if event.type == MOUSEBUTTONUP and event.button == 1 and self.step == 2:
                    if BUTTONS[0].input_check(MOUSE):
                        self.logic.set_algorithm('DFS')
                        self.set_language()
                    if BUTTONS[1].input_check(MOUSE):
                        self.logic.set_algorithm('BFS')
                        self.set_language()
                    if BUTTONS[2].input_check(MOUSE):
                        self.logic.set_algorithm('DLS')
                        self.set_language()
                    if BUTTONS[3].input_check(MOUSE):
                        self.logic.set_algorithm('DFS')
                        self.set_language()
                    if BUTTONS[4].input_check(MOUSE):
                        self.logic.set_algorithm('DFS')
                        self.set_language()
                    if BUTTONS[5].input_check(MOUSE):
                        self.logic.set_algorithm('AStar')
                        self.set_language()
                    if BACK_BTN.input_check(MOUSE):
                        self.decrease_step()

            update_display()

    def set_language(self) -> None:
        """
        Show language selection menu.

        Args: None

        Returns: None

        """
        from pygame.event import get as event_get
        from pygame.mouse import get_pos as mouse_pos
        from pygame.display import update as update_display
        from pygame import QUIT, MOUSEBUTTONUP

        self.increase_step()

        while self.step >= 3:

            self.blit_game_title()

            MOUSE = mouse_pos()

            INFO_TEXT = self.font.info.render("Select the language to execute the algorithm", True, "White")
            INFO_RECT = INFO_TEXT.get_rect(center=(400,300))

            self.window.blit(INFO_TEXT, INFO_RECT)

            BUTTONS = self.blit_buttons(MOUSE, self.get_small_buttons((
                                                    ((300,450), "C++"),
                                                    ((500,450), "Julia"))
                                        ))
            
            BACK_BTN = self.blit_back_button(MOUSE)

            for event in event_get():
                if event.type == QUIT:
                    self.end_game()
                if event.type == MOUSEBUTTONUP and event.button == 1 and self.step == 3:
                    if BUTTONS[0].input_check(MOUSE):
                        self.logic.set_language('C++')
                        self.show_maze()
                    if BUTTONS[1].input_check(MOUSE):
                        self.logic.set_language('Julia')
                        self.show_maze()
                    if BACK_BTN.input_check(MOUSE):
                        self.decrease_step()

            update_display()

    def upload_maze(self) -> None:
        """
        Show upload maze menu.

        Args: None

        Returns: None

        """
        from pygame.event import get as event_get
        from pygame.mouse import get_pos as mouse_pos
        from pygame.display import update as update_display
        from pygame import QUIT, MOUSEBUTTONUP

        self.increase_step()

        SHOW_CONTINUE = False
        WARNING = False

        while self.step >= 1:

            self.blit_game_title()

            MOUSE = mouse_pos()

            INFO_TEXT = self.font.info.render("Upload the maze to evaluate", True, "White")
            INFO_RECT = INFO_TEXT.get_rect(center=(400,300))

            self.window.blit(INFO_TEXT, INFO_RECT)

            BUTTONS = self.blit_buttons(MOUSE, self.get_big_buttons((
                                                    ((400,400), "Click to upload"),
                                                    ((400,500), "Continue"))
                                        ))
            
            BACK_BTN = self.blit_back_button(MOUSE)

            if WARNING:
                WARNING_TEXT = self.font.info.render("Please select a file", True, "Red")
                WARNING_RECT = WARNING_TEXT.get_rect(center=(400,335))
                self.window.blit(WARNING_TEXT, WARNING_RECT)

            for event in event_get():
                if event.type == QUIT:
                    self.end_game()
                if event.type == MOUSEBUTTONUP and event.button == 1 and self.step == 1:
                    if BUTTONS[0].input_check(MOUSE):
                        maze_file = self.logic.open_file()
                        SHOW_CONTINUE = True if len(maze_file) > 0 else False
                        self.logic.set_maze(maze_file)
                    if BUTTONS[1].input_check(MOUSE):
                        if SHOW_CONTINUE: 
                            self.select_algorithm()
                            WARNING = False
                        else: 
                            WARNING = True

                    if BACK_BTN.input_check(MOUSE):
                        self.decrease_step()

            update_display()

    def loading_page(self) -> None:
        """
        Show loading message while solve algorithms are running.

        Args: None

        Returns: None

        """
        from pygame.event import get as event_get
        from pygame.display import update as update_display
        from pygame import QUIT

        IS_LOADING = True

        if self.logic.language == 'C++': self.logic.cpp_process()
        if self.logic.language == 'Julia': self.logic.julia_process()

        while IS_LOADING:

            self.blit_game_title()

            LOADING_TEXT = self.font.subtitle.render("Loading...", True, "Black")
            LOADING_RECT = LOADING_TEXT.get_rect(center=(400,300))

            self.window.blit(LOADING_TEXT, LOADING_RECT)

            INFO_TEXT = self.font.info.render(self.logic.read_copy('loading_copy.txt').format(
                                            language = self.logic.language, algorithm = self.logic.algorithm, 
                                            maze = self.logic.maze.split('\\')[-1].split('/')[-1]), True, "White")

            INFO_RECT = INFO_TEXT.get_rect(center=(400,400))

            self.window.blit(INFO_TEXT, INFO_RECT)

            for event in event_get():
                if event.type == QUIT:
                    self.end_game()

            update_display()
        
            if self.logic.is_done(): IS_LOADING = False

    def show_maze(self) -> None:
        
        """
        Show maze animation.

        Args: None

        Returns: None

        """
        from pygame.event import get as event_get
        from pygame.mouse import get_pos as mouse_pos
        from pygame.display import update as update_display
        from pygame import QUIT, MOUSEBUTTONUP
        from config.window import Window

        self.loading_page()

        self.increase_step()

        self.create_window((780,700), self.logic.algorithm)

        maze = self.logic.open_maze()

        for i in range(len(maze[0])):
            if maze[0][i] == 'c' : actual_cell = [0,i]

        traverse = self.logic.open_traverse()
        tstep = 0

        solution = self.logic.open_solution()
        sstep = 0
        if len(maze) <= 10:
            TIMING = 150
        elif len(maze) <= 50:
            TIMING = 10
        else: 
            TIMING = 1
        WAIT_TIME = 1

        while self.step >= 4:

            self.blit_background()

            MOUSE = mouse_pos()
            
            HOME_BTN = self.blit_back_button(MOUSE, "Home")

            self.logic.draw_maze(maze, self.window)

            if WAIT_TIME%TIMING == 0:
                if tstep < len(traverse):
                    maze[traverse[tstep][0]][traverse[tstep][1]] = 't'
                    tstep += 1
                    WAIT_TIME = 0
                elif sstep < len(solution):
                    if sstep == 0: maze[actual_cell[0]][actual_cell[1]] = 's'
                    actual_cell = self.logic.set_actual_cell(actual_cell, solution[sstep])
                    maze[actual_cell[0]][actual_cell[1]] = 's'
                    sstep += 1

            WAIT_TIME += 1

            for event in event_get():
                if event.type == QUIT:
                    self.end_game()
                if event.type == MOUSEBUTTONUP and event.button == 1 and self.step == 4:
                    if HOME_BTN.input_check(MOUSE):
                        self.decrease_step(max)

            update_display()
        
        self.create_window((800, 600), "Maze Solver")