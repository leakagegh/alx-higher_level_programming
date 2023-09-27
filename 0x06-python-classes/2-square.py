#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Square that defines a square"""
    def __init__(self, size=0):
        """Initializing new square
            Args:
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
