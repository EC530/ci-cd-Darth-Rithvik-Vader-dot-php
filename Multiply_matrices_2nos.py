'''
 Python program to multiply 2 matrices
 Naming the matrices A and B
 C is the product matrix
 C = A.B
 print C
'''
def matrix_multiply(A, B):
    """
    Multiply two matrices A and B and return the result.

    Parameters:
    A: First matrix
    B: Second matrix

    Returns:
    Resulting matrix C = A * B
    """
    # Check if the number of columns in A is equal to the number of rows in B
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in matrix A must be equal to the number of rows in matrix B")

    # Initialize the result matrix with zeros
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Perform matrix multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C
