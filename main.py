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
    screen.fill(BG_COLOR)
    welcome_picture = pygame.image.load(WELCOME_BG_IMAGE).convert()
    welcome_picture = pygame.transform.scale(welcome_picture, (WIDTH,  HEIGHT + SQUARE_SIZE))
    welcome_font = pygame.font.Font(None, WELCOME_FONT)
    select_mode_font = pygame.font.Font(None, MODE_FONT)

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
    screen.fill(BG_COLOR)
    welcome_picture = pygame.image.load(WELCOME_BG_IMAGE).convert()
    welcome_picture = pygame.transform.scale(welcome_picture, (WIDTH,  HEIGHT + SQUARE_SIZE))
    game_over_font = pygame.font.Font(None, GAME_OVER_FONT)



    game_over_surf = game_over_font.render("Game Over :(", 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))


    screen.blit(welcome_picture, (0, 0))
    screen.blit(game_over_surf, game_over_rect)


    restart_surf, restart_rect = create_welcome_buttons("Restart", WIDTH // 1.5 - 50)


    screen.fill(BUTTON_FILL_COLOR, restart_rect, special_flags=0)

    screen.blit(restart_surf, restart_rect)

    return restart_rect

def game_in_progress_screen(screen, mistakes):

    x = 1
    mistakes_surf = pygame.font.Font(None, 30).render(f"Mistakes: {str(mistakes)}/5", 0, (0,0,0))
    mistakes_rect = mistakes_surf.get_rect(center=(SQUARE_SIZE * 2, HEIGHT + SQUARE_SIZE // 2))
    screen.blit(mistakes_surf, mistakes_rect)

    restart_surf = pygame.font.Font(None, 30).render(f"Restart", 0, (0, 0, 0))
    restart_rect = restart_surf.get_rect(center=(SQUARE_SIZE*4.5, HEIGHT + SQUARE_SIZE // 2))
    screen.fill(BUTTON_FILL_COLOR, restart_rect, special_flags=0)
    screen.blit(restart_surf, restart_rect)

    exit_surf = pygame.font.Font(None, 30).render(f"exit", 0, (0, 0, 0))
    exit_rect = exit_surf.get_rect(center=(SQUARE_SIZE * 8, HEIGHT + SQUARE_SIZE // 2))
    screen.fill(BUTTON_FILL_COLOR, exit_rect, special_flags=0)
    screen.blit(exit_surf, exit_rect)


    reset_surf = pygame.font.Font(None, 30).render(f"Reset", 0, (0, 0, 0))
    reset_rect = reset_surf.get_rect(center=(SQUARE_SIZE * 6.5, HEIGHT + SQUARE_SIZE // 2))
    screen.fill(BUTTON_FILL_COLOR, reset_rect, special_flags=0)
    screen.blit(reset_surf, reset_rect)


    return exit_rect, restart_rect, reset_rect



def game_won(screen):
    screen.fill(BG_COLOR)
    welcome_picture = pygame.image.load(WELCOME_BG_IMAGE).convert()
    welcome_picture = pygame.transform.scale(welcome_picture, (WIDTH,  HEIGHT + SQUARE_SIZE))
    game_over_font = pygame.font.Font(None, GAME_OVER_FONT)



    game_over_surf = game_over_font.render("Game Won!", 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

    screen.blit(welcome_picture, (0, 0))
    screen.blit(game_over_surf, game_over_rect)

    exit_surf, exit_rect = create_welcome_buttons("Exit", WIDTH // 1.5 - 50)

    screen.fill(BUTTON_FILL_COLOR, exit_rect, special_flags=0)

    screen.blit(exit_surf, exit_rect)

    return exit_rect



def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT + SQUARE_SIZE))
    pygame.display.set_caption("Sudoku")
    mode = MODE_START
    run = True
    square_col, square_row = 0, 0
    mistakes = 0

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
            exit_game, restart_game, reset_game = game_in_progress_screen(screen, mistakes)
            game_in_progress_screen(screen, mistakes)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_game.collidepoint(event.pos):
                        run = False

                    if restart_game.collidepoint(event.pos):
                        mistakes = 0
                        mode = MODE_START

                    if reset_game.collidepoint(event.pos):
                        mistakes = 0
                        game_board.reset_to_original()

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
                    if event.key == pygame.K_RETURN and not game_board.cells[square_row][square_col].pre_filled and game_board.cells[square_row][square_col].sketched_value != 0:
                        game_board.cells[square_row][square_col].value = game_board.cells[square_row][square_col].sketched_value
                        if not (game_board.cells[square_row][square_col].value == game_board.complete_sudoku_board[square_row][square_col]):
                            game_board.cells[square_row][square_col].correct = False
                            mistakes += 1
                            if mistakes >= 5:
                                game_board.draw()
                                game_in_progress_screen(screen, mistakes)
                                mode = MODE_END
                                mistakes = 0

                        else:
                            game_board.cells[square_row][square_col].correct = True




                if game_board.is_full() and game_board.check_board():
                    mode = MODE_WON
                elif game_board.is_full():
                    mode = MODE_END


        if mode == MODE_WON:

            exit = game_won(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                   if exit.collidepoint(event.pos):
                       run = False

        if mode == MODE_END:
            restart = game_over(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                   if restart.collidepoint(event.pos):
                       mode = MODE_START

        pygame.display.update()
        # pygame.time.Clock().tick(60)



if __name__ == '__main__':
    main()


