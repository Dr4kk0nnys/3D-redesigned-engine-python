import numpy as np

from data.models.object3D import Object3D
from data.controllers.blocks import BlocksController


class Block:

    def __init__(self, position) -> None:

        block = Object3D(self, np.array([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
                                         (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)]),
                         np.array(
            [(0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (2, 3, 7, 6), (1, 2, 6, 5), (0, 3, 7, 4)]))
        block.translate(position)

        BlocksController().append_block(block)
