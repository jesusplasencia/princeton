# Page 98

def square_matrix_multiplication(A, B):
    """
    T(n) = O(n^3)
    >>> A = [ [1, 3, 6], [2, 5, 8], [3, 7, 9] ];
    >>> B = [ [0, 8, 4], [2, 6, 7], [2, 1, 1] ];
    >>> square_matrix_multiplication(A, B);
    [[18, 32, 31], [26, 54, 51], [32, 75, 70]]
    """
    n = len(A);
    C = [ [ 0 for _ in range(n) ] for _ in range(n) ];

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j];
    return C;

def square_matrix_multiplication_recursive(A, B):
    n = len(A);
    C = [ [ 0 for _ in range(n) ] for _ in range(n) ];

    if n == 1:
        C[0][0] = A[0][0] * B[0][0];
    else

    return C;