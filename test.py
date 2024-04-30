import numpy as np
from rubik.cubeModel import *


foo = np.arange(9).reshape(3,3)

vectors = [
    foo[:,2],
    foo[2,:],
    foo[:,0],
    foo[0,:]
]

U_adj = (
    (Face.L,0,2), (Face.L,0,1), (Face.L,0,0),
    (Face.B,0,2), (Face.B,0,1), (Face.B,0,0),
    (Face.R,0,2), (Face.R,0,1), (Face.R,0,0),
    (Face.F,0,2), (Face.F,0,1), (Face.F,0,0)
)

L_adj = (
    (Face.B,2,2), (Face.B,1,2), (Face.B,0,2),
    (Face.U,0,0), (Face.U,1,0), (Face.U,2,0),
    (Face.F,0,0), (Face.F,1,0), (Face.F,2,0),
    (Face.D,0,0), (Face.D,1,0), (Face.D,2,0)
)

F_adj = (
    (Face.L,2,2), (Face.L,1,2), (Face.L,0,2),
    (Face.U,2,0), (Face.U,2,1), (Face.U,2,2),
    (Face.R,0,0), (Face.R,1,0), (Face.R,2,0),
    (Face.D,0,2), (Face.D,0,1), (Face.D,0,0)
)

R_adj = (
    (Face.F,2,2), (Face.F,1,2), (Face.F,0,2),
    (Face.U,2,2), (Face.U,1,2), (Face.U,0,2),
    (Face.B,0,0), (Face.B,1,0), (Face.B,2,0),
    (Face.D,2,2), (Face.D,1,2), (Face.D,0,2)
)

B_adj = (
    (Face.R,2,2), (Face.R,1,2), (Face.R,0,2),
    (Face.U,0,2), (Face.U,0,1), (Face.U,0,0),
    (Face.L,0,0), (Face.L,1,0), (Face.L,2,0),
    (Face.D,2,2), (Face.D,1,2), (Face.D,0,2)
)

D_adj = (
    (Face.L,2,0), (Face.L,2,1), (Face.L,2,2),
    (Face.F,2,0), (Face.F,2,1), (Face.F,2,2),
    (Face.R,2,0), (Face.R,2,1), (Face.R,2,2),
    (Face.B,2,0), (Face.B,2,1), (Face.B,2,2)
)

face_2_adj = (U_adj, L_adj, F_adj, R_adj, B_adj,D_adj)

print(vectors)