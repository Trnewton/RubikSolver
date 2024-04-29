import pickle
import array
from abc import ABC, abstractmethod

import cubeModel


class PatternDatabase(ABC):
    def __init__(self, size: int) -> None:
        self.num_moves = array.array('B', [0xff for n in range(size)])
        self.to_fill = size

    def is_full(self):
        ''''''
        return self.to_fill == 0

    @abstractmethod
    def _index(self, cube: cubeModel.RubikCube) -> int:
        ''''''
        pass

    def add_pattern(self, cube:cubeModel.RubikCube, num_moves: int) -> None:
        ''''''
        idx = self._index(cube)
        if self.num_moves[idx] > num_moves:
            self.num_moves[idx] = num_moves

    def get_steps(self, cube:cubeModel.RubikCube) -> int:
        ''''''
        return self.num_moves[self._index(cube)]

class G0Database(PatternDatabase):
    def __init__(self) -> None:
        super().__init__(2048)

    def _index(self, cube: cubeModel.RubikCubeIndex) -> int:
        val = 0
        base = 1
        for idx in cubeModel.EdgeIdx:
            val += cube.edges[idx].orientation * base
            base *= 2

        return val


class G1Database(PatternDatabase):
    def __init__(self) -> None:
        super.__init__(self, 1082565)

    def _index(self, cube: cubeModel.RubikCube) -> int:
        return super()._index(cube)

class G2Database(PatternDatabase):
    def __init__(self) -> None:
        super.__init__(self, 352800)

    def _index(self, cube: cubeModel.RubikCube) -> int:
        return super()._index(cube)

class G3Database(PatternDatabase):
    def __init__(self) -> None:
        super.__init__(self, 663552)

    def _index(self, cube: cubeModel.RubikCube) -> int:
        return super()._index(cube)