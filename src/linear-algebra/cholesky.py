import numpy as np
import math

def cholesky(A, tol):
    n = A.shape[0]
    L = np.zeros((n, n))

    if (not is_simetric_positive_defined(A)):
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

def solve(A, b):
    n = A.shape[0]
    x = np.zeros(n)

    L = cholesky(A, 0.0)
    Lt = np.transpose(L)

    print('L', L)

    # Performs forward substitution
    for i in range(n):
        x[i] = b[i]
        for k in range(i):
            print(x)
            x[i] -= L[i, k] * x[k]
        x[i] /= L[i, i]

    print('y',x)

    # Performs backwards substitution
    for i in range(n-1, -1, -1):
        for k in range(i+1, n):
            x[i] -= Lt[i, k] * x[k]
        x[i] /= Lt[i, i]

    return x


A = np.array([
    [1, 0.2, 0.4],
    [0.2, 1, 0.5],
    [0.4, 0.5, 1]
])
B = np.array([0.6, -0.3, -0.6])
ans = np.array([1,  0, -1.])

print(solve(A, B))
print(ans)
