#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n = []
    for i in matrix:
        y = list(map(lambda x: x ** 2, i))
        n.append(y)
    return n
