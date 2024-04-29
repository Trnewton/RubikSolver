from dataclasses import dataclass
import dataclasses
from enum import IntEnum, Enum

import numpy as np

#
col_2_str = [
    'g',
    'r',
    'w',
    'o',
    'y',
    'b',
]


#### Function ####
def edge_orientatoin(face_1, face_2):
    pass


#### Classes ####

class Colour(IntEnum):
    ''''''
    GREEN = 0
    RED = 1
    WHITE = 2
    ORANGE = 3
    YELLOW = 4
    BLUE = 5

    def __str__(self) -> str:
        return col_2_str[self]

class Face(IntEnum):
    ''''''
    U = 0
    L = 1
    F = 2
    R = 3
    B = 4
    D = 5

class EdgeIdx(IntEnum):
    ''''''
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

# Indexes for each pair of facelets of each cubie for each edge piece
edge_idxs = (
    ((Face.U, 2, 1), (Face.F, 0, 1)), #UF
    ((Face.U, 0, 1), (Face.B, 0, 1)), #UB
    ((Face.U, 1, 0), (Face.L, 0, 1)), #UL
    ((Face.U, 1, 2), (Face.R, 0, 1)), #UR

    ((Face.D, 0, 1), (Face.F, 2, 1)), #DF
    ((Face.D, 2, 1), (Face.B, 2, 1)), #DB
    ((Face.D, 1, 0), (Face.L, 2, 1)), #DL
    ((Face.D, 1, 2), (Face.R, 2, 1)), #DR

    ((Face.F, 1, 0), (Face.L, 1, 2)), #FL
    ((Face.F, 1, 2), (Face.R, 1, 0)), #FR
    ((Face.B, 1, 2), (Face.L, 1, 0)), #BL
    ((Face.B, 1, 0), (Face.R, 1, 2)), #BR
)

class CornerIdx(IntEnum):
    ''''''
    UFL = ULF = FUL = FLU = LFU = LUF = 0
    UFR = URF = FUR = FRU = RFU = RUF = 1
    DFL = DLF = FDL = FLD = LFD = LDF = 2
    DFR = DRF = FDR = FRD = RFD = RDF = 3

    UBL = ULB = BUL = BLU = LBU = LUB = 4
    UBR = URB = BUR = BRU = RBU = RUB = 5
    DBL = DLB = BDL = BLD = LBD = LDB = 6
    DBR = DRB = BDR = BRD = RBD = RDB = 7

# Indexes for each triplet of facelets of each cubie for each corner piece
corner_idxs = (
    ((Face.U, 2, 0), (Face.F, 0, 0), (Face.L, 0, 2)), # UFL
    ((Face.U, 2, 2), (Face.F, 0, 2), (Face.R, 0, 0)), # UFR
    ((Face.D, 0, 0), (Face.F, 2, 0), (Face.L, 2, 2)), # DFL
    ((Face.D, 0, 2), (Face.F, 2, 2), (Face.R, 2, 0)), # DFR
    ((Face.U, 0, 0), (Face.B, 0, 2), (Face.L, 0, 0)), # UBL
    ((Face.U, 0, 2), (Face.B, 0, 0), (Face.R, 0, 2)), # UBR
    ((Face.D, 2, 0), (Face.B, 2, 2), (Face.L, 2, 0)), # DBL
    ((Face.D, 2, 2), (Face.B, 2, 0), (Face.R, 2, 2)), # DBR
)

# Indicates the order of the facelets on each corner so that we know how a
# clockwise and counter clockwise rotation will shift a corners facelets
corner_order = (
    (Face.U, Face.F, Face.L), # UFL
    (Face.U, Face.R, Face.F), # UFR
    (Face.D, Face.L, Face.F), # DFL
    (Face.D, Face.F, Face.R), # DFR
    (Face.U, Face.L, Face.B), # UBL
    (Face.U, Face.B, Face.R), # UBR
    (Face.D, Face.B, Face.L), # DBL
    (Face.D, Face.R, Face.B), # DBR
)


class Twist(IntEnum):
    ''''''
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

# TODO: There is some really bad coupling going on here, try to remove.
col_2_adj: list = [
    [Face.L, Face.B, Face.R, Face.F], # g/U
    [Face.B, Face.U, Face.F, Face.D], # r/L
    [Face.L, Face.U, Face.R, Face.D], # w/F
    [Face.F, Face.U, Face.B, Face.D], # o/R
    [Face.R, Face.U, Face.L, Face.D], # y/B
    [Face.L, Face.F, Face.R, Face.B], # b/D
]


# TODO: Error in multi twists looks to be in face based RubikCubde model
class RubikCube:
    '''Represents orientation of Rubik cube.'''

    def __init__(self, faces) -> None:
        ''''''
        self.faces = np.array(sorted(faces, key=lambda f: f[1][1]), dtype=Colour)

    def rotate_face(self, face:Face, rotation:int):
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

        #
        for n, adj_face in enumerate(col_2_adj[face]):
            _, face_vec = store[(n-rotation)%4].copy()
            side, _ = store[n]
            if side == 0: # left
                self.faces[adj_face][:,0] = face_vec
            elif side == 1: # top
                self.faces[adj_face][0] = face_vec
            elif side == 2: # right
                self.faces[adj_face][:,2] = face_vec
            elif side == 3: # bottom
                self.faces[adj_face][2] = face_vec

        # rotate face
        self.faces[face] = np.rot90(self.faces[face], k=-rotation)

        return self

    def twist(self, twist: Twist):
        ''''''

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

    def _set_orientations(self):
        '''
        Computes the orientation
        '''
        pass

    def _get_edge_orientation(self, ):
        pass

    def get_col(self, face, x, y) -> str:
        ''''''

        return self.faces[face][x,y]

    def print(self):
        ''''''
        # TODO: Make print in cube layout
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
    orientation: int # TODO: Might want to restrict this to {0,1} or add check
    face_0: Colour
    face_1: Colour

@dataclass
class Corner:
    orientation: int # TODO: Might want to restrict this to {0,1,2} or add check
    face_0: Colour
    face_1: Colour
    face_2: Colour
    index: CornerIdx

    def get_colour(self, idx:int):
        match idx:
            case 0:
                return self.face_0
            case 1:
                return self.face_1
            case 2:
                return self.face_2
            case _:
                # TODO: Error
                return


face_2_edges = (
    (EdgeIdx.UB, EdgeIdx.UR, EdgeIdx.UF, EdgeIdx.UL),   #U
    (EdgeIdx.LU, EdgeIdx.LF, EdgeIdx.LD, EdgeIdx.LB),   #L
    (EdgeIdx.FU, EdgeIdx.FR, EdgeIdx.FD, EdgeIdx.FL),   #F
    (EdgeIdx.RU, EdgeIdx.RB, EdgeIdx.RD, EdgeIdx.RF),   #R
    (EdgeIdx.BU, EdgeIdx.BL, EdgeIdx.BD, EdgeIdx.BR),   #B
    (EdgeIdx.DF, EdgeIdx.DR, EdgeIdx.DB, EdgeIdx.DL)    #D
)

face_2_corners = (
    (CornerIdx.UFL, CornerIdx.UBL, CornerIdx.UBR, CornerIdx.UFR),   #U
    (CornerIdx.LFU, CornerIdx.LFD, CornerIdx.LBD, CornerIdx.LBU),   #L
    (CornerIdx.FUL, CornerIdx.FUR, CornerIdx.FDR, CornerIdx.FDL),   #F
    (CornerIdx.RFU, CornerIdx.RBU, CornerIdx.RBD, CornerIdx.RFD),   #R
    (CornerIdx.BDL, CornerIdx.BDR, CornerIdx.BUR, CornerIdx.BUL),   #B
    (CornerIdx.DFL, CornerIdx.DFR, CornerIdx.DBR, CornerIdx.DBL)    #D
)

def edge_orientation(c1:Colour, c2:Colour) -> int:
    if c1 is Colour.RED or c1 is Colour.ORANGE:
        return 1

    if c1 is Colour.WHITE or c1 is Colour.YELLOW:
        if c2 is Colour.BLUE or c2 is Colour.GREEN:
            return 1

    return 0

def corner_orientation(cornerIdx:CornerIdx, c1:Colour, c3:Colour, c2:Colour) -> int:
    ''''''

    if ((c1 == Colour.GREEN) or (c1 == Colour.BLUE)):
        return 0

    if cornerIdx in (CornerIdx.ULB, CornerIdx.URF, CornerIdx.DLF, CornerIdx.DRB):
        if ((c2 == Colour.GREEN) or (c2 == Colour.BLUE)):
            return 1
        else:
            return 2
    elif cornerIdx in (CornerIdx.URB, CornerIdx.ULF, CornerIdx.DLB, CornerIdx.DRF):
        if ((c3 == Colour.GREEN) or (c3 == Colour.BLUE)):
            return 1
        else:
            return 2
    else:
        # Error
        pass

class RubikCubeIndex:
    def __init__(self, **kwargs) -> None:
        self.edges = []
        self.corners = []
        self.centers = []

        if 'faces' not in kwargs:
            return

        faces = kwargs['faces']

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
            cornerIdx = CornerIdx[f1[0].name + f2[0].name + f3[0].name]
            c1 = faces[f1[0]][f1[1]][f1[2]]
            c2 = faces[f2[0]][f2[1]][f2[2]]
            c3 = faces[f3[0]][f3[1]][f3[2]]

            ori = corner_orientation(cornerIdx, c1, c2, c3)
            if ori == 0:
                self.corners.append(Corner(ori, c1, c2, c3, cornerIdx))
            elif ori == 1:
                self.corners.append(Corner(ori, c2, c3, c1, cornerIdx))
            else:
                self.corners.append(Corner(ori, c3, c1, c2, cornerIdx))

    def rotate_face(self, face: Face, rot: int):
        # Rotate Edges
        # TODO: This is unpleasant to look at, should be able to cleanup.
        idxs = face_2_edges[face]
        self.edges[idxs[(rot)%4]], self.edges[idxs[(rot+1)%4]], self.edges[idxs[(rot+2)%4]], self.edges[idxs[(rot+3)%4]] = self.edges[idxs[0]], self.edges[idxs[1]], self.edges[idxs[2]], self.edges[idxs[3]]

        # Edge Orientations
        # TODO: Need to test that this actually does the same thing as above function
        if (face is Face.F or face is Face.B) and (rot % 2) != 0:
            for idx in idxs:
                # NOTE: Could do XOR
                self.edges[idx].orientation = (self.edges[idx].orientation + 1) % 2

        # Rotate Corners
        # TODO: This is unpleasant to look at, should be able to cleanup.
        idxs = face_2_corners[face]
        self.corners[idxs[(rot)%4]], self.corners[idxs[(rot+1)%4]], self.corners[idxs[(rot+2)%4]], self.corners[idxs[(rot+3)%4]] = self.corners[idxs[0]], self.corners[idxs[1]], self.corners[idxs[2]], self.corners[idxs[3]]

        # Corner Orientations
        # TODO: Should improve this, make new function or something.
        # TODO: Need to test that this actually does the same thing as above function
        if face is Face.L and (rot % 2) != 0:
            # DLB 1, DLF 2, ULF 1, ULB 2
            self.corners[CornerIdx.DLB].orientation = (self.corners[CornerIdx.DLB].orientation + 1) % 3
            self.corners[CornerIdx.DLF].orientation = (self.corners[CornerIdx.DLF].orientation + 2) % 3
            self.corners[CornerIdx.ULF].orientation = (self.corners[CornerIdx.ULF].orientation + 1) % 3
            self.corners[CornerIdx.ULB].orientation = (self.corners[CornerIdx.ULB].orientation + 2) % 3
        elif face is Face.F and (rot % 2) != 0:
            # ULF 2, URF 1, DRF 2, DLF 1
            self.corners[CornerIdx.ULF].orientation = (self.corners[CornerIdx.ULF].orientation + 2) % 3
            self.corners[CornerIdx.URF].orientation = (self.corners[CornerIdx.URF].orientation + 1) % 3
            self.corners[CornerIdx.DRF].orientation = (self.corners[CornerIdx.DRF].orientation + 2) % 3
            self.corners[CornerIdx.DLF].orientation = (self.corners[CornerIdx.DLF].orientation + 1) % 3
        elif face is Face.R and (rot % 2) != 0:
            # DRB 2, DRF 1, URF 2, URB 1
            self.corners[CornerIdx.DRB].orientation = (self.corners[CornerIdx.DRB].orientation + 2) % 3
            self.corners[CornerIdx.DRF].orientation = (self.corners[CornerIdx.DRF].orientation + 1) % 3
            self.corners[CornerIdx.URF].orientation = (self.corners[CornerIdx.URF].orientation + 2) % 3
            self.corners[CornerIdx.URB].orientation = (self.corners[CornerIdx.URB].orientation + 1) % 3
        elif face is Face.B and (rot % 2) != 0:
            #ULB 1, URB 2, DRB 1, DLB 2
            self.corners[CornerIdx.ULB].orientation = (self.corners[CornerIdx.ULB].orientation + 1) % 3
            self.corners[CornerIdx.URB].orientation = (self.corners[CornerIdx.URB].orientation + 2) % 3
            self.corners[CornerIdx.DRB].orientation = (self.corners[CornerIdx.DRB].orientation + 1) % 3
            self.corners[CornerIdx.DLB].orientation = (self.corners[CornerIdx.DLB].orientation + 2) % 3

        return self

    def twist(self, twist: Twist):
        ''''''

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

    def check_edge_orientation(self) -> bool:
        '''Checks if all the edges are orientated correctly or not.'''

        for edge in self.edges:
            if edge.orientation == 1:
                return False

        return True

    def get_edge_colour(self, edgeIdx:EdgeIdx, face:Face) -> Colour:
        ''''''

        (face_1_name,_,_), (face_2_name,_,_) = edge_idxs[edgeIdx]

        if face == face_1_name:
            face_idx = 0
        elif face == face_2_name:
            face_idx = 1
        else:
            # TODO: Error handling
            pass

        idx = (self.edges[edgeIdx].orientation + face_idx) % 2
        if idx == 0:
            return self.edges[edgeIdx].face_0
        else:
            return self.edges[edgeIdx].face_1

    def get_corner_colour(self, cornerIdx:CornerIdx, face:Face) -> Colour:
        ''''''

        # Get the new permutation of the corner facelets
        match self.corners[cornerIdx].orientation:
            case 0:
                i0,i1,i2 = 0,1,2
            case 1:
                i0,i1,i2 = 2,0,1
            case 2:
                i0,i1,i2 = 1,2,0
            case ori:
                # Error
                pass

        # Based of current facelet orientation and start orientation get desired facelet
        og_index = self.corners[cornerIdx].index
        (f0,f1,f2) = corner_order[cornerIdx]
        if face == f0: # U/D
            return Colour(corner_order[og_index][i0])
        elif face == f1: # F/B
            return Colour(corner_order[og_index][i1])
        elif face == f2: # L/R
            return Colour(corner_order[og_index][i2])
        else:
            # Error
            print('Error')
            pass


    def copy(self):
        cube_copy = RubikCubeIndex()
        # TODO: I think this is a shallow copy so might causes issues...
        cube_copy.edges = [dataclasses.replace(item) for item in self.edges]
        cube_copy.corners = [dataclasses.replace(item) for item in self.corners]
        cube_copy.centers = [item for item in self.centers]
        return cube_copy

    def __str__(self) -> str:
        name = ''
        name += (
            f'\t|{self.get_corner_colour(CornerIdx.UBL,Face.U)}|{self.get_edge_colour(EdgeIdx.UB,Face.U)}|{self.get_corner_colour(CornerIdx.UBR,Face.U)}|\n'
            f'\t|{self.get_edge_colour(EdgeIdx.UL,Face.U)}|{self.centers[Face.U]}|{self.get_edge_colour(EdgeIdx.UR,Face.U)}|\n'
            f'\t|{self.get_corner_colour(CornerIdx.UFL,Face.U)}|{self.get_edge_colour(EdgeIdx.UF,Face.U)}|{self.get_corner_colour(CornerIdx.UFR,Face.U)}|\n'
        )
        name += '\t-------\n'
        name += (
            f'|{self.get_corner_colour(CornerIdx.UBL,Face.L)}|{self.get_edge_colour(EdgeIdx.UL,Face.L)}|{self.get_corner_colour(CornerIdx.UFL,Face.L)}|'
            f'\t|{self.get_corner_colour(CornerIdx.UFL,Face.F)}|{self.get_edge_colour(EdgeIdx.UF,Face.F)}|{self.get_corner_colour(CornerIdx.UFR,Face.F)}|'
            f'\t|{self.get_corner_colour(CornerIdx.UFR,Face.R)}|{self.get_edge_colour(EdgeIdx.UR,Face.R)}|{self.get_corner_colour(CornerIdx.UBR,Face.R)}|'
            f'\t|{self.get_corner_colour(CornerIdx.UBR,Face.B)}|{self.get_edge_colour(EdgeIdx.UB,Face.B)}|{self.get_corner_colour(CornerIdx.UBL,Face.B)}|\n'

            f'|{self.get_edge_colour(EdgeIdx.LB,Face.L)}|{self.centers[Face.L]}|{self.get_edge_colour(EdgeIdx.LF,Face.L)}|'
            f'\t|{self.get_edge_colour(EdgeIdx.FL,Face.F)}|{self.centers[Face.F]}|{self.get_edge_colour(EdgeIdx.FR,Face.F)}|'
            f'\t|{self.get_edge_colour(EdgeIdx.RF,Face.R)}|{self.centers[Face.R]}|{self.get_edge_colour(EdgeIdx.RB,Face.R)}|'
            f'\t|{self.get_edge_colour(EdgeIdx.BR,Face.B)}|{self.centers[Face.B]}|{self.get_edge_colour(EdgeIdx.BL,Face.B)}|\n'

            f'|{self.get_corner_colour(CornerIdx.DBL,Face.L)}|{self.get_edge_colour(EdgeIdx.LD,Face.L)}|{self.get_corner_colour(CornerIdx.FDL,Face.L)}|'
            f'\t|{self.get_corner_colour(CornerIdx.FDL,Face.F)}|{self.get_edge_colour(EdgeIdx.FD,Face.F)}|{self.get_corner_colour(CornerIdx.FDR,Face.F)}|'
            f'\t|{self.get_corner_colour(CornerIdx.FDR,Face.R)}|{self.get_edge_colour(EdgeIdx.RD,Face.R)}|{self.get_corner_colour(CornerIdx.BDR,Face.R)}|'
            f'\t|{self.get_corner_colour(CornerIdx.BDR,Face.B)}|{self.get_edge_colour(EdgeIdx.BD,Face.B)}|{self.get_corner_colour(CornerIdx.BDL,Face.B)}|\n'
        )
        name += '\t-------\n'
        name += (
            f'\t|{self.get_corner_colour(CornerIdx.FDL,Face.D)}|{self.get_edge_colour(EdgeIdx.DF,Face.D)}|{self.get_corner_colour(CornerIdx.FDR,Face.D)}|\n'
            f'\t|{self.get_edge_colour(EdgeIdx.DL,Face.D)}|{self.centers[Face.D]}|{self.get_edge_colour(EdgeIdx.DR,Face.D)}|\n'
            f'\t|{self.get_corner_colour(CornerIdx.BDL,Face.D)}|{self.get_edge_colour(EdgeIdx.DB,Face.D)}|{self.get_corner_colour(CornerIdx.BDR,Face.D)}|\n'
        )

        return name


