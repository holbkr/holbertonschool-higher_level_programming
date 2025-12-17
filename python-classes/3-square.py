#!/usr/bin/python3
"""Defines a Square class and computes its area."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): Size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
