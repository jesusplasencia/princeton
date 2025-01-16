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
    n = A.shape[0]
    if n == 1:
        return A * B
    else:
        # Split the matrices into quadrants
        mid = n // 2
        A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
        B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]
        C11 = square_matrix_multiplication_recursive(A11, B11) + square_matrix_multiplication_recursive(A12, B21)
        C12 = square_matrix_multiplication_recursive(A11, B12) + square_matrix_multiplication_recursive(A12, B22)
        C21 = square_matrix_multiplication_recursive(A21, B11) + square_matrix_multiplication_recursive(A22, B21)
        C22 = square_matrix_multiplication_recursive(A21, B12) + square_matrix_multiplication_recursive(A22, B22)
        
        # Combine the quadrants into a single matrix
        C = np.zeros((n, n))
        C[:mid, :mid] = C11
        C[:mid, mid:] = C12
        C[mid:, :mid] = C21
        C[mid:, mid:] = C22
        return C;

import numpy as np;

def pad_matrix(A):
    """
    Pads a matrix A to the next power of 2 size.
    :param A: 2D list or numpy array
    :return: Padded numpy array
    """
    n = len(A)
    m = len(A[0])
    new_size = 2 ** int(np.ceil(np.log2(max(n, m))))
    padded_matrix = np.zeros((new_size, new_size))
    padded_matrix[:n, :m] = A
    return padded_matrix;

def strassen_matrix_multiply(A, B):
    """
    Multiply two square matrices A and B using Strassen's algorithm.
    :param A: 2D numpy array (n x n)
    :param B: 2D numpy array (n x n)
    :return: 2D numpy array (n x n)
    """
    # Base case: if the matrix is 1x1, multiply directly
    n = A.shape[0]
    if n == 1:
        return A * B

    # Split the matrices into quadrants
    mid = n // 2
    A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    # Compute the 7 products (Strassen's key step)
    P1 = strassen_matrix_multiply(A11 + A22, B11 + B22)
    P2 = strassen_matrix_multiply(A21 + A22, B11)
    P3 = strassen_matrix_multiply(A11, B12 - B22)
    P4 = strassen_matrix_multiply(A22, B21 - B11)
    P5 = strassen_matrix_multiply(A11 + A12, B22)
    P6 = strassen_matrix_multiply(A21 - A11, B11 + B12)
    P7 = strassen_matrix_multiply(A12 - A22, B21 + B22)

    # Combine the products into the resulting matrix quadrants
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6

    # Combine the quadrants into a single matrix
    C = np.zeros((n, n))
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22

    return C;

# Example Matrices
A = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]]);
B = np.array([[1, 4, 6], [2, 3, 5], [6, 7, 8]]);

# Ensure matrices are square and padded if necessary
A_padded = pad_matrix(A);
B_padded = pad_matrix(B);

# Perform Strassen's matrix multiplication
result = strassen_matrix_multiply(A_padded, B_padded);

# Trim the result to the original size
result = result[:len(A), :len(B[0])]

print("Recursive-Method To Multiply Matrices:");
print(result);