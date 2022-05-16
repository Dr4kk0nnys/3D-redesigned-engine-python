import math
import numpy as np


def view(render, position):
    position = np.array([*position, 1.0])
    forward = np.array([0, 0, 1, 1])
    up = np.array([0, 1, 0, 1])
    right = np.array([1, 0, 0, 1])
    h_fov = math.pi / 3
    v_fov = h_fov * (render.HEIGHT / render.WIDTH)
    near_plane = 0.1
    far_plane = 100


def translate_matrix(position):
    x, y, z, w = position

    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0],
        [-x, -y, -z, 1]
    ])


def rotate_matrix(right, forward, up):
    rx, ry, rz, w = right
    fx, fy, fz, w = forward
    ux, uy, uz, w = up

    return np.array([
        [rx, ux, fx, 0],
        [ry, uy, fy, 0],
        [rz, uz, fz, 0],
        [0, 0, 0, 1]
    ])


def camera_matrix():
    return translate_matrix() @ rotate_matrix()
