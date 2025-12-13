from lab2.figure import Figure
from lab2.color import Color
import math

class Circle(Figure):
    def __init__(self, color, radius):
        self.color = Color(color)
        self.radius = radius

    @property
    def name(self):
        return "Круг"

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "{} {} цвета радиусом {}. Площадь: {:.2f}".format(
            self.name,
            self.color.color,
            self.radius,
            self.area()
        )
