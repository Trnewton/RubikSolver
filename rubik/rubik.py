from dataclasses import dataclass

import numpy as np


#### Classes ####
#TODO: This won't work for arbitrary dimensional cubes

class RubikCube:
    '''Represents orientation of Rubik cube.'''
    faces: list[np.array]
    col_2_face: dict = {
        'w' : 0,
        'o' : 1,
        'b' : 2,
        'r' : 3,
        'g' : 4,
        'y' : 5
    }
    col_2_adj: list = [
        [1,2,3,4],  # w
        [5,2,0,4],  # o
        [1,5,3,0],  # b
        [0,2,5,4],  # r
        [1,0,3,5],  # g
        [3,2,1,4]   # y
    ]

    def __init__(self, faces) -> None:
        ''''''
        self.faces = np.array(sorted(faces, key=lambda f: self.col_2_face[f[1][1]]), dtype=str)

    def rotate_face(self, face:str, rotation:int) -> None:
        ''''''

        idx = self.col_2_face[face]

        # rotate sides
        store = []
        for adj_face in self.col_2_adj[idx]:
            side = self.col_2_adj[adj_face].index(idx)

            if side == 0: # left
                column = np.flip(self.faces[adj_face][:,0].copy())
                store.append([side, column])
            elif side == 1: # top
                row = self.faces[adj_face][0].copy()
                store.append([side, row])
            elif side == 2: # right
                column = np.flip(self.faces[adj_face][:,2].copy())
                store.append([side, column])
            elif side == 3: # bottom
                row = self.faces[adj_face][2].copy()
                store.append([side, row])

        for n, adj_face in enumerate(self.col_2_adj[idx]):
            _, vec = store[n-rotation].copy()
            side, _ = store[n]
            if side == 0: # left
                self.faces[adj_face][:,0] = vec
            elif side == 1: # top
                self.faces[adj_face][0] = vec
            elif side == 2: # right
                self.faces[adj_face][:,2] = vec
            elif side == 3: # bottom
                self.faces[adj_face][2] = vec

        # rotate face
        self.faces[idx] = np.rot90(self.faces[idx], k=-rotation)

    #TODO: Finish
    def get_col(self, face, x, y, ref_face=None) -> str:
        ''''''
        if ref_face is None:
            ref_face = 'w' if face in ['w','y'] else 'o'

        # TODO: Add check for ref_face
        ref_idx = self.col_2_face(ref_face)
        idx = self.col_2_face(face)

        return ''

    def print(self):
        ''''''
        # TODO: Make print in cuibe layout
        for colour, idx in self.col_2_face.items():
            print(colour)
            print(self.faces[idx])

    def __str__(self):
        name = ''
        for row in self.faces[2]:
            name += f'\t|{"|".join(r for r in row)}|\n'
        name += '\t-------\n'

        for n in range(3):
            name += f'|{"|".join(r for r in self.faces[1][n])}|'
            name += f'\t|{"|".join(r for r in self.faces[0][n])}|'
            name += f'\t|{"|".join(r for r in self.faces[3][n])}|'
            name += f'\t|{"|".join(r for r in self.faces[5][n])}|\n'

        name += '\t-------\n'

        for row in self.faces[4]:
            name += f'\t|{"|".join(r for r in row)}|\n'

        return name