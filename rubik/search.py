from collections import deque
from typing import Callable

import cubeModel

class Pruner:
    def __init__(self, init_cube):
        self.seen = {init_cube}

    def prune(self, new_move, node):
        last_move = node[1][-1]

        if (last_move in {cubeModel.Twist.L, cubeModel.Twist.LP, cubeModel.Twist.L2} and
            (new_move in {cubeModel.Twist.L, cubeModel.Twist.LP, cubeModel.Twist.L2} or
            new_move in {cubeModel.Twist.R, cubeModel.Twist.RP, cubeModel.Twist.R2})):
            return True
        if (last_move in {cubeModel.Twist.R, cubeModel.Twist.RP, cubeModel.Twist.R2} and
            new_move in {cubeModel.Twist.R, cubeModel.Twist.RP, cubeModel.Twist.R2}):
            return True
        if (last_move in {cubeModel.Twist.F, cubeModel.Twist.FP, cubeModel.Twist.F2} and
            (new_move in {cubeModel.Twist.F, cubeModel.Twist.FP, cubeModel.Twist.F2} or
            new_move in {cubeModel.Twist.B, cubeModel.Twist.BP, cubeModel.Twist.B2})):
            return True
        if (last_move in {cubeModel.Twist.B, cubeModel.Twist.BP, cubeModel.Twist.B2} and
            new_move in {cubeModel.Twist.B, cubeModel.Twist.BP, cubeModel.Twist.B2}):
            return True
        if (last_move in {cubeModel.Twist.U, cubeModel.Twist.UP, cubeModel.Twist.U2} and
            (new_move in {cubeModel.Twist.U, cubeModel.Twist.UP, cubeModel.Twist.U2} or
            new_move in {cubeModel.Twist.D, cubeModel.Twist.DP, cubeModel.Twist.D2})):
            return True
        if (last_move in {cubeModel.Twist.D, cubeModel.Twist.DP, cubeModel.Twist.D2} and
            new_move in {cubeModel.Twist.D, cubeModel.Twist.DP, cubeModel.Twist.D2}):
            return True

        if node[0].copy().twist(new_move) in self.seen:
            return True
        else:
            self.seen.add(node[0].copy().twist(new_move))

        return False


def dfs(cube: cubeModel.RubikCube, goal: Callable, moves, pruner: Pruner, max_depth: int) -> None:
    '''Does a depth first search of twists on cube to find goal state.'''

    if goal(cube):
        return (cube, [])

    queue = deque()
    for move in moves:
        queue.append((cube.copy().twist(move), [move]))

    cur_depth = 1
    while queue:
        node = queue.popleft()
        if goal(node[0]):
            break

        if len(node[1]) < max_depth:
            if len(node[1]) > cur_depth:
                cur_depth = len(node[1])
                print(cur_depth)

            for move in moves:
                if pruner.prune(move, node):
                    continue
                queue.append((node[0].copy().twist(move), node[1] + [move]))

    return node
