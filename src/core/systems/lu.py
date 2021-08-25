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

def solve(A, b):
    n = A.shape[0]
    x = np.zeros(n)

    (A, P) = lu_decompose(A)

    # Performs permutation on B vector and
    # foward substitution
    for i in range(n):
        x[i] = b[P[i]]
        for k in range(i):
            x[i] -= A[i,k] * x[k]
        x[i] /= A[i, i]

    # Performs backwards substitution
    for i in range(n-1, -1, -1):
        for k in range(i+1,n):
            x[i] -= A[i,k] * x[k]
        
        x[i] /= A[i,i]

    return x

A = np.array([
    [0.0, 1, 1],
    [1, 2, 1],
    [1, 1, -1]
])
B = np.array([4, 7, 3.0])
ans = np.array([-1.,  4., 0.])

print(solve(A, B))
print(ans)