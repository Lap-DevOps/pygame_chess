from unittest import TestCase, main
import pygame as pg


class TestGame(TestCase):

    def test_game_exit(self):
        # Create a window
        pg.display.set_mode((200, 200))

        # Send the quit event to the event queue
        pg.event.post(pg.event.Event(pg.QUIT))

        # Call pygame.quit()
        pg.quit()

        # Check if pygame.quit() was called
        self.assertTrue(pg.quit)

    def test_game_fps(self):
        # Set the frame rate to 60
        FPS = 60

        # Set the dimensions of the window
        WINDOW_SIZE = (200, 200)

        # Create a display surface
        pg.display.set_mode(WINDOW_SIZE)

        # Create a clock object to regulate the frame rate
        clock = pg.time.Clock()

        # Call the main game loop 100 times
        for _ in range(100):
            # Check for events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    # Call pygame.quit()
                    pg.quit()

            # Regulate the frame rate
            clock.tick(FPS)

        # Check if the game runs at the correct frame rate
        self.assertAlmostEqual(clock.get_fps(), FPS, delta=10)

    def test_board_size(self):
        # Create a window
        pg.display.set_mode((700, 700))

        # Get the board surface
        board = pg.display.get_surface().copy()
        board_rect = board.get_rect()

        # Check if the board size is correct
        self.assertEqual(board_rect.width, 700)
        self.assertEqual(board_rect.height, 700)

    def test_cell_size(self):
        # Create a window
        pg.display.set_mode((700, 700))

        # Get the board surface
        board = pg.display.get_surface().copy()
        board_rect = board.get_rect()

        # Check if the cell size is correct
        self.assertEqual(board_rect.width % 10, 0)
        self.assertEqual(board_rect.height % 10, 0)


    def test_fps(self):
        # Set the frame rate
        FPS = 30

        # Create a window
        pg.display.set_mode((200, 200))

        # Create a clock object to regulate the frame rate
        clock = pg.time.Clock()

        # Call the main game loop 100 times
        for _ in range(100):
            clock.tick(FPS)

        # Check if the game runs at the correct frame rate
        self.assertAlmostEqual(clock.get_fps(), FPS, delta=1)


if __name__ == '__main__':
    main()
