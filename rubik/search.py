from collections import deque
from dataclasses import dataclass, field
from typing import Callable, Iterable

import cubeModel

@dataclass
class Node:
    cube: cubeModel.RubikCube
    moves: list[cubeModel.Twist] = field(default_factory=list)

class Pruner:
    def __init__(self, init_cube):
        self.seen = {init_cube}

    def prune(self, new_move, node: Node):
        last_move = node.moves[-1]

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

        if node.cube.copy().twist(new_move) in self.seen:
            return True
        else:
            self.seen.add(node.cube.copy().twist(new_move))

        return False


def dfs(cube: cubeModel.RubikCube, goal: Callable, moves: Iterable, pruner: Pruner, max_depth: int) -> Node:
    '''Does a depth first search of twists on cube to find goal state.'''

    if goal(cube):
        return Node(cube)

    queue = deque()
    for move in moves:
        queue.append(Node(cube.copy().twist(move), [move]))

    cur_depth = 1
    while queue:
        node = queue.pop()
        if goal(node.cube):
            break

        if len(node.moves) < max_depth:
            if len(node.moves) > cur_depth:
                cur_depth = len(node.moves)
                print(cur_depth)

            for move in moves:
                if pruner.prune(move, node):
                    continue
                queue.append(Node(node.cube.copy().twist(move), node.moves + [move]))

    return node

def ida_star(cube: cubeModel.RubikCube, goal: Callable, moves, pruner: Pruner, max_depth: int) -> Node:
    '''Performs a iteratively deepending A* search.'''

    if goal(cube):
        return Node(cube)

    queue = deque()
    for move in moves:
        queue.append(Node(cube.copy().twist(move), [move]))

    cur_depth = 1
    while queue:
        node = queue.popleft()
        if goal(node.cube):
            break

        if len(node.moves) < max_depth:
            if len(node.moves) > cur_depth:
                cur_depth = len(node.moves)
                print(cur_depth)

            for move in moves:
                if pruner.prune(move, node):
                    continue
                queue.append(Node(node.cube.copy().twist(move), node.moves + [move]))

    return node

def bfs(cube: cubeModel.RubikCube, goal: Callable, moves: Iterable, pruner: Pruner, max_depth: int) -> Node:

    if goal(cube):
        return Node(cube)

    queue = deque()
    for move in moves:
        queue.append(Node(cube.copy().twist(move), [move]))

    cur_depth = 1
    while queue:
        node = queue.pop()
        if goal(node.cube):
            break

        if len(node.moves) < max_depth:
            if len(node.moves) > cur_depth:
                cur_depth = len(node.moves)
                print(cur_depth)

            for move in moves:
                if pruner.prune(move, node):
                    continue
                queue.append(Node(node.cube.copy().twist(move), node.moves + [move]))

    return node