#!/usr/bin/python3
"""
    pascal triangle function
"""


def pascal_triangle(n):
    """ Function that represent  the pascal's triangle.
        n: the number
        Return: a list
    """
    if n <= 0:
        return []

    my_list = []
    for row in range(n):
        if row == 0:
            my_list.append([1])
        else:
            my_list.append([1] + [my_list[row - 1][column]
                           + my_list[row - 1][column + 1]
                           for column in range(row - 1)] + [1])
    return my_list
