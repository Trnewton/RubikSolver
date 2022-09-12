from curses.ascii import FF
from dataclasses import dataclass
from enum import IntEnum, Enum

import numpy as np

col_2_str = [
    'g',
    'r',
    'w',
    'o',
    'y',
    'b',
]


#### Classes ####
def edge_orientatoin(face_1, face_2):
    pass


#### Classes ####

class Colour(IntEnum):
    GREEN = 0
    RED = 1
    WHITE = 2
    ORANGE = 3
    YELLOW = 4
    BLUE = 5

class Face(IntEnum):
    U = 0
    L = 1
    F = 2
    R = 3
    B = 4
    D = 5

class EdgeIdx(IntEnum):
    UF = FU = 0
    UB = BU = 1
    UL = LU = 2
    UR = RU = 3
    DF = FD = 4
    DB = BD = 5
    DL = LD = 6
    DR = RD = 7
    FL = LF = 8
    FR = RF = 9
    BL = LB = 10
    BR = RB = 11

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

col_2_adj: list = [
    [0,3,1,2], # g
    [3,4,2,5], # r
    [0,4,1,5], # w
    [2,4,3,5], # o
    [1,4,0,5], # y
    [0,2,1,3], # b
]


edge_idxs = (
    ((Face.U, 0, 1), (Face.F, 0, 1)), #UF
    ((Face.U, 1, 0), (Face.B, 0, 1)), #UB
    ((Face.U, 1, 2), (Face.L, 0, 1)), #UL
    ((Face.U, 2, 1), (Face.R, 0, 1)), #UR

    ((Face.D, 0, 1), (Face.F, 2, 1)), #DF
    ((Face.D, 2, 1), (Face.B, 2, 1)), #DB
    ((Face.D, 1, 0), (Face.L, 2, 1)), #DL
    ((Face.D, 1, 2), (Face.R, 2, 1)), #DR

    ((Face.F, 1, 0), (Face.L, 1, 2)), #FL
    ((Face.F, 1, 2), (Face.R, 1, 0)), #FR
    ((Face.B, 1, 2), (Face.L, 1, 0)), #BL
    ((Face.B, 1, 0), (Face.R, 1, 2)), #BR
)

corner_idxs = [

]

class RubikCube:
    '''Represents orientation of Rubik cube.'''
    faces: list[np.array]

    def __init__(self, faces) -> None:
        ''''''
        self.faces = np.array(sorted(faces, key=lambda f: f[1][1]), dtype=Colour)
        self.orientations = np.zeros((6,3,3))
        self._set_orientations()

    def rotate_face(self, face:Face, rotation:int) -> None:
        ''''''

        # rotate sides
        store = []
        for adj_face in col_2_adj[face]:
            side = col_2_adj[adj_face].index(face)

            if side == 0: # left
                column = np.flip(self.faces[adj_face][:,0].copy())
                column_ori = np.flip(self.orientations[adj_face][:,0].copy())
                store.append([side, column, column_ori])
            elif side == 1: # top
                row = self.faces[adj_face][0].copy()
                row_ori = self.orientations[adj_face][0].copy()
                store.append([side, row, row_ori])
            elif side == 2: # right
                column = np.flip(self.faces[adj_face][:,2].copy())
                column_ori = np.flip(self.orientations[adj_face][:,2].copy())
                store.append([side, column, column_ori])
            elif side == 3: # bottom
                row = self.faces[adj_face][2].copy()
                row_ori = self.orientations[adj_face][2].copy()
                store.append([side, row, row_ori])

        for n, adj_face in enumerate(col_2_adj[face]):
            _, face_vec, ori_vec = store[(n-rotation)%4].copy()
            side, _ = store[n]
            if side == 0: # left
                self.faces[adj_face][:,0] = face_vec
                self.orientations[adj_face][:,0] = ori_vec
            elif side == 1: # top
                self.faces[adj_face][0] = face_vec
                self.orientations[adj_face][0] = ori_vec
            elif side == 2: # right
                self.faces[adj_face][:,2] = face_vec
                self.orientations[adj_face][:,2] = ori_vec
            elif side == 3: # bottom
                self.faces[adj_face][2] = face_vec
                self.orientations[adj_face][2] = ori_vec

        # rotate face
        self.faces[face] = np.rot90(self.faces[face], k=-rotation)
        self.orientations[face] = np.rot90(self.orientations[face], k=-rotation)

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
            case Twist.D:
                self.rotate_face(Face.D, 1)
            case Twist.D2:
                self.rotate_face(Face.D, 2)
            case Twist.DP:
                self.rotate_face(Face.D, -1)

        return self

    def get_col(self, face, x, y) -> str:
        ''''''

        return self.faces[face][x,y]

    def print(self):
        ''''''
        # TODO: Make print in cuibe layout
        for face in self.faces:
            print(face)

    def __str__(self):
        name = ''
        for row in self.faces[Face.U]:
            name += f'\t|{"|".join(col_2_str[r] if isinstance(r, Colour) else r for r in row)}|\n'
        name += '\t-------\n'

        for n in range(3):
            name += f'|{"|".join(col_2_str[r] if isinstance(r, Colour) else r for r in self.faces[Face.L][n])}|'
            name += f'\t|{"|".join(col_2_str[r] if isinstance(r, Colour) else r for r in self.faces[Face.F][n])}|'
            name += f'\t|{"|".join(col_2_str[r] if isinstance(r, Colour) else r for r in self.faces[Face.R][n])}|'
            name += f'\t|{"|".join(col_2_str[r] if isinstance(r, Colour) else r for r in self.faces[Face.B][n])}|\n'

        name += '\t-------\n'

        for row in self.faces[Face.D]:
            name += f'\t|{"|".join(col_2_str[r] if isinstance(r, Colour) else r for r in row)}|\n'

        return name

    def copy(self):
        return RubikCube(self.faces.copy())

@dataclass
class Edge:
    orientation: int
    face_1: Colour
    face_2: Colour

@dataclass
class Corner:
    orientation: int
    face_1: Colour
    face_2: Colour
    face_3: Colour

face_2_edges = (
    (EdgeIdx.UB, EdgeIdx.UR, EdgeIdx.UF, EdgeIdx.UL),   #U
    (EdgeIdx.LU, EdgeIdx.LF, EdgeIdx.LD, EdgeIdx.LB),   #L
    (EdgeIdx.FU, EdgeIdx.FR, EdgeIdx.FD, EdgeIdx.FL),   #F
    (EdgeIdx.RU, EdgeIdx.RB, EdgeIdx.RD, EdgeIdx.RF),   #R
    (EdgeIdx.BU, EdgeIdx.BL, EdgeIdx.BD, EdgeIdx.BR),   #B
    (EdgeIdx.DF, EdgeIdx.DR, EdgeIdx.DB, EdgeIdx.DL)    #D
)


def edge_orientation(c1, c2):
    if c1 is Colour.RED or c1 is Colour.ORANGE:
        return 1

    if c1 is Colour.WHITE or c1 is Colour.YELLOW:
        if c2 is Colour.BLUE or c2 is Colour.GREEN:
            return 1

    return 0

def corner_orientation():
    pass

class RubikCubeIndex:
    def __init__(self, faces) -> None:
        self.edges = []
        self.corners = []
        self.centers = []

        # Read Centers
        for i in range(6):
            self.centers.append(faces[i][1][1])

        # Read Edges
        for f1, f2 in edge_idxs:
            c1 = faces[f1[0]][f1[1]][f1[2]]
            c2 = faces[f2[0]][f2[1]][f2[2]]

            ori = edge_orientation(c1, c2)
            if ori == 0:
                self.edges.append(Edge(ori, c1, c2))
            else:
                self.edges.append(Edge(ori, c2, c1))

        # Read Corners
        for f1, f2, f3 in corner_idxs:
            c1 = faces[f1]
            c2 = faces[f2]
            c3 = faces[f3]

            ori = corner_orientation(c1, c2, c3)
            if ori == 0:
                self.corners.append(Corner(ori, c1, c2, c3))
            elif ori == 1:
                self.corners.append(Corner(ori, c2, c3, c1))
            else:
                self.corners.append(Corner(ori, c3, c1, c2))

    def rotate_face(self, face: Face, rot: int) -> None:
        # Rotate Edges
        idxs = face_2_edges[face]
        self.edges[idxs[0]], self.edges[idxs[1]], \
        self.edges[idxs[2]], self.edges[idxs[3]] \
            = self.edges[idxs[-(rot)%4]], self.edges[idxs[-(1+rot)%4]],\
            self.edges[idxs[-(2+rot)%4]], self.edges[idxs[-(3+rot)%4]]

        # Edge Orientations
        if (face is Face.F or face is Face.B) and (rot % 2) != 0:
            for idx in idxs:
                self.edges[idx].orientation = (self.edges[idx].orientation + 1) % 2


        # Rotate Corners
        # TODO:

        # Corner Orientations
        # TODO:


    def __str__(self) -> str:
        pass