import numpy as np
import checker

def solve(A, B, rtol):
    n = A.shape[0]
    residue = rtol + 1
    X = np.ones(n)

    if (not checker.is_simetric_positive_defined(A) and not checker.is_diagonal_dominant(A)):
        return -1

    while(residue > rtol):
        X_current = np.ones(n)

        for i in range(n):
            subtrahend = 0

            for j in range(i):
                subtrahend += A[i, j] * X_current[j]

            for j in range(i + 1, n):
                subtrahend += A[i, j] * X[j]

            X_current[i] = (B[i] - subtrahend) / A[i, i]

        residue = np.linalg.norm(X_current - X, ord=2) / \
            np.linalg.norm(X_current, ord=2)
        X = X_current

    return X
