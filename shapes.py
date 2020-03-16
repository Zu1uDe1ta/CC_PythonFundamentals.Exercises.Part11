import shapes

class Rectangle:
    def _init_ (self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

    def perimeter(self):
        print((self.length + self.width) * 2)

class Square(Rectangle):
        length = self.length
        length = self.width

    def area(self):
        print(length * length)

    def perimeter(self):
        print(4 * length)


rect = shapes.Rectangle(2, 4)
rect.area()
# 8

square = shapes.Square(8)
square.area()
# 64

square.perimeter()
# 32
