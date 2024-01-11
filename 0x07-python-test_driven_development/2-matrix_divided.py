"""
This is a doctest file for the 'matrix_divided' function.

>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 2)
[[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

>>> matrix_divided([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], 2.5)
[[0.4, 0.8, 1.2], [1.6, 2.0, 2.4]]

>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0.5)
[[2.0, 4.0, 6.0], [8.0, 10.0, 12.0]]

>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero

>>> matrix_divided([[1, 2, 3], [4, 5, 6]], '2')
Traceback (most recent call last):
    ...
TypeError: div must be a number

>>> matrix_divided([[1, 2, 3], [4, 5, 6]], [2])
Traceback (most recent call last):
    ...
TypeError: div must be a number

>>> matrix_divided([[1, 2, 3], [4, 5]], 2)
Traceback (most recent call last):
    ...
TypeError: Each row of the matrix must have the same size

>>> matrix_divided('not_a_matrix', 2)
Traceback (most recent call last):
    ...
TypeError: matrix must be a matrix (list of lists) of integers/floats
"""
