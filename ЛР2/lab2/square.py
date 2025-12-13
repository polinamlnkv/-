from lab2.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)

    @property
    def name(self):
        return "Квадрат"

    def __repr__(self):
        return "{} {} цвета со стороной {}. Площадь: {}".format(
            self.name,
            self.color.color,
            self.width,
            self.area()
        )
