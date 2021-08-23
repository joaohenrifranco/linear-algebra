def is_diagonal_dominant(A):
    n = A.shape[0]

    for i in range(n):
        row_sum = 0
        column_sum = 0

        for j in range(n):
            if (i == j):
                continue
            row_sum += abs(A[i, j])
            column_sum += abs(A[j, i])

        if (abs(A[i, i]) < row_sum or abs(A[i, i]) < column_sum):
            return False

    return True

def is_simetric_positive_defined(A):
    n = A.shape[0]

    for i in range(n):
        if A[i, i] < 0:
            return False

        for j in range(n):
            if A[i, j] != A[j, i]:
                return False

    return True