import numpy as np
import pygame as pg

from utils import matrix_functions


class Object3D:
    def __init__(self, render, vertexes, faces):
        self.render = render
        self.vertexes = np.array([np.array(v) for v in vertexes])
        self.faces = np.array([np.array(face) for face in faces])

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        vertexes = self.vertexes @ self.render.camera.camera_matrix()
        vertexes = vertexes @ self.render.projection.projection_matrix
        vertexes /= vertexes[:, -1].reshape(-1, 1)
        vertexes[(vertexes > 2) | (vertexes < -2)] = 0
        vertexes = vertexes @ self.render.projection.to_screen_matrix
        vertexes = vertexes[:, :2]

        half_width, half_height = self.render.configs['half_width'], self.render.configs['half_height']

        for face in self.faces:
            polygon = vertexes[face]

            if not np.any((polygon == half_width) | (polygon == half_height)):
                pg.draw.polygon(self.render.screen,
                                pg.Color('orange'), polygon, 3)

        for vertex in vertexes:
            if not np.any((vertex == half_width) | (vertex == half_height)):
                pg.draw.circle(self.render.screen,
                               pg.Color('white'), vertex, 6)

    def translate(self, pos):
        self.vertexes = self.vertexes @ matrix_functions.translate(pos)

    def scale(self, scale_to):
        self.vertexes = self.vertexes @ matrix_functions.scale(scale_to)

    def rotate_x(self, angle):
        self.vertexes = self.vertexes @ matrix_functions.rotate_x(angle)

    def rotate_y(self, angle):
        self.vertexes = self.vertexes @ matrix_functions.rotate_y(angle)

    def rotate_z(self, angle):
        self.vertexes = self.vertexes @ matrix_functions.rotate_z(angle)
