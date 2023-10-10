#!/usr/bin/python3
"""Write a class Square that defines a square """


class Square:
    """Write a class Square that defines a square """
    def __init__(self, size=0):
        """Initializing object instance"""
        self.size = size

    @property
    def size(self):
        """Get size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return Area of square"""
        return self.__size ** 2
