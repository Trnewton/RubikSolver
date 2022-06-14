from dataclasses import dataclass

import numpy as np


#### Classes ####

class RubikCube:
    '''Represents orientation of Rubik cube.'''
    faces: list[np.array]
    col_2_face: dict = {
        'w' : 0,
        'o' : 1,
        'r' : 2,
        'g' : 3,
        'b' : 4,
        'y' : 5
    }

    col_2_adj: list = [
        [1,4,2,3],  # w
        [5,4,0,3],  # o
        [0,4,5,3],  # r
        [1,4,2,3],  # g
        [1,3,2,0],  # b
        [2,4,1,3]   # y
    ]

    def __init__(self, faces) -> None:
        self.faces = [np.array(face, dtype=str) for face in faces]

    def rotate_face(self, face:str, rotation:int) -> None:
        ''''''

        idx = self.col_2_face[face]

        # rotate sides
        for adj_face in self.col_2_adj[idx]:
            side = adj_face.index(idx)

            if side == 0: # right
                pass
            elif side == 1: # top
                pass
            elif side == 2: # left
                pass
            elif side == 3: # bottom
                pass

        # rotate face
        self.col_2_adj[idx] = np.roll(self.col_2_adj[idx], rotation)

    #TODO: Must decide on how referencing for getting face colours works
    def get_col(face, x, y):
        ''''''
        pass

    def print(self):
        ''''''
        pass
