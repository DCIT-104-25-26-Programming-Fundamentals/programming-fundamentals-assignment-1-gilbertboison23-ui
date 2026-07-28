# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, label=""):
    print(f"\nEnter {label}:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


def print_matrix(matrix, title=""):
    if title:
        print(f"\n{title}:")
    width = max(len(str(val)) for row in matrix for val in row)
    for row in matrix:
        print("  ".join(str(val).rjust(width) for val in row))


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result


def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            result[i][j] = total
    return result


if __name__ == "__main__":
    # --- Part A: Transpose ---
    print("=== Part A: Transpose a Matrix ===")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols, "the matrix")

    print_matrix(matrix, "Original Matrix")
    print_matrix(transpose(matrix), "Transposed Matrix")

    # --- Part B: Addition ---
    print("\n=== Part B: Add Two Matrices ===")
    print(f"Both matrices must be {rows} x {cols}.")
    matrix_a = read_matrix(rows, cols, "Matrix A")
    matrix_b = read_matrix(rows, cols, "Matrix B")

    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")
    print_matrix(add_matrices(matrix_a, matrix_b), "Sum (A + B)")

    # --- Part C: Multiplication ---
    print("\n=== Part C: Multiply Two Matrices ===")
    m = int(input("Enter rows for Matrix A (M): "))
    n = int(input("Enter columns for Matrix A / rows for Matrix B (N): "))
    p = int(input("Enter columns for Matrix B (P): "))

    matrix_a2 = read_matrix(m, n, "Matrix A")
    matrix_b2 = read_matrix(n, p, "Matrix B")

    print_matrix(matrix_a2, "Matrix A")
    print_matrix(matrix_b2, "Matrix B")
    print_matrix(multiply_matrices(matrix_a2, matrix_b2), "Product (A x B)")