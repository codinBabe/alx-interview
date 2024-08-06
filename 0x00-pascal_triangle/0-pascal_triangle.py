#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """
    Generate a Pascal's Triangle of 'n' rows.

    Args:
    n (int): The number of rows in the triangle.

    Returns:
    list: A list of lists representing the Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
