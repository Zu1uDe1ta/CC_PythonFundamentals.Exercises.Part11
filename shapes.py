

class Rectangle:
    def _init_ (self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

    def perimeter(self):
        print((self.length + self.width) * 2)

class Square(Rectangle):
    def _init_(self, length, width):
        length = self.length
        width = self.width

    def area(self):
        print(self.length ** 2)

    def perimeter(self):
        print(4 * self.length)


"""
rect = shapes.Rectangle(2, 4)
rect.area()
# 8

square = shapes.Square(8)
square.area()
# 64

square.perimeter()
# 32
"""