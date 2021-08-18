import numpy as np

def lu_decompose(A):
  n = A.shape[0]
  pivot_row = 0
  
  for k in range(n):    
    # Find best pivot
    pivot = 0.0
    for i in range(k, n):
      if (A[i,k] > abs(pivot)):
        pivot = A[i,k]
        pivot_row = i

    # Swap rows if necessary
    if (pivot_row != k):
      for j in range (n):
        temp = A[pivot_row,j]
        A[pivot_row,j] = A[k,j]
        A[k,j] = temp

    # Fill matrix in place 
    for i in range(k+1,n):
      A[i,k] = A[i,k] / A[k,k]      # Fill L matrix
      for j in range (k+1,n):
        A[i,j] -= A[i,k] * A[k,j]   # Apply row subtration

  return A


def solve_forward_substitution(L, b):
    n = L.shape[0]
    x = np.zeros(n)
    
    for i in range(n):
        sum = b[i]
        for j in range(i-1):
            sum -= L[i,j] * x[j]
        x[i] = sum / L[i,i]
    return x

A = np.array([
  [0,1,1],
  [1,2,1],
  [2,7,9]
])

print(lu_decompose(A))