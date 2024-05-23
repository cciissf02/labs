class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_w(self):
        return self.w
    def get_h(self):
        return self.h
    def intersection(self, other):
        x1 = max(self.x, other.get_x())
        y1 = max(self.y, other.get_y())
        x2 = min(self.x + self.w, other.get_x() + other.get_w())
        y2 = min(self.y + self.h, other.get_y() + other.get_h())

        if x1<x2 and y1<y2:
            return Rectangle(x1, y1, x2-x1, y2-y1)
        else:
            return None

rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(10, 0, 10, 10)
rect3 = rect1.intersection(rect2)
if rect3 is None:
    print('no intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())

rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(1, 4, 8, 6)
rect3 = rect1.intersection(rect2)
if rect3 is None:
    print('no intersection')
else:
    print('intercsection', rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())