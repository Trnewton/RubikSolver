from enum import IntEnum, Enum

import numpy as np


#### Classes ####

class Colour(IntEnum):
    WHITE = 0
    ORANGE = 1
    BLUE = 2
    RED = 3
    GREEN = 4
    YELLOW = 5

class Face(IntEnum):
    L = 0
    R = 1
    F = 2
    B = 3
    U = 4
    D = 5

class Twist(IntEnum):
    L = 0
    LP = 1
    L2 = 2
    R = 3
    RP = 4
    R2 = 5
    F = 6
    FP = 7
    F2 = 8
    B = 9
    BP = 10
    B2 = 11
    U = 12
    UP = 13
    U2 = 14
    D = 15
    DP = 16
    D2 = 17

col_2_face = {
    'r' : 0,
    'o' : 1,
    'w' : 2,
    'y' : 3,
    'g' : 4,
    'b' : 5,
}

col_2_adj: list = [
    [2,5,3,4],  # r
    [3,5,2,4],  # o
    [1,5,0,4],  # w
    [0,5,1,4],   # y
    [1,2,0,3],  # g
    [1,3,0,2],  # b
]

class RubikCube:
    '''Represents orientation of Rubik cube.'''
    faces: list[np.array]

    def __init__(self, faces) -> None:
        ''''''
        self.faces = np.array(sorted(faces, key=lambda f: col_2_face[f[1][1]]), dtype=str)

    #TODO: Negative Rotation does not work
    def rotate_face(self, face:Face, rotation:int) -> None:
        ''''''

        # rotate sides
        store = []
        for adj_face in col_2_adj[face]:
            side = col_2_adj[adj_face].index(face)

            if side == 0: # left
                column = np.flip(self.faces[adj_face][:,0].copy())
                store.append([side, column])
            elif side == 1: # top
                row = self.faces[adj_face][0].copy()
                store.append([side, row])
            elif side == 2: # right
                column = np.flip(self.faces[adj_face][:,2].copy())
                store.append([side, column])
            elif side == 3: # bottom
                row = self.faces[adj_face][2].copy()
                store.append([side, row])

        for n, adj_face in enumerate(col_2_adj[face]):
            _, vec = store[(n-rotation)%4].copy()
            side, _ = store[n]
            if side == 0: # left
                self.faces[adj_face][:,0] = vec
            elif side == 1: # top
                self.faces[adj_face][0] = vec
            elif side == 2: # right
                self.faces[adj_face][:,2] = vec
            elif side == 3: # bottom
                self.faces[adj_face][2] = vec

        # rotate face
        self.faces[face] = np.rot90(self.faces[face], k=-rotation)

    def twist(self, twist: Twist):
        match twist:
            # left
            case Twist.L:
                self.rotate_face(Face.L, 1)
            case Twist.L2:
                self.rotate_face(Face.L, 2)
            case Twist.LP:
                self.rotate_face(Face.L, -1)
            # right
            case Twist.R:
                self.rotate_face(Face.R, 1)
            case Twist.R2:
                self.rotate_face(Face.R, 2)
            case Twist.RP:
                self.rotate_face(Face.R, -1)
            # front
            case Twist.F:
                self.rotate_face(Face.F, 1)
            case Twist.F2:
                self.rotate_face(Face.F, 2)
            case Twist.FP:
                self.rotate_face(Face.F, -1)
            # back
            case Twist.B:
                self.rotate_face(Face.B, 1)
            case Twist.B2:
                self.rotate_face(Face.B, 2)
            case Twist.BP:
                self.rotate_face(Face.B, -1)
            # top
            case Twist.U:
                self.rotate_face(Face.U, 1)
            case Twist.U2:
                self.rotate_face(Face.U, 2)
            case Twist.UP:
                self.rotate_face(Face.U, -1)
            # bot
            case Twist.B:
                self.rotate_face(Face.B, 1)
            case Twist.B2:
                self.rotate_face(Face.B, 2)
            case Twist.BP:
                self.rotate_face(Face.B, -1)


    def get_col(self, face, x, y) -> str:
        ''''''

        return self.faces[face][x,y]

    def print(self):
        ''''''
        # TODO: Make print in cuibe layout
        for colour, idx in self.col_2_face.items():
            print(colour)
            print(self.faces[idx])

    def __str__(self):
        name = ''
        for row in self.faces[4]:
            name += f'\t|{"|".join(r for r in row)}|\n'
        name += '\t-------\n'

        for n in range(3):
            name += f'|{"|".join(r for r in self.faces[0][n])}|'
            name += f'\t|{"|".join(r for r in self.faces[2][n])}|'
            name += f'\t|{"|".join(r for r in self.faces[1][n])}|'
            name += f'\t|{"|".join(r for r in self.faces[3][n])}|\n'

        name += '\t-------\n'

        for row in self.faces[5]:
            name += f'\t|{"|".join(r for r in row)}|\n'

        return name