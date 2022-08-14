from dataclasses import dataclass

import cubeModel


#### Constants ####
Twists_G3 = [
    cubeModel.Twist.L2, cubeModel.Twist.R2, cubeModel.Twist.F2,
    cubeModel.Twist.B2, cubeModel.Twist.U2, cubeModel.Twist.D2,
]
Twists_G2 = Twists_G3 + [
    cubeModel.Twist.L, cubeModel.Twist.LP, cubeModel.Twist.R, cubeModel.Twist.RP,
]
Twists_G1 = Twists_G2 + [
    cubeModel.Twist.F, cubeModel.Twist.FP, cubeModel.Twist.B, cubeModel.Twist.BP,
]
Twists_G0 = Twists_G1 + [
    cubeModel.Twist.U, cubeModel.Twist.UP, cubeModel.Twist.D, cubeModel.Twist.DP,
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
    BL = cube.faces[cubeModel.Face.B, 1, 0]
    BR = cube.faces[cubeModel.Face.B, 1, 2]
    BD = cube.faces[cubeModel.Face.B, 2, 1]

    DF = cube.faces[cubeModel.Face.D, 0, 1]
    DL = cube.faces[cubeModel.Face.D, 1, 0]
    DR = cube.faces[cubeModel.Face.D, 1, 2]
    DB = cube.faces[cubeModel.Face.D, 2, 1]

    return (
      (UF is cubeModel.Colour.BLUE or UF is cubeModel.Colour.GREEN or FU is cubeModel.Colour.WHITE or FU is cubeModel.Colour.YELLOW) and
      (UB is cubeModel.Colour.BLUE or UB is cubeModel.Colour.GREEN or BU is cubeModel.Colour.WHITE or BU is cubeModel.Colour.YELLOW) and
      (DF is cubeModel.Colour.BLUE or DF is cubeModel.Colour.GREEN or FD is cubeModel.Colour.WHITE or FD is cubeModel.Colour.YELLOW) and
      (DB is cubeModel.Colour.BLUE or DB is cubeModel.Colour.GREEN or BD is cubeModel.Colour.WHITE or BD is cubeModel.Colour.YELLOW) and
      (LU is cubeModel.Colour.BLUE or LU is cubeModel.Colour.GREEN or UL is cubeModel.Colour.WHITE or UL is cubeModel.Colour.YELLOW) and
      (LD is cubeModel.Colour.BLUE or LD is cubeModel.Colour.GREEN or DL is cubeModel.Colour.WHITE or DL is cubeModel.Colour.YELLOW) and
      (RU is cubeModel.Colour.BLUE or RU is cubeModel.Colour.GREEN or UR is cubeModel.Colour.WHITE or UR is cubeModel.Colour.YELLOW) and
      (RD is cubeModel.Colour.BLUE or RD is cubeModel.Colour.GREEN or DR is cubeModel.Colour.WHITE or DR is cubeModel.Colour.YELLOW) and
      (LF is cubeModel.Colour.BLUE or LF is cubeModel.Colour.GREEN or FL is cubeModel.Colour.WHITE or FL is cubeModel.Colour.YELLOW) and
      (LB is cubeModel.Colour.BLUE or LB is cubeModel.Colour.GREEN or BL is cubeModel.Colour.WHITE or BL is cubeModel.Colour.YELLOW) and
      (RF is cubeModel.Colour.BLUE or RF is cubeModel.Colour.GREEN or FR is cubeModel.Colour.WHITE or FR is cubeModel.Colour.YELLOW) and
      (RB is cubeModel.Colour.BLUE or RB is cubeModel.Colour.GREEN or BR is cubeModel.Colour.WHITE or BR is cubeModel.Colour.YELLOW))

def g2_solved(cube:cubeModel.RubikCube) -> bool:
    LUB = cube.face(cubeModel.Face.L, 0, 0)
    LUF = cube.face(cubeModel.Face.L, 0, 2)
    LDB = cube.face(cubeModel.Face.L, 2, 0)
    LDF = cube.face(cubeModel.Face.L, 2, 2)

    RUB = cube.face(cubeModel.Face.R, 0, 2)
    RUF = cube.face(cubeModel.Face.R, 0, 0)
    RDB = cube.face(cubeModel.Face.R, 2, 2)
    RDF = cube.face(cubeModel.Face.R, 2, 0)

    # Edges in the M slice (between R and L).
    UF = cube.face(cubeModel.Face.U, 2, 1)
    FU = cube.face(cubeModel.Face.F, 0, 1)

    UB = cube.face(cubeModel.Face.U, 0, 1)
    BU = cube.face(cubeModel.Face.B, 0, 1)

    DF = cube.face(cubeModel.Face.D, 0, 1)
    FD = cube.face(cubeModel.Face.F, 2, 1)

    DB = cube.face(cubeModel.Face.D, 2, 1)
    BD = cube.face(cubeModel.Face.B, 2, 1)

    # All left/right corner facets either blue or green.
    # UF, UB, DF, DB in the M slice.  Note that the edges
    # are already oriented.
    return (
      (LUB is cubeModel.Colour.BLUE or LUB is cubeModel.Colour.GREEN) and
      (LUF is cubeModel.Colour.BLUE or LUF is cubeModel.Colour.GREEN) and
      (LDB is cubeModel.Colour.BLUE or LDB is cubeModel.Colour.GREEN) and
      (LDF is cubeModel.Colour.BLUE or LDF is cubeModel.Colour.GREEN) and
      (RUB is cubeModel.Colour.BLUE or RUB is cubeModel.Colour.GREEN) and
      (RUF is cubeModel.Colour.BLUE or RUF is cubeModel.Colour.GREEN) and
      (RDB is cubeModel.Colour.BLUE or RDB is cubeModel.Colour.GREEN) and
      (RDF is cubeModel.Colour.BLUE or RDF is cubeModel.Colour.GREEN) and

      (UF is cubeModel.Colour.RED   or UF is cubeModel.Colour.ORANGE) and
      (FU is cubeModel.Colour.WHITE or FU is cubeModel.Colour.YELLOW) and

      (UB is cubeModel.Colour.RED   or UB is cubeModel.Colour.ORANGE) and
      (BU is cubeModel.Colour.WHITE or BU is cubeModel.Colour.YELLOW) and

      (DF is cubeModel.Colour.RED   or DF is cubeModel.Colour.ORANGE) and
      (FD is cubeModel.Colour.WHITE or FD is cubeModel.Colour.YELLOW) and

      (DB is cubeModel.Colour.RED   or DB is cubeModel.Colour.ORANGE) and
      (BD is cubeModel.Colour.WHITE or BD is cubeModel.Colour.YELLOW)
      )

def g3_solved(cube:cubeModel.RubikCube) -> bool:
    pass


def thistlethwaite(cube) -> str:
    pass


if __name__ == '__main__':
    pass