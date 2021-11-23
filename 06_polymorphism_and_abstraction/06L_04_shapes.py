import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    # @property
    # def radius(self):
    #     return self.__radius
    #
    # @radius.setter
    # def radius(self, value):
    #     self.__radius = value
    #     return self.__radius

    def calculate_area(self):
        return self.__radius * self.__radius * math.pi

    def calculate_perimeter(self):
        return 2 * self.__radius * math.pi


class Rectangle(Shape):

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    # @property
    # def height(self):
    #     return self.__height
    #
    # @height.setter
    # def height(self, value):
    #     self.__height = value
    #     return self.__height
    #
    # @property
    # def width(self):
    #     return self.__width
    #
    # @width.setter
    # def width(self, value):
    #     self.__width = value
    #     return self.__width

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
