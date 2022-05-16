import pygame as pg

from data.models.object3D import Object3D

from data.camera.camera import *
from data.camera.projection import *

from data.configurations.configs import Configurations


class Render:
    def __init__(self):
        pg.init()

        self.configs = Configurations().configs

        width, height = self.configs['width'], self.configs['height']
        self.screen = pg.display.set_mode((width, height))

        self.clock = pg.time.Clock()

        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self)
        self.projection = Projection(self)
        self.object = Object3D(self)
        # self.object.translate([0.2, 0.4, 0.2])
        # self.object.rotate_y(math.pi / 6)

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

            self.clock.tick(self.configs['fps'])


if __name__ == '__main__':
    app = Render()
    app.run()
