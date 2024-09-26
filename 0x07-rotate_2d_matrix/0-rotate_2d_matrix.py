#!/usr/bin/python
"""Rotate matrix , rotate it 90 degrees clockwise."""


def rotate_2d_matrix(matrix: list) -> None:
    """Rotate matrix."""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
