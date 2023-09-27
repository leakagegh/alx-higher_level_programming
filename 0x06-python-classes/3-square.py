#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Class Square that defines a square"""
    def __init__(self, size=0):
        """Initializes object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Defines area of square"""
        return self.__size ** 2
