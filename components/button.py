class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.x_pos, self.y_pos= pos[0], pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, None, self.base_color)
        self.image = self.text if image == None else image
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, window):
        if self.image is not None:
            window.blit(self.text, self.text_rect)
        window.blit(self.text, self.text_rect)
    
    def input_check(self, pos):
        if pos[0] in range (self.rect.left, self.rect.right) and pos[1] in range (self.rect.top, self.rect.bottom):
            return True
        return False
    
    def change_color(self, pos):
        if pos[0] in range (self.rect.left, self.rect.right) and pos[1] in range (self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)