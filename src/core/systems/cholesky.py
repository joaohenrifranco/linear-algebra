import numpy as np
import math
from .. import checker

def cholesky(A):
    n = A.shape[0]
    L = np.zeros((n, n))

    if (not checker.is_simetric_positive_defined(A)):
        raise Exception("Matrix is not simetric positive defined")

    for i in range(n):
        for j in range(i+1):
            sum = 0.0
            for k in range(j):
                 sum += L[i, k] * L[j, k]
            
            if j == i:
                L[i,j] = math.sqrt(A[i,i] - sum)
            else:
                L[i,j] = (A[i,j] - sum) / L[j,j]

    return L

def computeDeterminant(L):
    n = L.shape[0]
    det = 1
    for i in range(n):
        det *= pow(L[i,i], 2)
    return det

def solve(A, B, enableDet):
    n = A.shape[0]
    x = np.zeros(n)

    L = cholesky(A)

    # Performs forward substitution
    for i in range(n):
        x[i] = B[i]
        for k in range(i):
            x[i] -= L[i, k] * x[k]
        x[i] /= L[i, i]

    # Performs backwards substitution
    # with transposed L
    for i in range(n-1, -1, -1):
        for k in range(i+1, n):
            x[i] -= L[k, i] * x[k]
        x[i] /= L[i, i]


    if (enableDet):
        return x, computeDeterminant(L)


    return x