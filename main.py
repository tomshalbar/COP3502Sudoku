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
    easy_surf, easy_rect = create_welcome_buttons("Easy", WIDTH//3- 50)
    medium_surf, medium_rect = create_welcome_buttons("Medium", WIDTH//1.5- 50)
    hard_surf, hard_rect = create_welcome_buttons("Hard", WIDTH//1- 50)
    screen.fill(BUTTON_FILL_COLOR, easy_rect, special_flags=0)
    screen.fill(BUTTON_FILL_COLOR, medium_rect, special_flags=0)
    screen.fill(BUTTON_FILL_COLOR, hard_rect, special_flags=0)
    screen.blit(easy_surf, easy_rect)
    screen.blit(medium_surf, medium_rect)
    screen.blit(hard_surf, hard_rect)

    return easy_rect, medium_rect, hard_rect




def game_over(screen):
    welcome_picture = pygame.image.load(WELCOME_BG_IMAGE).convert()
    welcome_picture = pygame.transform.scale(welcome_picture, (WIDTH, HEIGHT))
    game_over_font = pygame.font.Font(None, GAME_OVER_FONT)


    pygame.display.flip()

    game_over_surf = game_over_font.render("Game Over :(", 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))


    screen.blit(welcome_picture, (0, 0))
    screen.blit(game_over_surf, game_over_rect)


    restart_surf, restart_rect = create_welcome_buttons("Restart", WIDTH // 1.5 - 50)


    screen.fill(BUTTON_FILL_COLOR, restart_rect, special_flags=0)

    screen.blit(restart_surf, restart_rect)

    return restart_rect

def game_in_progress_screen(screen):
    pass

def game_won(screen):
    welcome_picture = pygame.image.load(WELCOME_BG_IMAGE).convert()
    welcome_picture = pygame.transform.scale(welcome_picture, (WIDTH, HEIGHT))
    game_over_font = pygame.font.Font(None, GAME_OVER_FONT)

    pygame.display.flip()

    game_over_surf = game_over_font.render("Game Won!", 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

    screen.blit(welcome_picture, (0, 0))
    screen.blit(game_over_surf, game_over_rect)

    game_won_surf, game_won_rect = create_welcome_buttons("Exit", WIDTH // 1.5 - 50)

    screen.fill(BUTTON_FILL_COLOR, game_won_rect, special_flags=0)

    screen.blit(game_won_surf, game_won_rect)

    return game_won_rect



def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT + SQUARE_SIZE))
    pygame.display.set_caption("Sudoku")
    screen.fill(BG_COLOR)
    mode = MODE_START
    run = True
    square_col, square_row = 0, 0

    while run:
        if mode == MODE_START:

            easy, medium, hard = start_game_screen(screen)
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy.collidepoint(event.pos):
                        game_board = Board(9, 9, screen, difficulty='easy')
                        mode = MODE_PROGRESS
                    elif medium.collidepoint(event.pos):
                        game_board = Board(9, 9, screen, difficulty='medium')
                        mode = MODE_PROGRESS
                    elif hard.collidepoint(event.pos):
                        game_board = Board(9, 9, screen, difficulty='hard')
                        mode = MODE_PROGRESS


        if mode == MODE_PROGRESS:
            game_board.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_board.cells[square_row][square_col].selected = False
                    clicked_x, clicked_y = event.pos
                    if clicked_y < HEIGHT:
                        square_col, square_row = clicked_x // SQUARE_SIZE, clicked_y // SQUARE_SIZE
                        game_board.cells[square_row][square_col].selected = True

                if event.type == pygame.KEYUP:
                    #arrow key movement

                    if event.key == pygame.K_RIGHT and square_col < 8:
                        game_board.cells[square_row][square_col].selected = False
                        square_col, square_row = square_col + 1, square_row
                        game_board.cells[square_row][square_col].selected = True

                    if event.key == pygame.K_LEFT and square_col > 0:
                        game_board.cells[square_row][square_col].selected = False
                        square_col, square_row = square_col - 1, square_row
                        game_board.cells[square_row][square_col].selected = True

                    if event.key == pygame.K_UP and square_row > 0:
                        game_board.cells[square_row][square_col].selected = False
                        square_col, square_row = square_col, square_row - 1
                        game_board.cells[square_row][square_col].selected = True

                    if event.key == pygame.K_DOWN and square_row < 8:
                        game_board.cells[square_row][square_col].selected = False
                        square_col, square_row = square_col, square_row + 1
                        game_board.cells[square_row][square_col].selected = True

                    # check that the input is a num and not a pre-filled square
                    if 48 < event.key < 58 and not game_board.cells[square_row][square_col].pre_filled:
                        game_board.cells[square_row][square_col].sketched_value = event.key - 48
                    if event.key == pygame.K_BACKSPACE and not game_board.cells[square_row][square_col].pre_filled:
                        game_board.cells[square_row][square_col].sketched_value = 0
                        game_board.cells[square_row][square_col].value = 0
                    if event.key == pygame.K_RETURN and not game_board.cells[square_row][square_col].pre_filled:
                        game_board.cells[square_row][square_col].value = game_board.cells[square_row][square_col].sketched_value


                if game_board.is_full() and game_board.check_board():
                    mode = MODE_WON
                elif game_board.is_full():
                    mode = MODE_END


        if mode == MODE_WON:
            won = game_won(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                   if won.collidepoint(event.pos):
                       run = False

        if mode == MODE_END:
            restart = game_over(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = Falseeasy, medium, hard = start_game_screen(screen)

                if event.type == pygame.MOUSEBUTTONDOWN:
                   if restart.collidepoint(event.pos):
                       print("Restart")
                       mode = MODE_START

        pygame.display.update()






if __name__ == '__main__':
    main()


