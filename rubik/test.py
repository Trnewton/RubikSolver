from distutils.util import change_root
import random
from typing import Iterable

import cubeModel
from cubeModel import Colour
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
    print('G2:', thistlethwaite.g2_solved(cube))

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

    print(UF is Colour.ORANGE or UF is Colour.RED or FU is Colour.GREEN or FU is Colour.BLUE)
    print(UB is Colour.ORANGE or UB is Colour.RED or BU is Colour.GREEN or BU is Colour.BLUE)
    print(DF is Colour.ORANGE or DF is Colour.RED or FD is Colour.GREEN or FD is Colour.BLUE)
    print(DB is Colour.ORANGE or DB is Colour.RED or BD is Colour.GREEN or BD is Colour.BLUE)
    print(LU is Colour.ORANGE or LU is Colour.RED or UL is Colour.GREEN or UL is Colour.BLUE)
    print(LD is Colour.ORANGE or LD is Colour.RED or DL is Colour.GREEN or DL is Colour.BLUE)
    print(RU is Colour.ORANGE or RU is Colour.RED or UR is Colour.GREEN or UR is Colour.BLUE)
    print(RD is Colour.ORANGE or RD is Colour.RED or DR is Colour.GREEN or DR is Colour.BLUE)
    print(LF is Colour.ORANGE or LF is Colour.RED or FL is Colour.GREEN or FL is Colour.BLUE)
    print(LB is Colour.ORANGE or LB is Colour.RED or BL is Colour.GREEN or BL is Colour.BLUE)
    print(RF is Colour.ORANGE or RF is Colour.RED or FR is Colour.GREEN or FR is Colour.BLUE)
    print(RB is Colour.ORANGE or RB is Colour.RED or BR is Colour.GREEN or BR is Colour.BLUE)

    # cube.faces[cubeModel.Face.U, 0, 1] = 'UB'
    # cube.faces[cubeModel.Face.U, 1, 0] = 'UL'
    # cube.faces[cubeModel.Face.U, 1, 2] = 'UR'
    # cube.faces[cubeModel.Face.U, 2, 1] = 'UF'

    # cube.faces[cubeModel.Face.L, 0, 1] = 'LU'
    # cube.faces[cubeModel.Face.L, 1, 0] = 'LB'
    # cube.faces[cubeModel.Face.L, 1, 2] = 'LF'
    # cube.faces[cubeModel.Face.L, 2, 1] = 'LD'

    # cube.faces[cubeModel.Face.F, 0, 1] = 'FU'
    # cube.faces[cubeModel.Face.F, 1, 0] = 'FL'
    # cube.faces[cubeModel.Face.F, 1, 2] = 'FR'
    # cube.faces[cubeModel.Face.F, 2, 1] = 'FD'

    # cube.faces[cubeModel.Face.R, 0, 1] = 'RU'
    # cube.faces[cubeModel.Face.R, 1, 0] = 'RF'
    # cube.faces[cubeModel.Face.R, 1, 2] = 'RB'
    # cube.faces[cubeModel.Face.R, 2, 1] = 'RD'

    # cube.faces[cubeModel.Face.B, 0, 1] = 'BU'
    # cube.faces[cubeModel.Face.B, 1, 2] = 'BL'
    # cube.faces[cubeModel.Face.B, 1, 0] = 'BR'
    # cube.faces[cubeModel.Face.B, 2, 1] = 'BD'

    # cube.faces[cubeModel.Face.D, 0, 1] = 'DF'
    # cube.faces[cubeModel.Face.D, 1, 0] = 'DL'
    # cube.faces[cubeModel.Face.D, 1, 2] = 'DR'
    # cube.faces[cubeModel.Face.D, 2, 1] = 'DB'

    print(cube)

print('G1:', thistlethwaite.g1_solved(cube))