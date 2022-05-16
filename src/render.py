import numpy as np
from utils import matrix_functions


def draw(screen, color):
    screen.fill(color)


def create_3D_object(render):

    vertexes = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
                        (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)])

    faces = np.array([(0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1),
                     (2, 3, 7, 6), (1, 2, 6, 5), (0, 3, 7, 4)])


def screen_projection(vertexes, render):
    vertexes = vertexes @ render.camera.camera_matrix()


# TODO: Check all those functions, they need to directly change vertexes (inside create_3D_object)
def translate(vertexes, pos):
    vertexes = vertexes @ translate(pos)


def scale(vertexes, scale_to):
    vertexes = vertexes @ scale(scale_to)


def rotate_x(vertexes, angle):
    vertexes = vertexes @ rotate_x(angle)


def rotate_y(vertexes, angle):
    vertexes = vertexes @ rotate_y(angle)


def rotate_z(vertexes, angle):
    vertexes = vertexes @ rotate_z(angle)
