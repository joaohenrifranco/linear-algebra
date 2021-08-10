import numpy as np

def lu_decompose(A):
  n = A.shape[0]
  i_max = 0
  
  for k in range(n):
    pivot = 0.0

    for i in range(k, n):
      if (A[i,k] > abs(pivot)):
        pivot = A[i,k]
        i_max = i
    print(pivot, i_max)

    if (A[k,k] == 0):
      for j in range (n):
        temp = A[i_max,j]
        A[i_max,j] = A[k,j]
        A[k,j] = temp

    for i in range(k+1,n):
      A[i,k] = A[i,k] / A [k,k]
      for j in range (k+1,n):
        A[i,j] -= A[i,k] * A[k,j]

  return A

A = np.array([
  [0.0,1,1],
  [1,10,1],
  [1,1,0]
])

print(lu_decompose(A))