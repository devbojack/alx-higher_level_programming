#!/usr/bin/python3
"""MagicClass that does exactly as the bytecode provided"""

import math


class MagicClass:
    """Circle representation"""

    def __init__(self, radius=0):
        """Initialization

        Arg: radius (float or int): Magicclass radius
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
