 # -*- coding: utf-8 -*-
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
        self.language = None
    
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
        from os.path import join, sep, dirname, abspath

        init_path = sep.join(dirname(abspath(__file__)).split(sep)[:-1])
        with open(join(init_path, 'src', 'copys', file_name).replace('\\', '/'), encoding = 'utf-8') as f:
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
        
        subprocess.run(['chmod', '+x','./linux.sh'])

        if self.algorithm == 'DLS':
            script = f'./{self.algorithm} {self.maze} {1000}'
        else:
            script = f'./{self.algorithm} {self.maze}'

        f = open("./linux.sh", "w")
        f.writelines([
                "#!/bin/bash\n",
                script
                ])
        f.close()
        print(f'./{self.algorithm} {self.maze}')
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

    # SOLVER VALIDATION

    def is_done(self) -> None:
        """
        Check if algorithm is done.

        Args: None

        Returns: None

        """
        from pygame.time import wait
        wait(5000)
        return True

    # UTILS

    def draw_maze(self, maze, window):
        from pygame import Rect
        from pygame.draw import rect as draw_rect
        
        blockSize = int((window.height)/len(maze))

        grid_x, grid_y = 0, 0

        for y in range(0, window.height, blockSize):
            grid_y = 0
            for x in range(0, window.width-80, blockSize):
                
                if grid_x < len(maze) and grid_y < len(maze):
                    rect = Rect(x+80, y, blockSize, blockSize)

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

    def set_actual_cell(self, actual_cell, dir) -> None:
        if dir == 'D':
            return [actual_cell[0] + 1, actual_cell[1]]
        elif dir == 'R':
            return [actual_cell[0], actual_cell[1] + 1]
        elif dir == 'L':
            return [actual_cell[0], actual_cell[1] - 1]
        else:
            return [actual_cell[0] - 1, actual_cell[1]]

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

        from os.path import join, dirname, abspath, sep
        init_path = sep.join(dirname(abspath(__file__)).split(sep)[:-1])

        with open(join(init_path, 'logic', 'output', 
                        '{script}_traverse.txt'.format(script = self.algorithm)), encoding = 'utf-8') as f:
            file = f.read()
        
        raw_list = file.split()
        traverse = [(int(item.split(',')[0][1:]),  int(item.split(',')[1][:-1])) for item in raw_list]

        return traverse

    def open_solution(self) -> None:

        from os.path import join, dirname, abspath, sep
        init_path = sep.join(dirname(abspath(__file__)).split(sep)[:-1])

        with open(join(init_path, 'logic', 'output', 
                        '{script}_path.txt'.format(script = self.algorithm)), encoding = 'utf-8') as f:
            file = f.read()
        
        solve = file.split()

        return solve

    def open_file(self) -> None:
        """
        Open a filedialog.

        Args: None

        Returns:
            A str with the content of the file selected in the filedialog

        """
        from tkinter import filedialog
        return filedialog.askopenfilename()