import constants
import pygame

from constants import LINE_COLOR


class Cell:
    def __init__(self, value, row, col, screen, pre_filled=False, correct = True):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False
        self.pre_filled = pre_filled
        self.correct = correct

    def set_cell_value(self, value):
        """Setter
        for this cell’s value"""
        if not self.pre_filled:
            self.value = value

    def set_sketched_value(self, value):
        """Setter
        for this cell’s sketched value"""
        self.sketched_value = value

    def draw(self):
        """Draws this cell, along with the value inside it.
        If this cell has a nonzero value, that value is displayed.
        Otherwise, no value is displayed in the cell.
        The cell is outlined red if it is currently selected."""
        x = self.col * constants.SQUARE_SIZE
        y = self.row * constants.SQUARE_SIZE

        if self.selected:
            # sets to red
            color = constants.RED
        else:
            # sets to blue
            color = (128, 128, 128)

        pygame.draw.rect(self.screen, color, (x, y, constants.SQUARE_SIZE, constants.SQUARE_SIZE), 2)
        font_size = pygame.font.Font(None, 40)
        sketch_font_size = pygame.font.SysFont(None, 25)

        if self.value != 0 and self.correct:
            text = font_size.render(str(self.value), True, (0, 0, 0))
            text_rectangle = text.get_rect(center=(x + constants.SQUARE_SIZE // 2, y + constants.SQUARE_SIZE // 2))
            self.screen.blit(text, text_rectangle)
        elif self.value != 0 and not self.pre_filled and not self.correct:
            text = font_size.render(str(self.value), True, (255, 0, 0))
            text_rectangle = text.get_rect(center=(x + constants.SQUARE_SIZE // 2, y + constants.SQUARE_SIZE // 2))
            self.screen.blit(text, text_rectangle)
        elif self.sketched_value != 0:
            text = sketch_font_size.render(str(self.sketched_value), True, (128, 128, 128))
            text_rectangle = text.get_rect(center=(x + constants.SQUARE_SIZE // 4, y + constants.SQUARE_SIZE // 4))
            self.screen.blit(text, text_rectangle)

