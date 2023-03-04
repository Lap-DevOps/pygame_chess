import pygame as pg

from game_config import *

pg.init()
fnt_num = pg.font.Font(FNT_PTH, FNT_SIZE)


class Chessboard:
    def __init__(self, parent_surface: pg.Surface,
                 cell_qty: int = CELL_QTY, cell_size: int = CELL_SIZE):
        self.__screen = parent_surface
        self.__prepare_screen()
        self.__draw_playboard(cell_qty, cell_size)
        pg.display.update()

    def __draw_playboard(self, cell_qty, cell_size):
        total_width = cell_qty * cell_size
        num_fields = self.__create_num_fields(cell_qty, cell_size)
        fields = self.__create_all_cells(cell_qty, cell_size)
        num_fields_depth = num_fields[0].get_width()
        playboard_view = pg.Surface((
            2 * num_fields_depth + total_width,
            2 * num_fields_depth + total_width
        )).convert_alpha()

        back_img = pg.image.load(IMG_PATH + BOARD_BG_IMG)
        back_img = pg.transform.scale(back_img, (playboard_view.get_width(), playboard_view.get_height()))
        playboard_view.blit(back_img, back_img.get_rect())

        playboard_view.blit(num_fields[0],
                            (0, num_fields_depth))
        playboard_view.blit(num_fields[0],
                            (num_fields_depth + total_width, num_fields_depth))
        playboard_view.blit(num_fields[1],
                            (num_fields_depth, 0))
        playboard_view.blit(num_fields[1],
                            (num_fields_depth, num_fields_depth + total_width))
        playboard_view.blit(fields,
                            (num_fields_depth, num_fields_depth))

        playboard_rect = playboard_view.get_rect()
        playboard_rect.x += (self.__screen.get_width() - playboard_rect.width) // 2
        playboard_rect.y += (self.__screen.get_height() - playboard_rect.height) // 2
        self.__screen.blit(playboard_view, playboard_rect)

    def __create_num_fields(self, cell_qty, cell_size):
        n_lines = pg.Surface((cell_qty * cell_size, cell_size // 3)).convert_alpha()
        n_rows = pg.Surface((cell_size // 3, cell_qty * cell_size)).convert_alpha()
        for i in range(0, cell_qty):
            letter = fnt_num.render(LTRS[i], 1, WHITE)
            number = fnt_num.render(str(cell_qty - i), 1, WHITE)
            n_lines.blit(letter, (
                i * cell_size + (cell_size - letter.get_rect().width) // 2,
                (n_lines.get_height() - letter.get_rect().height) // 2
            ))
            n_rows.blit(number, (
                (n_rows.get_width() - letter.get_rect().width) // 2,
                i * cell_size + (cell_size - number.get_rect().height) // 2
            ))

        return (n_rows, n_lines)

    def __create_all_cells(self, cell_qty, cell_size):
        fields = pg.Surface((cell_qty * cell_size, cell_qty * cell_size)).convert_alpha()
        is_even_qty = (cell_qty % 2 == 0)
        cell_color_index = 1 if is_even_qty else 0
        for y in range(cell_qty):
            for x in range(cell_qty):
                cell = pg.image.load(IMG_PATH + COLORS[cell_color_index])
                cell = pg.transform.scale(cell, (cell_size, cell_size))
                fields.blit(cell, (x * cell_size, y * cell_size))
                cell_color_index ^= True
            cell_color_index = cell_color_index ^ True if (is_even_qty) else cell_color_index
        return fields

    def __prepare_screen(self):
        back_img = pg.image.load(IMG_PATH + WIM_BG_IMG)
        back_img = pg.transform.scale(back_img, WINDOW_SIZE)
        self.__screen.blit(back_img, (0, 0))