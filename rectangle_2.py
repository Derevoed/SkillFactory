from rectangle_aquare_circle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
print(rect_1.getArea())
print(rect_2.getArea())

print('-' * 10)

square_1 = Square(5)
square_2 = Square(10)
print(square_1.getArea_square(),
      square_2.getArea_square())

print('-' * 10)

circle_1 = Circle(12)
circle_2 = Circle(5)
print(circle_1.getArea_circle(),
      circle_2.getArea_circle())

print('-' * 10)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.getArea_square())
    elif isinstance(figure, Circle):
        print(figure.getArea_circle())
    else:
        print(figure.getArea())