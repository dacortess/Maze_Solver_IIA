 # -*- coding: utf-8 -*-
from os.path import join
from pygame.transform import scale
from pygame.image import load
from pygame import Surface

class Images():
    """ Manage image uploads accross pygame methods."""
    
    def __init__(self) -> None:
        """
        Images constructor.

        Args: None

        Returns: None

        """
        self.buttons = self.get_buttons()
        self.background = self.get_background()
        self.icon = self.get_icon()
    
    # SET IMAGES

    def get_buttons(self) -> tuple:
        """
        Load button image objects.

        Args: None

        Returns:
            A Tuple(Surface, Surface, Surface) with the 3 types of buttons.

        """
        return (load(join('.\src', 'img', 'button', 'button1.png')),
                load(join('.\src', 'img', 'button', 'button2.png')),
                load(join('.\src', 'img', 'button', 'button3.png')))
    
    def get_background(self) -> Surface:
        """
        Load background.

        Args: None

        Returns:
            A pygame.Surface with de background loaded.

        """
        return scale(load(join('.\src', 'img', 'bg', 'bg_deg.jpg')), (800, 600))
    
    def get_icon(self) -> Surface:
        """
        Load icon.

        Args: None

        Returns:
            A pygame.Surface with de icon loaded.
        """
        return load(join('.\src', 'img', 'icon', 'icon.png'))



