from chess_items import *
from game_config import *

clock = pg.time.Clock()
screen = pg.display.set_mode(WINDOW_SIZE)
screen.fill(BACKGROUND)

chessboard = Chessboard(screen)

# main game loop
run = True
if __name__ == '__main__':
    while run:
        # regulate the frame rate
        clock.tick(FPS)
        # check for events
        for event in pg.event.get():
            # if the user clicks the close button
            if event.type == pg.QUIT:
                # exit the game
                pg.quit()
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                chessboard.btn_down(event.button,event.pos)
            if event.type == pg.MOUSEBUTTONUP:
                chessboard.btn_up(event.button,event.pos)
            if event.type == pg.MOUSEMOTION:
                chessboard.drad(event.pos)
            if event.type == pg.KEYUP:
                chessboard.key_up(event)
            if event.type == pg.KEYDOWN:
                chessboard.key_down(event)
