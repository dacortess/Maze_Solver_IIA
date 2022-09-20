 # -*- coding: utf-8 -*-
from pygame import Surface

class Window():
    """ Manage pygame window updates."""

    def __init__(self, dimensions: tuple, caption: str, background: Surface) -> None:
        """
        Window constructor.

        Args:
            dimensions: A Tuple(int, int) with the dimensions of the window.
            caption: A str with the caption of the window.
            background: A pyagme.Surface with the background of the window.

        Returns:
            None

        """
        from pygame.display import set_mode

        self.width: int = dimensions[0]
        self.height: int = dimensions[1]
        self.caption: str = caption
        self.fps: int = 300
        self.background: Surface = background
        self.window: Surface = set_mode((self.width, self.height))

    # GAME INIT

    def start(self, icon: Surface) -> None:
        """
        Init window config.

        Args:
            icon: A pyagme.Surface with the icon of the window.

        Returns:
            None

        """
        from pygame.display import set_caption, set_icon

        set_caption(self.caption)
        set_icon(icon)

    def set_caption(self, caption: str) -> None:
        """
        Init window config.

        Args:
            icon: A pyagme.Surface with the icon of the window.

        Returns:
            None

        """
        self.caption = caption

    # WINDOW ACTUALIZATION

    def blit(self, object: Surface | str, coordinates: tuple) -> None:
        """
        Blit objects in the window.

        Args:
            object: A pyagme.Surface or text to blit in the window.
            coordinates: A Tuple(int, int) with the coordinates to blit in the window

        Returns:
            None

        """
        self.window.blit(object, coordinates)