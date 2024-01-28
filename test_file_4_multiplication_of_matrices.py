from Multiply_matrices_2nos.py import matrix_multiply

# Test Case 1: Correct input
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[7, 8],
     [9, 10],
     [11, 12]]
result = matrix_multiply(A, B)
assert result == [[58, 64], [139, 154]], "Test Case 1 failed"

# Test Case 2: Incorrect input - Number of columns in A is not equal to the number of rows in B
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[7, 8],
     [9, 10]]
try:
    result = matrix_multiply(A, B)
except ValueError as e:
    assert str(e) == "Number of columns in matrix A must be equal to the number of rows in matrix B", "Test Case 2 failed"

# Test Case 3: Empty matrices
A = []
B = []
result = matrix_multiply(A, B)
assert result == [], "Test Case 3 failed"

# Test Case 4: Identity matrix
A = [[1, 0],
     [0, 1]]
B = [[2, 3],
     [4, 5]]
result = matrix_multiply(A, B)
assert result == B, "Test Case 4 failed"
