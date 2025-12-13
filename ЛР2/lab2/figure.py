from abc import ABC, abstractmethod

class Figure(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def __repr__(self):
        return "{} {} цвета площадью {}".format(
            self.name,
            self.color.color,
            self.area()
        )
