import numpy as np


def lu_decompose(A):
    n = A.shape[0]
    pivot_row = 0

    # Creates permutation matrix equivalent,
    # the row swap tracker
    P = np.arange(0, n)

    for k in range(n):
        # Find best pivot
        pivot = 0.0
        for i in range(k, n):
            if (A[i, k] > abs(pivot)):
                pivot = A[i, k]
                pivot_row = i

        # Swap rows if necessary
        if (pivot_row != k):
            temp = P[k]
            P[k] = P[pivot_row]
            P[pivot_row] = temp

            for j in range(n):
                temp = A[pivot_row, j]
                A[pivot_row, j] = A[k, j]
                A[k, j] = temp

        # Fill matrix in place
        for i in range(k+1, n):
            A[i, k] = A[i, k] / A[k, k]      # Fill L matrix
            for j in range(k+1, n):
                A[i, j] -= A[i, k] * A[k, j]   # Apply row subtration

    return A, P


def back_substitute(U, b):
    n = U.shape[0]
    x = np.zeros(n)

    for i in range(n-1, -1, -1):
        sum = b[i]
        for j in range(i+1, n):
            sum -= U[i, j] * x[j]

        x[i] = sum / U[i, i]

    return x


def forward_substitute(L, b):
    n = L.shape[0]
    x = np.zeros(n)
    for i in range(n):
        temp = b[i]
        for j in range(i-1):
            temp -= L[i, j] * x[j]
        x[i] = temp / L[i, i]
    return x


def apply_swap_vec(P, B):
    n = B.shape[0]
    for i in range(n):
        i_pos = P[i]
        if (i != i_pos):
            # print('i, i_pos: ', i, i_pos)
            # print('p: ', P)
            # print('b: ', b)

            temp = B[i]
            B[i] = B[i_pos]
            B[i_pos] = temp

            temp = P[i]
            P[i] = P[i_pos]
            P[i_pos] = temp

            # print('i, i_pos: ', i, i_pos)
            # print('p: ', P)
            # print('b: ', b)


def solve(A, B):
    # Ax=b -> LUx=b -> Ly=b -> Ux=y
    LU, P = lu_decompose(A)
    apply_swap_vec(P, B)

    L = np.copy(LU)
    for i in range(L.shape[0]):
        L[i, i] = 1

    print(B)
    print(L)
    print(LU)
    y = forward_substitute(L, B)
    print(y)

    x = back_substitute(LU, y)

    return x


A = np.array([
    [0.0, 1, 1],
    [1, 2, 1],
    [1, 1, -1]
])

B = np.array([4, 7, 3.0])

print(solve(A, B))
