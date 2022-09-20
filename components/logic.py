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
        from os.path import join
        with open(join('./src/copys', file_name).replace('\\', '/'), encoding = 'utf-8') as f:
            file = f.read()
        return file

    # SOLVER PROCESS

    def cpp_process(self) -> None:
        """
        Execute the c++ selected algorithm in the selected maze.

        Args: None

        Returns: None

        """
        #import subprocess
        #subprocess.run(["./{script}".format(script=self.algorithm), "{file}".format(file=self.maze)])
        pass

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
        #TODO: COMPLETE
        return False
    
    # UTILS

    def open_file(self) -> None:
        """
        Open a filedialog.

        Args: None

        Returns:
            A str with the content of the file selected in the filedialog

        """
        from tkinter import filedialog
        return filedialog.askopenfilename()