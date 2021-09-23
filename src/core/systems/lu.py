import numpy as np

# Input matrix is replaced with LU matrix
# Output is the replaced A matrix with a 
# permutation matrix represented as position vector
def lu_decompose(A):
    n = A.shape[0]
    pivot_row = 0

    # Creates permutation matrix equivalent,
    # the row swap tracker
    P = np.arange(0, n)

    # Permutation count
    P_count = 0

    for k in range(n):
        # Find best pivot
        pivot_abs = 0.0
        for i in range(k, n):
            current_abs = abs(A[i, k])
            if (current_abs > pivot_abs):
                pivot_abs = current_abs
                pivot_row = i

        # Swap rows if necessary
        if (k != pivot_row):
            P_count += 1
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

    return A, P, P_count

def computeDeterminantLU(A, P_count):
    n = A.shape[0]
    det = A[0,0]

    for i in range(n):
        det *= A[i,i]

    if (P_count % 2 != 0):
        return -det

    return det

def computeDeterminant(A, copy):
    LU = A
    if copy:
        LU = A.copy()
        
    (LU, _, P_count) = lu_decompose(LU)
    return computeDeterminantLU(LU, P_count)

def solve(A, B, enableDet):
    n = A.shape[0]
    x = np.zeros(n)

    (A, P, P_count) = lu_decompose(A)

    # Performs permutation on B vector and
    # forward substitution
    for i in range(n):
        x[i] = B[P[i]]
        for k in range(i):
            x[i] -= A[i,k] * x[k]
        x[i] /= A[i, i]

    # Performs backwards substitution
    for i in range(n-1, -1, -1):
        for k in range(i+1,n):
            x[i] -= A[i,k] * x[k]
        
        x[i] /= A[i,i]

    if enableDet:
        return x, computeDeterminantLU(A, P_count)

    return x, 0.0