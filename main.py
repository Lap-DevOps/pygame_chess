import pygame as pg

# initialize pygame modules
pg.init()

# create a clock object to regulate the frame rate
clock = pg.time.Clock()

# set the frame rate
FPS = 10

# settings  of the window
WINDOW_SIZE = (700, 700)
BACKGROUND = (150, 90, 30)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
MID_GREY = (90, 90, 90)
YELLOW = (255, 255, 0)
CELL_QTY = 8
CELL_SIZE = 70
COLORS = (BLACK, WHITE)
FNT18 = pg.font.Font('assets/fonts/Arial.ttf', 18)
FNT28 = pg.font.Font('assets/fonts/Arial.ttf', 28)
LTRS = 'abcdefghijklmnopqrstuvwxyz'

# create a display surface
screen = pg.display.set_mode(WINDOW_SIZE)

screen.fill(BACKGROUND)
n_lines = pg.Surface((CELL_QTY * CELL_SIZE, CELL_SIZE // 2)).convert_alpha()
n_rows = pg.Surface((CELL_SIZE // 2, CELL_QTY * CELL_SIZE)).convert_alpha()
fields = pg.Surface((CELL_QTY * CELL_SIZE, CELL_QTY * CELL_SIZE)).convert_alpha()
board = pg.Surface((
    2 * n_rows.get_width() + fields.get_width(),
    2 * n_lines.get_height() + fields.get_height()
)).convert_alpha()

is_even_qty = (CELL_QTY % 2 == 0)
cell_color_index = 1 if (is_even_qty) else 0
for y in range(CELL_QTY):
    for x in range(CELL_QTY):
        # pg.draw.rect(screen, COLORS[cell_color_index], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        cell = pg.Surface((CELL_SIZE, CELL_SIZE))
        cell.fill(COLORS[cell_color_index])

        cell_name = FNT28.render(LTRS[x] + str(CELL_QTY - y), 0, MID_GREY)
        cell.blit(cell_name, (
            (CELL_SIZE - cell_name.get_rect().width) // 2,
            (CELL_SIZE - cell_name.get_rect().height) // 2
        ))
        fields.blit(cell, (x * CELL_SIZE, y * CELL_SIZE))
        cell_color_index ^= True
    cell_color_index = cell_color_index ^ True if is_even_qty else cell_color_index
for i in range(0, CELL_QTY):
    letter = FNT18.render(LTRS[i], 1, WHITE)
    number = FNT18.render(str(CELL_QTY - i), 1, WHITE)
    n_lines.blit(letter, (
        i * CELL_SIZE + (CELL_SIZE - letter.get_rect().width) // 2,
        (n_lines.get_height() - letter.get_rect().height) // 2
    ))
    n_rows.blit(number, (
        (n_rows.get_width() - letter.get_rect().width) // 2,
        i * CELL_SIZE + (CELL_SIZE - number.get_rect().height) // 2
    ))

board.blit(n_rows, (0, n_lines.get_height()))
board.blit(n_rows, (n_rows.get_width() + fields.get_width(), n_lines.get_height()))
board.blit(n_lines, (n_rows.get_width(), 0))
board.blit(n_lines, (n_rows.get_width(), n_rows.get_width() + fields.get_width()))
board.blit(fields, (n_rows.get_width(), n_lines.get_height()))
screen.blit(board, (
    (WINDOW_SIZE[0] - board.get_width()) // 2,
    (WINDOW_SIZE[1] - board.get_height()) // 2
))
pg.display.update()

# set the run variable to True
run = True

# main game loop
if __name__ == '__main__':
    while run:
        # check for events
        for event in pg.event.get():
            # if the user clicks the close button
            if event.type == pg.QUIT:
                # exit the game
                pg.quit()
                run = False

        # regulate the frame rate
        clock.tick(FPS)
