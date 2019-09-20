class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        super(Rectangle, self).__init__(color)

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width * self.length)

    def __mul__(self, other):
        self.width *= other
        self.length *= other

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.area() == other.area() and self.perimeter() == other.perimeter()

    def __str__(self):
        return "Rectangle : {} X {}".format(self.width, self.length)

    def __repr__(self):
        return str(self)
if __name__ == '__main__':
    rec1 = Rectangle(4,5, 'Yellow')
    rec2 = Rectangle(5,20 , 'Black')
    print(rec1)
    print(rec2)
    rectangles = [rec1, rec2]
    print(rectangles)
