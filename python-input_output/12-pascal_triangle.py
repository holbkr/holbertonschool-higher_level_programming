#!/usr/bin/python3

'''
12-pascal_triangle.py
File that add a function that create a pascal triangle of the lenght enter
in argument
'''


def pascal_triangle(n):
    '''Function that create a pascal triangle based of n lenght'''
    if n < 0:
        return []
    else:
        pascal_triangle = []
        for i in range(0, n):
            new_row = []
            new_row.append(1)
            if i != 0:
                for k in range(0, len(pascal_triangle[i - 1]) - 1):
                    nb1 = pascal_triangle[i - 1][k]
                    nb2 = pascal_triangle[i - 1][k + 1]
                    new_row.append(nb1 + nb2)
            if i > 0:
                new_row.append(1)
            pascal_triangle.append(new_row)
        return pascal_triangle
