import pygame as pg

import board_data
from game_config import *
from pieces import *

pg.init()
fnt_num = pg.font.Font(FNT_PTH, FNT_SIZE)


class Chessboard:
    def __init__(self, parent_surface: pg.Surface,
                 cell_qty: int = CELL_QTY, cell_size: int = CELL_SIZE):
        self.__screen = parent_surface
        self.__table = board_data.board
        self.__qty = cell_qty
        self.__size = cell_size
        self.__pieces_types = PIECES_TYPES
        self.__all_cells = pg.sprite.Group()
        self.__all_pieces = pg.sprite.Group()
        self.__prepare_screen()
        self.__draw_playboard()
        self.__draw_all_pieses()
        pg.display.update()

    def __draw_playboard(self, ):
        total_width = self.__qty * self.__size
        num_fields = self.__create_num_fields()
        self.__all_cells = self.__create_all_cells()

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

        playboard_rect = playboard_view.get_rect()
        playboard_rect.x += (self.__screen.get_width() - playboard_rect.width) // 2
        playboard_rect.y += (self.__screen.get_height() - playboard_rect.height) // 2
        self.__screen.blit(playboard_view, playboard_rect)
        cells_offsets = (
            playboard_rect.x + num_fields_depth,
            playboard_rect.y + num_fields_depth
        )
        self.__draw_cells_on_playboard(cells_offsets)

    def __create_num_fields(self):
        n_lines = pg.Surface((self.__qty * self.__size, self.__size // 3)).convert_alpha()
        n_rows = pg.Surface((self.__size // 3, self.__qty * self.__size)).convert_alpha()
        for i in range(0, self.__qty):
            letter = fnt_num.render(LTRS[i], 1, WHITE)
            number = fnt_num.render(str(self.__qty - i), 1, WHITE)
            n_lines.blit(letter, (
                i * self.__size + (self.__size - letter.get_rect().width) // 2,
                (n_lines.get_height() - letter.get_rect().height) // 2
            ))
            n_rows.blit(number, (
                (n_rows.get_width() - letter.get_rect().width) // 2,
                i * self.__size + (self.__size - number.get_rect().height) // 2
            ))

        return (n_rows, n_lines)

    def __create_all_cells(self, ):
        group = pg.sprite.Group()
        fields = pg.Surface((self.__qty * self.__size, self.__qty * self.__size)).convert_alpha()
        is_even_qty = (self.__qty % 2 == 0)
        cell_color_index = 1 if is_even_qty else 0
        for y in range(self.__qty):
            for x in range(self.__qty):
                cell = Cell(cell_color_index, self.__size, (x, y), LTRS[x] + str(self.__qty - y))
                group.add(cell)
                cell_color_index ^= True
            cell_color_index = cell_color_index ^ True if (is_even_qty) else cell_color_index
        return group

    def __prepare_screen(self):
        back_img = pg.image.load(IMG_PATH + WIM_BG_IMG)
        back_img = pg.transform.scale(back_img, WINDOW_SIZE)
        self.__screen.blit(back_img, (0, 0))

    def __draw_cells_on_playboard(self, cells_offsets):
        for cell in self.__all_cells:
            cell.rect.x += cells_offsets[0]
            cell.rect.y += cells_offsets[1]
        self.__all_cells.draw(self.__screen)

    def __draw_all_pieses(self):
        self.__setup_board()
        self.__all_pieces.draw(self.__screen)

    def __setup_board(self):
        for j, row in enumerate(self.__table):
            for i, field_value in enumerate(row):
                if field_value != 0:
                    piece = self.__create_piece(field_value, (j, i))
                    self.__all_pieces.add(piece)
        for piece in self.__all_pieces:
            for cell in self.__all_cells:
                if piece.field_name == cell.field_name:
                    piece.rect = cell.rect

    def __create_piece(self, piece_symbol: str, table_coord: tuple):
        field_name = self.__to_field_name(table_coord)
        piece_tuple = self.__pieces_types[piece_symbol]

        classname = globals()[piece_tuple[0]]

        return classname(self.__size, piece_tuple[1], field_name)

    def __to_field_name(self, table_coord: tuple):
        return LTRS[table_coord[1]] + str(self.__qty - table_coord[0])


class Cell(pg.sprite.Sprite):
    def __init__(self, color_index: int, size: int, coords: tuple, name: str, ):
        super().__init__()
        x, y = coords
        self.color = color_index
        self.field_name = name
        self.image = pg.image.load(IMG_PATH + COLORS[color_index])
        self.image = pg.transform.scale(self.image, (size, size))
        self.rect = pg.Rect(x * size, y * size, size, size)
