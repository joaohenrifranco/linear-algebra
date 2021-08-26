import numpy as np
from ..systems import gauss_seidel


def least_squares(P):
    n = P.shape[0]

    A = np.identity(2)
    A[0, 0] = n
    A[0, 1] = sum(P[i, 0] for i in range(n))
    A[1, 0] = A[0, 1]
    A[1, 1] = sum((P[i, 0] ** 2) for i in range(n))

    C = np.array([0., 0.])
    C[0] = sum(P[i, 1] for i in range(n))
    C[1] = sum(P[i, 0] * P[i, 1] for i in range(n))

    B = gauss_seidel.solve(A, C, 0.0001)

    return B


def get_interpolated(P, x0):
    B = least_squares(P)
    y0 = B[0] + x0 * B[1]

    return y0