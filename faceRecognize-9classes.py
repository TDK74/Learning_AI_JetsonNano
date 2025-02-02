class Rectangle:
    ''' Class for calculation for area of a rectangle '''
    def __init__(self, c, w, l):
        self.width = w
        self.length = l
        self.color = c

    def area(self) -> float:
        ''' Calculate area of a rectangle and calling with return '''
        self.area = self.width * self.length

        return self.area

    def area1(self) -> None:
        ''' Calculate area of a rectangle but callign w/o return'''
        self.area1 = self.width * self.length

    def per(self) -> float:
        ''' Calculate perimeter of a rectangle '''
        self.perimeter = 2*self.width + 2*self.length

        return self.perimeter


c1 = 'red'
w1 = 3
l1 = 4
rect1 = Rectangle(c1, w1, l1)
#a way of calling
rect1.area1()
print(rect1.area1)
#a better way of calling
areaRect1 = rect1.area()
print(areaRect1)

c2 = 'blue'
w2 = 7
l2 = 3.2
rect2 = Rectangle(c2, w2, l2)
areaRect2 = rect2.area()
print(areaRect2)

print('Rectangle 1 is: ', rect1.color)
print('Rectangle 2 is: ', rect2.color)

per1 = rect1.per()
print('Rectangle 1 has perimeter', per1)
print('The', rect1.color, 'rectangle has perimeter ', per1)

per2 = rect2.per()
print('Rectangle 2 has perimeter', per2)
print('The', rect2.color, 'rectangle has perimeter ', per2)
