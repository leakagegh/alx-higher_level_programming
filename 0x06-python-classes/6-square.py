#!/usr/bin/python3
"""Square class with modules"""


class Square:
    """Square class with modules"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize object instance

        Args:
        size (int): The size of the new square.
        position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size attribute values"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Position attribute value"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Check all cases of position error; verification"""
        if (
                not isinstance(value, tuple)
                or len(value) != 2
                or not isinstance(value[0], int)
                or not isinstance(value[1], int)
                or any(num < 0 for num in value)
                ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
            return
# Print both vertical and horizontal blanks
        else:
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end='')
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
