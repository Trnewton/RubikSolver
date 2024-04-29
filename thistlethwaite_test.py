import random
from typing import Iterable
import unittest

from rubik import cubeModel
from rubik import thistlethwaite


def randomize_cube(cube: cubeModel.RubikCube, num_twists: int, twists: Iterable=None) -> None:
    if twists is None:
        twists = list(cubeModel.Twist)

    for n in range(num_twists):
        twist = random.choice(twists)
        cube.twist(twist)



solved_cube = cubeModel.RubikCubeIndex(faces=[
    [[c,c,c],
    [c,c,c],
    [c,c,c]] for c in cubeModel.Colour
])

def check_g0_g1():
    cube = solved_cube.copy()
    randomize_cube(cube, 1, twists=thistlethwaite.Twists_G1)
    print(cube)

    # pruner = search.Pruner(cube)
    # sol = search.dfs(cube, thistlethwaite.g1_solved, thistlethwaite.Twists_G0, pruner, max_depth=7)
    # print(sol.cube)
    # print(sol.moves)

class TestGroupChecks(unittest.TestCase):

    def test_g1_solved(self):
        self.assertTrue(thistlethwaite.g1_solved(solved_cube))

    def test_g1_1(self):
        self.assertFalse(thistlethwaite.g1_solved(solved_cube.copy().rotate_face(cubeModel.Face.D, 1)))

if __name__ == '__main__':
    unittest.main()
