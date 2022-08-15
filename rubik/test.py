from distutils.util import change_root
import random
from typing import Iterable

import cubeModel
import search
import thistlethwaite


def randomize_cube(cube: cubeModel.RubikCube, num_twists: int, twists: Iterable=None) -> None:
    if twists is None:
        twists = list(cubeModel.Twist)

    for n in range(num_twists):
        twist = random.choice(twists)
        cube.twist(twist)


solved_cube = [
    [[c,c,c],
    [c,c,c],
    [c,c,c]] for c in cubeModel.Colour
]

def check_rotation():
    twists = [
        cubeModel.Twist.L2,
        cubeModel.Twist.R2,
        cubeModel.Twist.F2,
        cubeModel.Twist.B2,
        cubeModel.Twist.U2,
        cubeModel.Twist.D2,
    ]
    for twist in twists:
        print(twist)
        cube = cubeModel.RubikCube(solved_cube)
        cube.twist(twist)
        print(cube)


def check_g0_g1():
    cube = cubeModel.RubikCube(solved_cube)
    randomize_cube(cube, 1, twists=thistlethwaite.Twists_G1)
    print(cube)

    # pruner = search.Pruner(cube)
    # sol = search.dfs(cube, thistlethwaite.g1_solved, thistlethwaite.Twists_G0, pruner, max_depth=7)
    # print(sol.cube)
    # print(sol.moves)




if __name__ == '__main__':
    cube = cubeModel.RubikCube(solved_cube)
    print('G1:', thistlethwaite.g1_solved(cube))

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

    print(UF is cubeModel.Colour.BLUE or UF is cubeModel.Colour.GREEN or
        FU is cubeModel.Colour.WHITE or FU is cubeModel.Colour.YELLOW)
    print(UB is cubeModel.Colour.BLUE or UB is cubeModel.Colour.GREEN or
        BU is cubeModel.Colour.WHITE or BU is cubeModel.Colour.YELLOW)
    print(DF is cubeModel.Colour.BLUE or DF is cubeModel.Colour.GREEN or
        FD is cubeModel.Colour.WHITE or FD is cubeModel.Colour.YELLOW)
    print(DB is cubeModel.Colour.BLUE or DB is cubeModel.Colour.GREEN or
        BD is cubeModel.Colour.WHITE or BD is cubeModel.Colour.YELLOW)
    print(LU is cubeModel.Colour.BLUE or LU is cubeModel.Colour.GREEN or
        UL is cubeModel.Colour.WHITE or UL is cubeModel.Colour.YELLOW)
    print(LD is cubeModel.Colour.BLUE or LD is cubeModel.Colour.GREEN or
        DL is cubeModel.Colour.WHITE or DL is cubeModel.Colour.YELLOW)
    print(RU is cubeModel.Colour.BLUE or RU is cubeModel.Colour.GREEN or
        UR is cubeModel.Colour.WHITE or UR is cubeModel.Colour.YELLOW)
    print(RD is cubeModel.Colour.BLUE or RD is cubeModel.Colour.GREEN or
        DR is cubeModel.Colour.WHITE or DR is cubeModel.Colour.YELLOW)
    print(LF is cubeModel.Colour.BLUE or LF is cubeModel.Colour.GREEN or
        FL is cubeModel.Colour.WHITE or FL is cubeModel.Colour.YELLOW)
    print(LB is cubeModel.Colour.BLUE or LB is cubeModel.Colour.GREEN or
        BL is cubeModel.Colour.WHITE or BL is cubeModel.Colour.YELLOW)
    print(RF is cubeModel.Colour.BLUE or RF is cubeModel.Colour.GREEN or
        FR is cubeModel.Colour.WHITE or FR is cubeModel.Colour.YELLOW)
    print(RB is cubeModel.Colour.BLUE or RB is cubeModel.Colour.GREEN or
        BR is cubeModel.Colour.WHITE or BR is cubeModel.Colour.YELLOW)

    cube.faces[cubeModel.Face.U, 0, 1] = 'UB'
    cube.faces[cubeModel.Face.U, 1, 0] = 'UL'
    cube.faces[cubeModel.Face.U, 1, 2] = 'UR'
    cube.faces[cubeModel.Face.U, 2, 1] = 'UF'

    cube.faces[cubeModel.Face.L, 0, 1] = 'LU'
    cube.faces[cubeModel.Face.L, 1, 0] = 'LB'
    cube.faces[cubeModel.Face.L, 1, 2] = 'LF'
    cube.faces[cubeModel.Face.L, 2, 1] = 'LD'

    cube.faces[cubeModel.Face.F, 0, 1] = 'FU'
    cube.faces[cubeModel.Face.F, 1, 0] = 'FL'
    cube.faces[cubeModel.Face.F, 1, 2] = 'FR'
    cube.faces[cubeModel.Face.F, 2, 1] = 'FD'

    cube.faces[cubeModel.Face.R, 0, 1] = 'RU'
    cube.faces[cubeModel.Face.R, 1, 0] = 'RF'
    cube.faces[cubeModel.Face.R, 1, 2] = 'RB'
    cube.faces[cubeModel.Face.R, 2, 1] = 'RD'

    cube.faces[cubeModel.Face.B, 0, 1] = 'BU'
    cube.faces[cubeModel.Face.B, 1, 2] = 'BL'
    cube.faces[cubeModel.Face.B, 1, 0] = 'BR'
    cube.faces[cubeModel.Face.B, 2, 1] = 'BD'

    cube.faces[cubeModel.Face.D, 0, 1] = 'DF'
    cube.faces[cubeModel.Face.D, 1, 0] = 'DL'
    cube.faces[cubeModel.Face.D, 1, 2] = 'DR'
    cube.faces[cubeModel.Face.D, 2, 1] = 'DB'

    print(cube)
