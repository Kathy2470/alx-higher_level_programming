#!/usr/bin/python3
"""Module to perform matrix multiplication using NumPy
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        numpy.ndarray: Result of the matrix multiplication.

    Raises:
        ValueError: If matrices cannot be multiplied.
    """
    matrix_a = np.array(m_a)
    matrix_b = np.array(m_b)

    if matrix_a.shape[1] != matrix_b.shape[0]:
        raise ValueError("shapes {} and {} not aligned: {} (dim 1) != {} (dim 0)"
                         .format(matrix_a.shape, matrix_b.shape, matrix_a.shape[1], matrix_b.shape[0]))

    result = np.dot(matrix_a, matrix_b)
    return (result)
