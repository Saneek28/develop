import math

from develop.src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        Figure.__init__(self, "circle")
        self.radius = radius


@property
def area(self):
    return math.pi * (self.radius ** 2)


@property
def perimeter(self):
    return 2 * math.pi * self.radius
