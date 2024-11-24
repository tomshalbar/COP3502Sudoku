import pygame
import constants

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        x = self.col * constants.SQUARE_SIZE
        y = self.row * constants.SQUARE_SIZE

        if self.selected:
            #sets to red
            color = constants.RED
        else:
            #sets to black
            color = (0, 0, 0)
            
        pygame.draw.rect(self.screen, color, (x, y, constants.SQUARE_SIZE, constants.SQUARE_SIZE), 2)
        font_size = pygame.font.Font(None, 40)


        if self.value != 0:
            text = font_size.render(str(self.value), True, (0, 0, 0))
            text_rectangle = text.get_rect(center=(x + constants.SQUARE_SIZE // 2, y + constants.SQUARE_SIZE // 2))
            self.screen.blit(text, text_rectangle)

        elif self.sketched_value != 0:
            text = font_size.render(str(self.sketched_value), True, (128, 128, 128))
            text_rectangle = text.get_rect(center=(x + constants.SQUARE_SIZE // 2, y + constants.SQUARE_SIZE // 2))
            self.screen.blit(text, text_rectangle)
