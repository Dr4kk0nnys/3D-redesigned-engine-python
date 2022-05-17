import numpy as np

from models.object3D import Object3D
from controllers.blocks import BlocksController


class Block:

    def __init__(self, render, position) -> None:

        block = Object3D(render, np.array([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
                                           (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)]),
                         np.array(
            [(0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (2, 3, 7, 6), (1, 2, 6, 5), (0, 3, 7, 4)]))
        block.translate(position)

        BlocksController().append_block(block)
