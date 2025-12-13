from lab2.figure import Figure
from lab2.color import Color

class Rectangle(Figure):
    def __init__(self, color, width, height):
        self.color = Color(color)
        self.width = width
        self.height = height

    @property
    def name(self):
        return "Прямоугольник"

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {}. Площадь: {}".format(
            self.name,
            self.color.color,
            self.width,
            self.height,
            self.area()
        )
