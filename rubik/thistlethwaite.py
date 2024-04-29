from dataclasses import dataclass

from rubik import cubeModel
from rubik.cubeModel import Colour

#### Constants ####
Twists_G3 = [
    cubeModel.Twist.L2, cubeModel.Twist.R2, cubeModel.Twist.F2,
    cubeModel.Twist.B2, cubeModel.Twist.U2, cubeModel.Twist.D2,
]
Twists_G2 = Twists_G3 + [
    cubeModel.Twist.L, cubeModel.Twist.LP, cubeModel.Twist.R, cubeModel.Twist.RP,
]
Twists_G1 = Twists_G2 + [
    cubeModel.Twist.U, cubeModel.Twist.UP, cubeModel.Twist.D, cubeModel.Twist.DP,
]
Twists_G0 = Twists_G1 + [
    cubeModel.Twist.F, cubeModel.Twist.FP, cubeModel.Twist.B, cubeModel.Twist.BP,
]

#### Classes ####


#### Functions ####

def g1_solved(cube:cubeModel.RubikCubeIndex) -> bool:
    return cube.check_edge_orientation()

def g2_solved(cube:cubeModel.RubikCube) -> bool:
    LUB = cube.faces[cubeModel.Face.L, 0, 0]
    LUF = cube.faces[cubeModel.Face.L, 0, 2]
    LDB = cube.faces[cubeModel.Face.L, 2, 0]
    LDF = cube.faces[cubeModel.Face.L, 2, 2]

    RUB = cube.faces[cubeModel.Face.R, 0, 2]
    RUF = cube.faces[cubeModel.Face.R, 0, 0]
    RDB = cube.faces[cubeModel.Face.R, 2, 2]
    RDF = cube.faces[cubeModel.Face.R, 2, 0]

    # Edges in the M slice (between R and L).
    UF = cube.faces[cubeModel.Face.U, 2, 1]
    FU = cube.faces[cubeModel.Face.F, 0, 1]

    UB = cube.faces[cubeModel.Face.U, 0, 1]
    BU = cube.faces[cubeModel.Face.B, 0, 1]

    DF = cube.faces[cubeModel.Face.D, 0, 1]
    FD = cube.faces[cubeModel.Face.F, 2, 1]

    DB = cube.faces[cubeModel.Face.D, 2, 1]
    BD = cube.faces[cubeModel.Face.B, 2, 1]

    # All left/right corner facets either blue or green.
    # UF, UB, DF, DB in the M slice.  Note that the edges
    # are already oriented.
    return (
      (LUB is Colour.ORANGE or LUB is Colour.RED) and
      (LUF is Colour.ORANGE or LUF is Colour.RED) and
      (LDB is Colour.ORANGE or LDB is Colour.RED) and
      (LDF is Colour.ORANGE or LDF is Colour.RED) and
      (RUB is Colour.ORANGE or RUB is Colour.RED) and
      (RUF is Colour.ORANGE or RUF is Colour.RED) and
      (RDB is Colour.ORANGE or RDB is Colour.RED) and
      (RDF is Colour.ORANGE or RDF is Colour.RED) and

      (UF is Colour.WHITE or UF is Colour.YELLOW) and
      (FU is Colour.GREEN or FU is Colour.BLUE) and

      (UB is Colour.WHITE or UB is Colour.YELLOW) and
      (BU is Colour.GREEN or BU is Colour.BLUE) and

      (DF is Colour.WHITE or DF is Colour.YELLOW) and
      (FD is Colour.GREEN or FD is Colour.BLUE) and

      (DB is Colour.WHITE or DB is Colour.YELLOW) and
      (BD is Colour.GREEN or BD is Colour.BLUE)
      )

def g3_solved(cube:cubeModel.RubikCube) -> bool:
    pass


def thistlethwaite(cube) -> str:
    pass


if __name__ == '__main__':
    pass