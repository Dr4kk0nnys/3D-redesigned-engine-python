import pygame as pg

from render import draw


if __name__ == '__main__':
    pg.init()

    # TODO: Configurations
    screen = pg.display.set_mode((900, 600))
    clock = pg.time.Clock()

    # Main game loop
    while True:
        draw(screen, pg.Color('darkslategray'))

        [exit() for i in pg.event.get() if i.type == pg.QUIT]

        # TODO: FPS counter
        pg.display.set_caption(str(clock.get_fps())[0:2])

        pg.display.flip()

        # TODO: FPS tick
        clock.tick(60)
