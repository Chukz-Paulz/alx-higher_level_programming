#!/usr/bin/python3
# 100-matrix_mul.py
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """
    def validate_matrix(matrix, matrix_name):
        if not isinstance(matrix, list):
            raise TypeError(f"{matrix_name} must be a list")
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(f"{matrix_name} must be a list of lists")
        if not all((isinstance(ele, int) or isinstance(ele, float))
                   for ele in [num for row in matrix for num in row]):
            raise TypeError(f"{matrix_name} should contain only integers or floats")
        if not matrix or any(len(row) != len(matrix[0]) for row in matrix):
            raise TypeError(f"Each row of {matrix_name} must be of the same size")

    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Transpose matrix_b
    transposed_b = [[m_b[row][col] for row in range(len(m_b))] for col in range(len(m_b[0]))]

    # Matrix multiplication
    result = [[sum(x * y for x, y in zip(row_a, col_b)) for col_b in transposed_b] for row_a in m_a]

    return result
