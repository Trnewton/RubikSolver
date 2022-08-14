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

    pruner = search.Pruner(cube)
    sol = search.dfs(cube, thistlethwaite.g1_solved, thistlethwaite.Twists_G0, pruner, max_depth=7)
    print(sol.cube)
    print(sol.moves)




if __name__ == '__main__':
    check_g0_g1()