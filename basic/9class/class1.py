class Rectangle:
    count = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def calc_area(self):
        area = self.width * self.height
        return area

    @classmethod
    def print_count(cls):
        print(cls.count)

rect1 = Rectangle(5, 5)
rect2 = Rectangle(2, 5)
rect1.print_count() # 2
print(rect1.calc_area())