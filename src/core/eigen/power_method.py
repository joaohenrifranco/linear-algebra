import numpy as np


def run(A, tolm):
    n = A.shape[0]

    eigenvector = np.ones(n)
    residue = tolm + 1
    prev_eigenvalue = 1

    iteration_count = 0

    while(tolm < residue):
        iteration_count += 1

        Y = A @ eigenvector

        eigenvalue = Y[0]
        eigenvector = Y / eigenvalue

        residue = (eigenvalue - prev_eigenvalue) / eigenvalue
        prev_eigenvalue = eigenvalue

    return eigenvector, eigenvalue, iteration_count
