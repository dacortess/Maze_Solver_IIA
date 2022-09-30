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
        from logic.logic import Logic
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

        Returns: A pygame.Surface with the new window

        """
        from config.window import Window
        from pygame.transform import scale

        return Window(dimentions, caption, scale(self.images.background, (dimentions)))

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
        self.step = 0 if max else self.step - 1

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

        # Objects config

        TITLE_TEXT1 = self.font.tilte.render("MAZE", True, "#FFFFFF")
        TITLE_TEXT2 = self.font.tilte.render("SOLVER", True, "#FFFFFF")

        TITLE_REC1 = TITLE_TEXT1.get_rect(center=(550,80))
        TITLE_REC2 = TITLE_TEXT2.get_rect(center=(550,180))

        # Blit objects

        self.blit_background()
        self.window.blit(self.images.icon, (100, 10))

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

            # Create button

            BUTTON = Button(*options)

            # Updates the color of the button if the mouse is over it.

            BUTTON.update(self.window, MOUSE)

            # Save the button for future events

            new_buttons.append(BUTTON)
        
        return new_buttons
    
    def blit_save_button(self, MOUSE: tuple) -> None:
        """
        Blit save button.

        Args: 
            MOUSE: A Tuple(int, int) with the mouse position
            is_other: A str with the text for the button

        Returns: None

        """
        from components.button import Button
        from pygame.transform import scale

        # Create button

        SAVE_BTN = Button(image=scale(self.images.buttons[0], (150, 80)), pos=(100,100),
                            text_input="Save as png", font=self.font.text, 
                            base_color="#FFFFFF", hovering_color="#FFFFFF",
                            hovering_image=scale(self.images.buttons[2], (150, 80)))

        # Updates the color of the button if the mouse is over it.

        SAVE_BTN.update(self.window, MOUSE)

        return SAVE_BTN

    def blit_back_button(self, MOUSE: tuple, is_other: str = None) -> None:
        """
        Blit back button.

        Args: 
            MOUSE: A Tuple(int, int) with the mouse position
            is_other: A str with the text for the button

        Returns: None

        """
        from components.button import Button
        from pygame.transform import scale

        # Create button

        BACK_BTN = Button(image=scale(self.images.buttons[0], (80, 40)), pos=(40,20),
                            text_input="Back" if is_other == None else is_other, font=self.font.text, 
                            base_color="#FFFFFF", hovering_color="#FFFFFF",
                            hovering_image=scale(self.images.buttons[2], (80, 40)))
        
        # Updates the color of the button if the mouse is over it.

        BACK_BTN.update(self.window, MOUSE)

        return BACK_BTN

    # MENU BUTTONS CONFIG

    def get_big_buttons(self, options: tuple) -> tuple:
        """
        Set options for big buttons.

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
        Set options for medium buttons.

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
        Set options for small buttons.

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

        # Start window

        self.window = self.create_window((800, 600), "Maze Solver")
        self.window.start(self.images.icon)

        # Window config

        self.clock.tick(self.window.fps)

        # Objects config

        BUTTONS_CONFIG = self.get_big_buttons(( ((200,395), "Select Maze"),
                                                ((600,395), "Upload Maze"))
                                            )

        while self.step >= 0:

            #Mouse position

            MOUSE = mouse_pos() 

            #Blit objects

            self.blit_game_title()  

            BUTTONS = self.blit_buttons(MOUSE, BUTTONS_CONFIG)
            
            EXIT_BTN = self.blit_back_button(MOUSE, "Exit")

            #Event handler

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
            
            # Update window

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
        from os.path import join

        # Menu state

        self.increase_step()

        # Objects config

        INFO_TEXT = self.font.info.render("Select the maze to evaluate", True, "White")
        INFO_RECT = INFO_TEXT.get_rect(center=(400,290))

        CAUTION_TEXT = self.font.info.render("In a maze of size greater than 50, only the solution is shown", 
                                                True, "Grey")
        CAUTION_RECT = CAUTION_TEXT.get_rect(center=(400,325))

        BUTTONS_CONFIG = self.get_medium_buttons((  ((150,400), "Maze 5x5"),
                                                    ((150,500), "Maze 10x10"),
                                                    ((400,450), "Maze 50x50"),
                                                    ((650,400), "Maze 100x100"),
                                                    ((650,500), "Maze 400x400"))
                                                )

        while self.step >= 1:

            # Mouse positions

            MOUSE = mouse_pos()

            # Blit objects

            self.blit_game_title()

            self.window.blit(INFO_TEXT, INFO_RECT)

            self.window.blit(CAUTION_TEXT, CAUTION_RECT)
            
            BUTTONS = self.blit_buttons(MOUSE, BUTTONS_CONFIG)
            
            BACK_BTN = self.blit_back_button(MOUSE)

            # Event handler

            for event in event_get():
                if event.type == QUIT:
                    self.end_game()
                if event.type == MOUSEBUTTONUP and event.button == 1 and self.step == 1:
                    if BUTTONS[0].input_check(MOUSE):
                        self.logic.set_maze(join(self.logic.root_path(), 'logic', 'files', 'maze_5x5.csv'))
                        self.select_algorithm()
                    if BUTTONS[1].input_check(MOUSE):
                        self.logic.set_maze(join(self.logic.root_path(), 'logic', 'files', 'maze_10x10.csv'))
                        self.select_algorithm()
                    if BUTTONS[2].input_check(MOUSE):
                        self.logic.set_maze(join(self.logic.root_path(), 'logic', 'files', 'maze_50x50.csv'))
                        self.select_algorithm()
                    if BUTTONS[3].input_check(MOUSE):
                        self.logic.set_maze(join(self.logic.root_path(), 'logic', 'files', 'maze_100x100.csv'))
                        self.select_algorithm()
                    if BUTTONS[4].input_check(MOUSE):
                        self.logic.set_maze(join(self.logic.root_path(), 'logic', 'files', 'maze_400x400.csv'))
                        self.select_algorithm()
                    if BACK_BTN.input_check(MOUSE):
                        self.decrease_step()

            # Update window

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
        
        # Menu state

        self.increase_step()

        #Objects config

        INFO_TEXT = self.font.info.render("Select the search algorithm to use", True, "White")
        INFO_RECT = INFO_TEXT.get_rect(center=(400,325))

        BUTTONS_CONFIG = self.get_medium_buttons((  ((150,400), "DFS"),
                                                    ((150,500), "BFS"),
                                                    ((400,400), "Iterative DFS"),
                                                    ((400,500), "Uniform Cost"),
                                                    ((650,400), "Greedy"),
                                                    ((650,500), "A*"))
                                                )

        while self.step >= 2:

            # Mouse position

            MOUSE = mouse_pos()

            # Blit objects

            self.blit_game_title()

            self.window.blit(INFO_TEXT, INFO_RECT)

            BUTTONS = self.blit_buttons(MOUSE, BUTTONS_CONFIG)
            
            BACK_BTN = self.blit_back_button(MOUSE)

            #Event handler

            for event in event_get():
                if event.type == QUIT:
                    self.end_game()
                if event.type == MOUSEBUTTONUP and event.button == 1 and self.step == 2:
                    if BUTTONS[0].input_check(MOUSE):
                        self.logic.set_algorithm('DFS')
                        self.show_maze()
                    if BUTTONS[1].input_check(MOUSE):
                        self.logic.set_algorithm('BFS')
                        self.show_maze()
                    if BUTTONS[2].input_check(MOUSE):
                        self.logic.set_algorithm('DLS')
                        self.show_maze()
                    if BUTTONS[3].input_check(MOUSE):
                        self.logic.set_algorithm('UCS')
                        self.show_maze()
                    if BUTTONS[4].input_check(MOUSE):
                        self.logic.set_algorithm('Greedy')
                        self.show_maze()
                    if BUTTONS[5].input_check(MOUSE):
                        self.logic.set_algorithm('AStar')
                        self.show_maze()
                    if BACK_BTN.input_check(MOUSE):
                        self.decrease_step()

            # Update window

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

        #Menu state

        self.increase_step()

        # Objects config

        INFO_TEXT = self.font.info.render("Upload the maze to evaluate", True, "White")
        INFO_RECT = INFO_TEXT.get_rect(center=(400,300))

        WARNING_TEXT = self.font.info.render("Please select a file", True, "Red")
        WARNING_RECT = WARNING_TEXT.get_rect(center=(400,335))

        CAUTION_TEXT = self.font.info.render("Maze saved", True, "Green")
        CAUTION_RECT = CAUTION_TEXT.get_rect(center=(400,335))

        BUTTONS_CONFIG = self.get_big_buttons(( ((400,400), "Click to upload"),
                                                ((400,500), "Continue"))
                                            )

        # Objects flags

        SHOW_CONTINUE = False
        SHOW_WARNING = False
        SHOW_CAUTION = False

        while self.step >= 1:

            # Mouse position

            MOUSE = mouse_pos()

            # Blit Objects

            self.blit_game_title()

            self.window.blit(INFO_TEXT, INFO_RECT)

            BUTTONS = self.blit_buttons(MOUSE, BUTTONS_CONFIG)
            
            BACK_BTN = self.blit_back_button(MOUSE)

            if SHOW_WARNING: self.window.blit(WARNING_TEXT, WARNING_RECT)

            if SHOW_CAUTION: self.window.blit(CAUTION_TEXT, CAUTION_RECT)

            # Event handler

            for event in event_get():
                if event.type == QUIT:
                    self.end_game()
                if event.type == MOUSEBUTTONUP and event.button == 1 and self.step == 1:
                    if BUTTONS[0].input_check(MOUSE):
                        maze_file = self.logic.open_file()
                        if len(maze_file) > 0:
                            SHOW_CONTINUE = True
                            SHOW_CAUTION = True
                            SHOW_WARNING = False
                        else: 
                            SHOW_CONTINUE = False
                            SHOW_WARNING = True
                            SHOW_CAUTION = False
                        self.logic.set_maze(maze_file)
                    if BUTTONS[1].input_check(MOUSE):
                        if SHOW_CONTINUE: 
                            self.select_algorithm()
                            SHOW_WARNING = False
                        else: 
                            SHOW_WARNING = True
                    if BACK_BTN.input_check(MOUSE):
                        self.decrease_step()

            # Update window

            update_display()

    def loading_page(self) -> None:
        """
        Show loading message while solve algorithms are running.

        Args: None

        Returns: None

        """
        from pygame.display import update as update_display

        # Object config

        LOADING_TEXT = self.font.subtitle.render("Loading...", True, "Black")
        LOADING_RECT = LOADING_TEXT.get_rect(center=(400,300))

        INFO_TEXT = self.font.info.render(self.logic.read_copy('loading_copy.txt').format(
                                        language = self.logic.language, algorithm = self.logic.algorithm, 
                                        maze = self.logic.maze.split('\\')[-1].split('/')[-1]), True, "White")

        INFO_RECT = INFO_TEXT.get_rect(center=(400,400))

        # Blit objects

        self.blit_game_title()

        self.window.blit(LOADING_TEXT, LOADING_RECT)

        self.window.blit(INFO_TEXT, INFO_RECT)

        # Update window

        update_display()

        # Run algorithm

        if self.logic.language == 'C++': self.logic.cpp_process()
        #if self.logic.language == 'Julia': self.logic.julia_process() #Depercated

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
        from pygame.transform import scale

        # Show load page while algorithm is running

        self.loading_page()

        # Menu state

        self.increase_step()

        # Read algorithm results

        solution = self.logic.open_solution()

        traverse = self.logic.open_traverse()

        stats = self.logic.open_stats()

        # Objects config

        CAUTION_TEXT = self.font.info.render("Saved", True, "Green")
        CAUTION_RECT = CAUTION_TEXT.get_rect(center=(100,150))

        MEMORY_TEXT = self.font.info.render("Used Memory:", True, "Grey")
        MEMORY_RECT = MEMORY_TEXT.get_rect(center=(100,300))

        VRAM_TEXT = self.font.info.render(f"VRAM: {stats[0]} kb", True, "Grey")
        VRAM_RECT = VRAM_TEXT.get_rect(center=(100,340))

        RAM_TEXT = self.font.info.render(f"RAM: {stats[1]} kb", True, "Grey")
        RAM_RECT = RAM_TEXT.get_rect(center=(100,380))

        TIME_TEXT = self.font.info.render("Execution Time:", True, "Grey")
        TIME_RECT = TIME_TEXT.get_rect(center=(100,450))

        EXTIME_TEXT = self.font.info.render(f"{stats[2]} ms", True, "Grey")
        EXTIME_RECT = EXTIME_TEXT.get_rect(center=(100,480))

        # Objects flags

        IS_SAVED = False
        IS_COMPLETE = False

        # Read maze
                
        maze = self.logic.open_maze()

        # Find start cell

        for i in range(len(maze[0])):
            if maze[0][i] == 'c' : 
                actual_cell = [0,i]
                break

        # Animation config

        TIMING = 50-len(maze)*5
        if TIMING <= 0: TIMING = 1

        WAIT_TIME = 1
        
        sstep = 0
        tstep = 0

        # Screenshot flag

        img = None

        # Maze and start cell backups for screenshots
        
        bk_maze = maze.copy()
        start_cell = actual_cell.copy()

        while self.step >= 3:

            # Mouse position

            MOUSE = mouse_pos()

            # Blit objects

            self.blit_background()
            
            if IS_SAVED: self.window.blit(CAUTION_TEXT, CAUTION_RECT)

            if IS_COMPLETE: SAVE_BTN = self.blit_save_button(MOUSE)

            self.window.blit(MEMORY_TEXT, MEMORY_RECT)

            self.window.blit(VRAM_TEXT, VRAM_RECT)

            self.window.blit(RAM_TEXT, RAM_RECT)

            self.window.blit(TIME_TEXT, TIME_RECT)

            self.window.blit(EXTIME_TEXT, EXTIME_RECT)

            HOME_BTN = self.blit_back_button(MOUSE, "Home")

            # Big maze logic

            if len(maze) > 300:
                if img == None:
                    self.save_maze(bk_maze, solution, start_cell, save_path=self.logic.root_path())
                    img = self.logic.path_as_img(len(bk_maze))
                    IS_COMPLETE = True
                self.window.blit(scale(img, (600,600)), (200,0))
            else:
                self.logic.draw_maze(maze, self.window, 200)

            # Animation Logic

            if WAIT_TIME==TIMING and not IS_COMPLETE:
                if tstep < len(traverse) and len(maze) <= 50:
                    maze = self.logic.modify_traverse(maze, traverse, tstep)
                    tstep += 1
                elif sstep < len(solution):
                    if sstep == 0: maze = self.logic.modify_solution(maze, actual_cell)
                    actual_cell = self.logic.set_actual_cell(actual_cell, solution[sstep])
                    maze = self.logic.modify_solution(maze, actual_cell)
                    sstep += 1
                else:
                    IS_COMPLETE = True
                WAIT_TIME = 0

            WAIT_TIME += 1

            # Event handler

            for event in event_get():
                if event.type == QUIT:
                    self.end_game()
                if event.type == MOUSEBUTTONUP and event.button == 1 and self.step == 3:
                    if HOME_BTN.input_check(MOUSE):
                        self.decrease_step(max = True)
                    if IS_COMPLETE:
                        if SAVE_BTN.input_check(MOUSE):
                            self.save_maze(bk_maze, solution, start_cell)
                            IS_SAVED = True

            # Update window

            update_display()
        
    def save_maze(self, maze: list, solution: list, actual_cell: list, save_path: str =None):
        """
        Save the maze solution to an image.

        Args:
            maze: a List[List[str,...]] with the maze info
            solution: a List[str,...] with the solution instructions
            actual_cell: a List[int, int]

        Returns: None

        """
        from pygame.image import save
        from pygame.transform import scale
        from os. path import join

        # Window resolution

        size = (len(maze)*2)

        # Window to draw maze with the solution 

        new_window = self.create_window((size, size), self.logic.algorithm)

        # Aux vars

        sstep = 0

        # Modify maze with the solution

        while sstep < len(solution):
            if sstep == 0: maze[actual_cell[0]][actual_cell[1]] = 's'
            actual_cell = self.logic.set_actual_cell(actual_cell, solution[sstep])
            maze[actual_cell[0]][actual_cell[1]] = 's'
            sstep += 1

        # Draw solution
        
        self.logic.draw_maze(maze, new_window, 0)

        # Save image

        if save_path == None: save_path = self.logic.open_folder()
        save(scale(new_window.window, (size*10, size*10)), join(save_path, f"solution_with_{self.logic.algorithm}_in_maze_{len(maze)}x{len(maze)}.jpg"))
        
        # Re-scale window

        self.window = self.create_window((800, 600), "Maze Solver")
        self.window.start(self.images.icon)