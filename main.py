import pygame
from cell import *
from board import *
from sudoku_generator import *
from constants import *


def generate_sudoku(size, removed) -> list[list]:
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    original_board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    sudoku.print_board()
    return board
def create_welcome_buttons(text, width):
    button_font = pygame.font.Font(None, BUTTON_FONT)
    button_surf = button_font.render(text, 0, BUTTON_FONT_COLOR)
    button_rect = button_surf.get_rect(center=(width, HEIGHT // 1.2 - 50))

    return button_surf, button_rect


def start_game_screen(screen):
    welcome_picture = pygame.image.load(WELCOME_BG_IMAGE).convert()
    welcome_picture = pygame.transform.scale(welcome_picture, (WIDTH, HEIGHT))
    welcome_font = pygame.font.Font(None, WELCOME_FONT)
    select_mode_font = pygame.font.Font(None, MODE_FONT)

    pygame.display.flip()



    welcome_surf = welcome_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    welcome_rect = welcome_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    mode_surf = select_mode_font.render("Select mode", 0, LINE_COLOR)
    mode_rect = mode_surf.get_rect(center=(WIDTH // 2, HEIGHT // 1.5 - 50))

    screen.blit(welcome_picture, (0, 0))
    screen.blit(welcome_surf, welcome_rect)
    screen.blit(mode_surf, mode_rect)
    x, y = create_welcome_buttons("Easy", WIDTH//3- 50)
    a, b = create_welcome_buttons("Medium", WIDTH//1.5- 50)
    c, d = create_welcome_buttons("Hard", WIDTH//1- 50)
    screen.fill(BUTTON_FILL_COLOR, y, special_flags=0)
    screen.fill(BUTTON_FILL_COLOR, b, special_flags=0)
    screen.fill(BUTTON_FILL_COLOR, d, special_flags=0)
    screen.blit(x,y)
    screen.blit(a, b)
    screen.blit(c, d)









def game_over():
    pass

def game_won():
    pass
def game_screen():
    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill(BG_COLOR)
    board = Board(10, 10, screen, difficulty='medium')

    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        start_game_screen(screen)
        # board.draw()
        pygame.display.update()

        pygame.time.Clock().tick(60)






if __name__ == '__main__':
    main()


