import pygame as pg

from data.models.object3D import Object3D

from data.camera.camera import *
from data.camera.projection import *


class Render:
    def __init__(self):
        pg.init()

        """ TODO: Configurations """
        self.RES = self.WIDTH, self.HEIGHT = 900, 600
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.object = Object3D(self)
        self.object.translate([0.2, 0.4, 0.2])
        self.object.rotate_y(math.pi / 6)

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        self.object.draw()

    def run(self):
        while True:
            self.draw()
            self.camera.control()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]

            """ TODO: Fps counter """
            pg.display.set_caption(f'{str(self.clock.get_fps())[0:2]} fps')

            pg.display.flip()

            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = Render()
    app.run()
