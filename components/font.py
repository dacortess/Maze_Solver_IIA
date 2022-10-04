 # -*- coding: utf-8 -*-
from pygame import font as F
from os.path import sep, dirname, abspath

init_path = sep.join(dirname(abspath(__file__)).split(sep)[:-1])

class Font():
    """ Manage pygame font object."""

    def __init__(self) -> None:
        """
        Font constructor and font init

        Args: None

        Returns: None

        """
        F.init()
        self.tilte = self.local_font('comicsans', 80)
        self.subtitle = self.external_font('Adumu.ttf', 30)
        self.text = self.external_font('Adumu.ttf', 20)
        self.info = self.local_font('comicsans', 20)
        self.mini = self.local_font('comicsans', 10)

    def external_font(self, font, size) -> F.Font:
        """
        Load a font from file.

        Args:
            font: A str with name of the font with the extention.

        Returns:
            A pygame.font.Font object

        """
        from os.path import join
        return F.Font(join(init_path, "src", "font", font), size) #Ej. Adumu.ttf
    
    def local_font(self, font, size) -> F.Font:
        """
        Load a font from system

        Args:
            font: A str with name of the font in the system.

        Returns:
            A pygame.font.Font object

        """
        return F.SysFont(font, size) # Ej. comicsans