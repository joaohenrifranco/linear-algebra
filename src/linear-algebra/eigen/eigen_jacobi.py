import numpy as np
import checker


def eigen_jacobi(A, rtol=0.00000001):
    order = A.shape[0]

    if not checker.is_simetric(A):
        raise Exception("Matrix is not simetric")

    X = np.identity(order)
    residue = rtol + 1

    while(residue > rtol):
        # Finds greater absolute value position outside diagonal
        greatest_el = 0
        for i in range(order):
            for j in range(order):
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
        P = np.identity(order)
        P[i, i] = np.cos(phi)
        P[j, j] = np.cos(phi)
        P[j, i] = np.sin(phi)
        P[i, j] = -np.sin(phi)

        # Next iteration A matrix
        residue = abs(greatest_el)
        A = np.transpose(P) @ A @ P
        X = X @ P

    eigenvalues = np.zeros(order)

    # Eigenvalues are the values in the main diagonal
    for i in range(order):
        for j in range(order):
            if i == j:
                eigenvalues[i] = A[i, j]

    eigenvectors = X

    return eigenvectors, eigenvalues
