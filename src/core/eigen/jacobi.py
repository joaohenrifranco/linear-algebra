import numpy as np
import checker


def eigen_jacobi(A, tolm=0.00000001):
    n = A.shape[0]

    if not checker.is_simetric(A):
        raise Exception("Matrix is not simetric")

    X = np.identity(n)
    residue = tolm + 1

    while(residue > tolm):
        # Finds greater absolute value position outside diagonal
        greatest_el = 0
        for i in range(n):
            for j in range(n):
                if i != j and abs(A[i, j]) > abs(greatest_el):
                    greatest_el_pos = (i, j)
                    greatest_el = A[i, j]

        # Compute phi for P matrix
        i, j = greatest_el_pos
        if (A[i, i] != A[j, j]):
            phi = 1/2 * np.arctan(2 * A[i, j] / (A[i, i] - A[j, j]))
        else:
            phi = np.pi / 4

        # Compute P matrix
        P = np.identity(n)
        P[i, i] = np.cos(phi)
        P[j, j] = np.cos(phi)
        P[j, i] = np.sin(phi)
        P[i, j] = -np.sin(phi)

        # Next iteration A matrix
        residue = abs(greatest_el)
        A = np.transpose(P) @ A @ P
        X = X @ P

    eigenvalues = np.zeros(n)

    # Eigenvalues are the values in the main diagonal
    for i in range(n):
        for j in range(n):
            if i == j:
                eigenvalues[i] = A[i, j]

    eigenvectors = X

    return eigenvectors, eigenvalues
