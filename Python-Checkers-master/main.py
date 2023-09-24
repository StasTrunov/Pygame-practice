# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from checkers.constants import WIDTH, HEIGHT, GREY, SQUARE_SIZE, RED, WHITE
from checkers.board import Board
from checkers.game import Game


FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
pygame.init()


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col



def main():
    board = Board()
    run = True
    clock = pygame.time.Clock()
    piece = board.get_piece(0,1)
    game = Game(WIN)
 

    while run:
        clock.tick(FPS)

        if game.winner() == RED:
            print('RED WINS')
            break

        if game.winner() == WHITE:
            print('WHITE WINS')
            break


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)



        game.update()


    pygame.quit()
        

        



main()