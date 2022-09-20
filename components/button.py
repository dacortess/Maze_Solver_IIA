 # -*- coding: utf-8 -*-
from pygame import Surface
from pygame.font import Font
class Button():
    """ Manage buttons logic."""

    def __init__(self, image: Surface, pos: tuple, text_input: str, font: Font, 
            base_color: str, hovering_color: str, hovering_image: Surface):
        """
        Buttons constructor.

        Args:
            image: A pygame.Surface with the image that represents the button.
            pos: A Tuple(int, int) with the coordinates of the center of the button.
            text_input: A str with the text of the button.
            font: A pygame.font.Font with the font of the text of the button.
            base_color: A str with the color of the text of the button.
            hovering_color: A str with the color of the text of the button when hover it.
            hovering_color: A pygame.Surface with the image of the button when hover it.

        Returns:
            None

        """
        self.x_pos, self.y_pos= pos[0], pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, None, self.base_color)
        self.image = self.text if image == None else image
        self.hovering_image = self.text if hovering_image == None else hovering_image
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    
    # BUTTON ACTUALIZATION

    def input_check(self, pos: tuple) -> bool:
        """
        Check if the coordinates are inside the buttom.

        Args:
            pos: A Tuple(int, int) with the coordinates to check.

        Returns:
            True if is inside, False if not.

        """
        if pos[0] in range (self.rect.left, self.rect.right) and pos[1] in range (self.rect.top, self.rect.bottom):
            return True
        return False

    def update(self, window: Surface, pos: tuple) -> None:
        """
        Updates the button in the window depending the coordinates.

        Args:
            window: A pygame.Surface to update.
            pos: A Tuple(int, int) with the coordinates to evaluate.

        Returns:
            None

        """
        if self.input_check(pos):
            if self.image is not None:
                window.blit(self.hovering_image, self.rect)
            window.blit(self.text, self.text_rect)
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            if self.image is not None:
                window.blit(self.image, self.rect)
            window.blit(self.text, self.text_rect)
            self.text = self.font.render(self.text_input, True, self.base_color)