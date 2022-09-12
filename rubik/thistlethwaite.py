from dataclasses import dataclass

import cubeModel
from cubeModel import Colour

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

def g1_solved(cube:cubeModel.RubikCube) -> bool:
    UB = cube.faces[cubeModel.Face.U, 0, 1]
    UL = cube.faces[cubeModel.Face.U, 1, 0]
    UR = cube.faces[cubeModel.Face.U, 1, 2]
    UF = cube.faces[cubeModel.Face.U, 2, 1]

    LU = cube.faces[cubeModel.Face.L, 0, 1]
    LB = cube.faces[cubeModel.Face.L, 1, 0]
    LF = cube.faces[cubeModel.Face.L, 1, 2]
    LD = cube.faces[cubeModel.Face.L, 2, 1]

    FU = cube.faces[cubeModel.Face.F, 0, 1]
    FL = cube.faces[cubeModel.Face.F, 1, 0]
    FR = cube.faces[cubeModel.Face.F, 1, 2]
    FD = cube.faces[cubeModel.Face.F, 2, 1]

    RU = cube.faces[cubeModel.Face.R, 0, 1]
    RF = cube.faces[cubeModel.Face.R, 1, 0]
    RB = cube.faces[cubeModel.Face.R, 1, 2]
    RD = cube.faces[cubeModel.Face.R, 2, 1]

    BU = cube.faces[cubeModel.Face.B, 0, 1]
    BL = cube.faces[cubeModel.Face.B, 1, 2]
    BR = cube.faces[cubeModel.Face.B, 1, 0]
    BD = cube.faces[cubeModel.Face.B, 2, 1]

    DF = cube.faces[cubeModel.Face.D, 0, 1]
    DL = cube.faces[cubeModel.Face.D, 1, 0]
    DR = cube.faces[cubeModel.Face.D, 1, 2]
    DB = cube.faces[cubeModel.Face.D, 2, 1]

    return (
      (UF is Colour.ORANGE or UF is Colour.RED or FU is Colour.GREEN or FU is Colour.BLUE) and
      (UB is Colour.ORANGE or UB is Colour.RED or BU is Colour.GREEN or BU is Colour.BLUE) and
      (DF is Colour.ORANGE or DF is Colour.RED or FD is Colour.GREEN or FD is Colour.BLUE) and
      (DB is Colour.ORANGE or DB is Colour.RED or BD is Colour.GREEN or BD is Colour.BLUE) and
      (LU is Colour.ORANGE or LU is Colour.RED or UL is Colour.GREEN or UL is Colour.BLUE) and
      (LD is Colour.ORANGE or LD is Colour.RED or DL is Colour.GREEN or DL is Colour.BLUE) and
      (RU is Colour.ORANGE or RU is Colour.RED or UR is Colour.GREEN or UR is Colour.BLUE) and
      (RD is Colour.ORANGE or RD is Colour.RED or DR is Colour.GREEN or DR is Colour.BLUE) and
      (LF is Colour.ORANGE or LF is Colour.RED or FL is Colour.GREEN or FL is Colour.BLUE) and
      (LB is Colour.ORANGE or LB is Colour.RED or BL is Colour.GREEN or BL is Colour.BLUE) and
      (RF is Colour.ORANGE or RF is Colour.RED or FR is Colour.GREEN or FR is Colour.BLUE) and
      (RB is Colour.ORANGE or RB is Colour.RED or BR is Colour.GREEN or BR is Colour.BLUE))

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