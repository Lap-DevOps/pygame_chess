import pygame as pg

# initialize pygame modules
pg.init()

# create a clock object to regulate the frame rate
clock = pg.time.Clock()

# set the frame rate
FPS = 10

# set the dimensions of the window
WINDOW_SIZE = (700, 700)

# create a display surface
pg.display.set_mode(WINDOW_SIZE)

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
