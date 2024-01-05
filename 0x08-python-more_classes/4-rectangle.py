#!/usr/bin/python3
"""Defines a Rectangle class."""
class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self._validate_dimension('_width', value)

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self._validate_dimension('_height', value)

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        return 2 * (self.__width + self.__height) if self.__width != 0 and self.__height != 0 else 0

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def _validate_dimension(self, attribute, value):
        """Validate and set the width or height attribute."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute[1:]} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute[1:]} must be >= 0")
        setattr(self, attribute, value)
