from dataclasses import dataclass

import rubik.cubeModel as cubeModel


#### Constants ####

#### Classes ####

@dataclass
class Node:
    cube: cubeModel.RubikCube
    moves: list[str]


#### Functions ####

def g1_solved(cube:cubeModel.RubikCube) -> bool:
    UB = cube.getColor(cube.Face.UP, 0, 1)
    UL = cube.getColor(cube.Face.UP, 1, 0)
    UR = cube.getColor(cube.Face.UP, 1, 2)
    UF = cube.getColor(cube.Face.UP, 2, 1)

    LU = cube.getColor(cube.Face.LEFT, 0, 1)
    LB = cube.getColor(cube.Face.LEFT, 1, 0)
    LF = cube.getColor(cube.Face.LEFT, 1, 2)
    LD = cube.getColor(cube.Face.LEFT, 2, 1)

    FU = cube.getColor(cube.Face.FRONT, 0, 1)
    FL = cube.getColor(cube.Face.FRONT, 1, 0)
    FR = cube.getColor(cube.Face.FRONT, 1, 2)
    FD = cube.getColor(cube.Face.FRONT, 2, 1)

    RU = cube.getColor(cube.Face.RIGHT, 0, 1)
    RF = cube.getColor(cube.Face.RIGHT, 1, 0)
    RB = cube.getColor(cube.Face.RIGHT, 1, 2)
    RD = cube.getColor(cube.Face.RIGHT, 2, 1)

    BU = cube.getColor(cube.Face.BACK, 0, 1)
    BL = cube.getColor(cube.Face.BACK, 1, 0)
    BR = cube.getColor(cube.Face.BACK, 1, 2)
    BD = cube.getColor(cube.Face.BACK, 2, 1)

    DF = cube.getColor(cube.Face.DOWN, 0, 1)
    DL = cube.getColor(cube.Face.DOWN, 1, 0)
    DR = cube.getColor(cube.Face.DOWN, 1, 2)
    DB = cube.getColor(cube.Face.DOWN, 2, 1)

    return (
      (UF == cube.Colour.BLUE or UF == cube.Colour.GREEN or FU == cube.Colour.WHITE or FU == cube.Colour.YELLOW) and
      (UB == cube.Colour.BLUE or UB == cube.Colour.GREEN or BU == cube.Colour.WHITE or BU == cube.Colour.YELLOW) and
      (DF == cube.Colour.BLUE or DF == cube.Colour.GREEN or FD == cube.Colour.WHITE or FD == cube.Colour.YELLOW) and
      (DB == cube.Colour.BLUE or DB == cube.Colour.GREEN or BD == cube.Colour.WHITE or BD == cube.Colour.YELLOW) and
      (LU == cube.Colour.BLUE or LU == cube.Colour.GREEN or UL == cube.Colour.WHITE or UL == cube.Colour.YELLOW) and
      (LD == cube.Colour.BLUE or LD == cube.Colour.GREEN or DL == cube.Colour.WHITE or DL == cube.Colour.YELLOW) and
      (RU == cube.Colour.BLUE or RU == cube.Colour.GREEN or UR == cube.Colour.WHITE or UR == cube.Colour.YELLOW) and
      (RD == cube.Colour.BLUE or RD == cube.Colour.GREEN or DR == cube.Colour.WHITE or DR == cube.Colour.YELLOW) and
      (LF == cube.Colour.BLUE or LF == cube.Colour.GREEN or FL == cube.Colour.WHITE or FL == cube.Colour.YELLOW) and
      (LB == cube.Colour.BLUE or LB == cube.Colour.GREEN or BL == cube.Colour.WHITE or BL == cube.Colour.YELLOW) and
      (RF == cube.Colour.BLUE or RF == cube.Colour.GREEN or FR == cube.Colour.WHITE or FR == cube.Colour.YELLOW) and
      (RB == cube.Colour.BLUE or RB == cube.Colour.GREEN or BR == cube.Colour.WHITE or BR == cube.Colour.YELLOW))

def g2_solved(cube:cubeModel.RubikCube) -> bool:
    pass

def g3_solved(cube:cubeModel.RubikCube) -> bool:
    pass

def depth_first_search(cube:cubeModel.RubikCube, goal, pos_moves):
    stack = [Node(cube)]

    cur_node = stack.pop()
    while not goal(cur_node):
        pass



def thistlethwaite(cube) -> str:
    pass


if __name__ == '__main__':
    pass