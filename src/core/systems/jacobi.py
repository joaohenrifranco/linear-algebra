import numpy as np
from .. import checker

def solve(A, B, tolm):
    n = A.shape[0]
    residue = tolm + 1
    X = np.ones(n)

    iteration_count = 0
    residue_history = []

    if (not checker.is_diagonal_dominant(A)):
        raise Exception(
            "Method diverges: matrix is not diagonal dominant"
        )

    while(residue > tolm):
        iteration_count += 1
        residue_history.append(residue)

        X_current = np.ones(n)

        for i in range(n):
            subtrahend = 0

            for j in range(n):
                if (j == i):
                    continue
                subtrahend += A[i, j] * X[j]

            X_current[i] = (B[i] - subtrahend) / A[i, i]

        residue = np.linalg.norm(X_current - X, ord=2) / \
            np.linalg.norm(X_current, ord=2)
        X = X_current

    return X, iteration_count, residue_history
