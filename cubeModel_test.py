from typing import Iterable
import unittest

from rubik import cubeModel

solved_cube = cubeModel.RubikCube(faces=[
    [[c,c,c],
    [c,c,c],
    [c,c,c]] for c in cubeModel.Colour
])

solved_cube_index = cubeModel.RubikCubeIndex(faces=[
    [[c,c,c],
    [c,c,c],
    [c,c,c]] for c in cubeModel.Colour
])

class TestCubeModel(unittest.TestCase):
    ''''''

    def test_orientation_single(self):
        for twist in cubeModel.Twist:
            cube = solved_cube.copy().twist(twist)
            cubeIndex = solved_cube_index.copy().twist(twist)

            # Test edge orientations for twist
            for f1, f2 in cubeModel.edge_idxs:
                c1 = cube.faces[f1[0]][f1[1]][f1[2]]
                c2 = cube.faces[f2[0]][f2[1]][f2[2]]
                edgeIdx = cubeModel.EdgeIdx[f1[0].name + f2[0].name]

                with self.subTest():
                    self.assertEqual(
                        cubeModel.edge_orientation(c1, c2),
                        cubeIndex.edges[edgeIdx].orientation,
                        (
                            f'Orientation failed  on twist {twist.name} at edge {edgeIdx.name}\n'
                            f'{str(cube)}\n{str(cubeIndex)}'

                        )
                    )
            # Test corner orientations for twist
            for f1, f2, f3 in cubeModel.corner_idxs:
                cornerIdx = cubeModel.CornerIdx[f1[0].name + f2[0].name + f3[0].name]
                c1 = cube.faces[f1[0]][f1[1]][f1[2]]
                c2 = cube.faces[f2[0]][f2[1]][f2[2]]
                c3 = cube.faces[f3[0]][f3[1]][f3[2]]
                with self.subTest():
                    self.assertEqual(
                        cubeIndex.corners[cornerIdx].orientation,
                        cubeModel.corner_orientation(cornerIdx, c1, c2, c3),
                        (
                            f'Orientation failed on twist {twist.name} at corner {cornerIdx.name}:\n'
                            f'{str(cubeIndex)}'
                        )
                    )

    def test_orientation_double(self):
        for twist_1 in cubeModel.Twist:
            cube_base = solved_cube.copy().twist(twist_1)
            cubeIndex_base = solved_cube_index.copy().twist(twist_1)
            for twist_2 in cubeModel.Twist:
                cube = cube_base.copy().twist(twist_2)
                cubeIndex = cubeIndex_base.copy().twist(twist_2)

                # Test edge orientations for twist
                for f1, f2 in cubeModel.edge_idxs:
                    c1 = cube.faces[f1[0]][f1[1]][f1[2]]
                    c2 = cube.faces[f2[0]][f2[1]][f2[2]]
                    edgeIdx = cubeModel.EdgeIdx[f1[0].name + f2[0].name]

                    with self.subTest():
                        self.assertEqual(
                            cubeModel.edge_orientation(c1, c2),
                            cubeIndex.edges[edgeIdx].orientation,
                            (
                                f'Orientation failed  on twist {twist_1.name},{twist_2.name} at edge {edgeIdx.name}\n'
                                f'{str(cube)}\n{str(cubeIndex)}'

                            )
                        )
                # Test corner orientations for twist
                for f1, f2, f3 in cubeModel.corner_idxs:
                    cornerIdx = cubeModel.CornerIdx[f1[0].name + f2[0].name + f3[0].name]
                    c1 = cube.faces[f1[0]][f1[1]][f1[2]]
                    c2 = cube.faces[f2[0]][f2[1]][f2[2]]
                    c3 = cube.faces[f3[0]][f3[1]][f3[2]]
                    with self.subTest():
                        self.assertEqual(
                            cubeIndex.corners[cornerIdx].orientation,
                            cubeModel.corner_orientation(cornerIdx, c1, c2, c3),
                            (
                                f'Orientation failed on twist {twist_1.name},{twist_2.name} at corner {cornerIdx.name}:\n'
                                f'{str(cubeIndex)}'
                            )
                        )


    def test_singleTurns(self):
        for twist in cubeModel.Twist:
            cube_out = str(solved_cube.copy().twist(twist))
            cubeIndex_out = str(solved_cube_index.copy().twist(twist))
            with self.subTest():
                self.assertEqual(cube_out, cubeIndex_out, f'\nDid not agree on {twist.name}:\n{cube_out}\n{cubeIndex_out}')

    def test_multiTwist(self):
        twists = (
            cubeModel.Twist.L,
            cubeModel.Twist.B,
            cubeModel.Twist.D,
            cubeModel.Twist.R,
            cubeModel.Twist.F,
            cubeModel.Twist.U,
        )

        cube = solved_cube.copy()
        cubeIndex = solved_cube_index.copy()

        for twist in twists:
            cube.twist(twist)
            cubeIndex.twist(twist)

        cube_out = str(cube)
        cubeIndex_out = str(cubeIndex)

        self.assertEqual(cube_out, cubeIndex_out, f'\nDid not agree on:\n {cube_out}\n{cubeIndex_out}')


if __name__ == '__main__':
    unittest.main()