 # -*- coding: utf-8 -*-
from pygame import Surface
from config.window import Window

class Logic():
    """ Manage maze solver logic."""
    
    def __init__(self) -> None:
        """
        Logic constructor.

        Args: None

        Returns: None

        """
        self.maze = None
        self.algorithm = None
        self.language = "C++"
    
    # SET SOLVER SETTINGS

    def set_maze(self, maze: str) -> None:
        """
        Set the maze to solve.

        Args:
            maze: A str with the info of the maze.

        Returns: None

        """
        self.maze = maze
    
    def set_algorithm(self, algorithm) -> None:
        """
        Set the algorithm to use.

        Args:
            algorithm: A str with the name of the algorithm file.

        Returns: None

        """
        self.algorithm = algorithm
    
    def set_language(self, language: str) -> None:
        """
        Set the language to use.

        Args:
            language: A str with the name of language to use.

        Returns: None

        """
        self.language = language

    def read_copy(self, file_name: str) -> None:
        """
        Read file in path src/copys.

        Args:
            file_name: A str with the name and extension of the copy.

        Returns:
            A str with the content of the file

        """
        from os.path import join

        with open(join(self.root_path(), 'src', 'copys', file_name).replace('\\', '/'), encoding = 'utf-8') as f:
            file = f.read()
        return file

    # SOLVER PROCESS

    def cpp_process(self) -> None:
        """
        Execute the c++ selected algorithm in the selected maze.

        Args: None

        Returns: None

        """
        import subprocess
        from sys import platform
        from os.path import join

        if platform == 'win32':
            if self.algorithm == 'DLS':
                script = f'.\{self.algorithm}.exe {self.maze} {1000}'
            else:
                script = f'.\{self.algorithm}.exe {self.maze}'

            f = open("windows.bat", "w")
            f.writelines([
                    f"cd {join(self.root_path(), 'logic', 'C++')}\n",
                    script
                    ])
            f.close()
            
            subprocess.run(['windows.bat'])
        else:
            subprocess.run(['chmod', '+x','./linux.sh'])

            if self.algorithm == 'DLS':
                script = f'./{self.algorithm} {self.maze} {1000}'
            else:
                script = f'./{self.algorithm} {self.maze}'

            f = open("./linux.sh", "w")
            f.writelines([
                    "#!/bin/bash\n",
                    f"cd {join(self.root_path(), 'logic', 'C++')}\n",
                    script
                    ])
            f.close()
            
            subprocess.run(['sh', './linux.sh'])

    def julia_process(self) -> None:
        """
        Execute the julia selected algorithm in the selected maze.

        Args: None

        Returns: None

        """
        #import subprocess
        #subprocess.run(["julia", "{script}.jl".format(script=self.algorithm), "{file}".format(file=self.maze)])
        pass

    # MAZE LOGIC

    def draw_maze(self, maze: list, window: Window, gap: int):
        """
        Draw the grid with the actual changes. (Steps of animation)

        Args:
            maze: a List[List[str,...]] with the maze info
            window: a pygame.Surface to blit the actual state of the maze
            gap: int that represent the space for the buttons

        Returns: None

        """
        from pygame import Rect
        from pygame.draw import rect as draw_rect
        
        blockSize = int(window.height/len(maze))

        grid_x, grid_y = 0, 0

        for y in range(0, window.height, blockSize):
            grid_y = 0
            for x in range(0, window.width-gap, blockSize):
                
                if grid_x < len(maze) and grid_y < len(maze):
                    rect = Rect(x+gap, y, blockSize, blockSize)

                    if maze[grid_x][grid_y] == 'w': 
                        draw_rect(window.window, "Red", rect, 100)
                    elif maze[grid_x][grid_y] == 't': 
                        draw_rect(window.window, "Blue", rect, 100)
                    elif maze[grid_x][grid_y] == 's': 
                        draw_rect(window.window, "Green", rect, 100)
                    else: 
                        draw_rect(window.window, "White", rect, 100)
                
                grid_y += 1
            grid_x += 1

    def set_actual_cell(self, actual_cell: list, dir: str) -> None:
        """
        Set the next cell to modify.

        Args:
            maze: a List[List[str,...]] with the maze info
            actual_cell: a List[int, int] with the top of search algorithm animation
            dir: The direccion to turn

        Returns: None

        """
        if dir == 'D':
            return [actual_cell[0] + 1, actual_cell[1]]
        elif dir == 'R':
            return [actual_cell[0], actual_cell[1] + 1]
        elif dir == 'L':
            return [actual_cell[0], actual_cell[1] - 1]
        else:
            return [actual_cell[0] - 1, actual_cell[1]]

    def path_as_img(self, size: int) -> Surface:
        """
        Create a object with the maze and the solution path.

        Args:
            size: a int with the length of the size

        Returns: a pygame.Surface with the screenshot of the maze with the solution path

        """
        from pygame.image import load
        from os.path import join
        from os import remove

        img = load(join(self.root_path(), f"solution_with_{self.algorithm}_in_maze_{size}x{size}.jpg")).convert()
        remove(join(self.root_path(), f"solution_with_{self.algorithm}_in_maze_{size}x{size}.jpg"))

        return img
    
    def modify_traverse(self, maze, traverse, tstep) -> None:
        """
        Modify the maze with the new state of the traverse animation

        Args:
            maze: a List[List[str,...]] with the maze info
            traverse: a List[Tuples[int, int]] with the traverse info
            tstep: a int with the state of the traverse in the animation

        Returns: None

        """
        maze[traverse[tstep][0]][traverse[tstep][1]] = 't'
        return maze

    def modify_solution(self, maze, actual_cell) -> None:
        """
        Modify the maze with the new state of the solution animation

        Args:
            maze: a List[List[str,...]] with the maze info
            solution: a List[str,...] with the traverse info
            sstep: a int with the state of the solution in the animation

        Returns: None

        """
        maze[actual_cell[0]][actual_cell[1]] = 's'
        return maze

    # UTILS

    def root_path(self) -> None:
        """
        get the root path.

        Args: None

        Returns:
            A str with the root path.

        """
        from os.path import join, sep, dirname, abspath

        return sep.join(dirname(abspath(__file__)).split(sep)[:-1])

    def open_maze(self) -> None:
         
        """
        Read the maze file.

        Args: None

        Returns:
            A List[List[str]] with the info of the maze.

        """
        with open(self.maze, encoding = 'utf-8') as f:
            file = f.read()
        
        raw_maze = file.replace("\n\n","\n").strip().split('\n')
        maze = [ row.strip().split(',') for row in raw_maze]

        return maze

    def open_traverse(self) -> None:
        """
        Read the traverse file.

        Args: None

        Returns:
            A List[Tuple[(int,int)]] with the traverse graph.

        """

        from os.path import join

        with open(join(self.root_path(), 'logic', f'{self.language}', 'output', 
                        f'{self.algorithm}_traverse.txt'), encoding = 'utf-8') as f:
            file = f.read()
        
        raw_list = file.split()
        solve = sorted(set(raw_list), key=lambda x:raw_list.index(x))
        return [(int(item.split(',')[0][1:]),  int(item.split(',')[1][:-1])) for item in solve]

    def open_solution(self) -> None:
        """
        Read the solution file.

        Args: None

        Returns:
            A List[str,...] with the solution path

        """

        from os.path import join

        with open(join(self.root_path(), 'logic', f'{self.language}', 'output', 
                        f'{self.algorithm}_path.txt'), encoding = 'utf-8') as f:
            file = f.read()
        
        return file.split()

    def open_stats(self) -> None:
        """
        Read the stats file.

        Args: None

        Returns:
            A List[str,...] with the solution path

        """

        from os.path import join

        with open(join(self.root_path(), 'logic', f'{self.language}', 'output', 
                        f'{self.algorithm}_stats.txt'), encoding = 'utf-8') as f:
            file = f.read()

        return file.split()

    def open_file(self) -> None:
        """
        Open a filedialog to select a file.

        Args: None

        Returns:
            A str with the content of the file selected in the filedialog

        """
        from tkinter import filedialog
        return filedialog.askopenfilename()
    
    def open_folder(self) -> None:
        """
        Open a filedialog to select a folder.

        Args: None

        Returns:
            A str with the content of the file selected in the filedialog

        """
        from tkinter import filedialog
        return filedialog.askdirectory()

class Node:
    def __init__(self, tag, index) -> None:
        self.index = index
        self.tag = tag
        self.childs = []
    
    def __str__(self) -> str:
        return f'Node -> tag: {self.tag}, index: {self.index}'

class Tree:
    def __init__(self, logic) -> None:
        self.tree = self.get_tree(logic)
        self.root = Node(self.tree[0], 0)
        self.max_childs = 0
        self.set_tree(self.root)
    
    def set_tree(self, father):
        count = 0
        for x in range(1,5):
            try:
                index = (4*father.index)+x
                tag = self.tree[index]
                if tag != '-1':
                    father.childs.append(Node(tag, index))
                    count += 1
            except Exception:
                pass

        if count >= self.max_childs: self.max_childs = count
        
        for child in father.childs:
            self.set_tree(child)
    
    def print_tree(self, window, font):
        self.print_childs(window, font, [self.root], self.max_childs, 0, None)

    def print_childs(self, window, font, childs, max_childs, level, fcords):
        from pygame import Rect
        from pygame.draw import rect as draw_rect, line as draw_line

        nodeSize = int(100/max_childs)
        
        for i in range(len(childs)):
            x_pos, y_pos = (nodeSize-10)+(i*nodeSize), 150+(level*30)

            if fcords != None: draw_line(window.window, "Yellow", (x_pos+15, y_pos+6), fcords)

            rect = Rect(x_pos, y_pos, 30, 15)
            draw_rect(window.window, "Yellow", rect, 100)

            text = font.render(childs[i].tag, None, "Black")
            text_rect = text.get_rect(center=(x_pos+15, y_pos+6))

            window.blit(text, text_rect)

            self.print_childs(window, font, childs[i].childs, max_childs, level+1, (x_pos+15, y_pos+6))

    def get_tree(self, logic) -> None:
        """
        Read the stats file.

        Args: None

        Returns:
            A List[str,...] with the solution path

        """

        from os.path import join

        with open(join(logic.root_path(), 'logic', f'{logic.language}', 'output', 
                        f'{logic.algorithm}_tree.txt'), encoding = 'utf-8') as f:
            file = f.read()

        return file.split()
