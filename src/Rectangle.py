from develop.src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        Figure.__init__(self, "rectangle")
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)
