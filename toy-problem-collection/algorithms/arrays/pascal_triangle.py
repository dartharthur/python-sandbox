"""
Given num_rows, generate the first num_rows of Pascal's triangle.

Source: https://leetcode.com/problems/pascals-triangle/description/
"""


def generate_triangle(num_rows):
    """
    :type num_rows: int
    :rtype: List[List[int]]
    """
    triangle = []

    i = 1
    while i <= num_rows:
        if i == 1:
            triangle.append([1])
        elif i == 2:
            triangle.append([1, 1])
        else:
            triangle.append(generate_row(triangle[i - 2], i))
        i += 1

    return triangle


def generate_row(prev_row, num):
    """
    :type prev_row: List[int]
    :type n: int
    :rtype: List[int]
    """
    i = 0
    new_row = []
    while i < num:
        if i == 0 or i == num - 1:
            new_row.append(1)
            i += 1
        else:
            new_row.append(prev_row[i - 1] + prev_row[i])
            i += 1
    return new_row
