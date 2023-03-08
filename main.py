# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main

rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)

#more tests
print(rect.get_picture())
print(rect.get_amount_inside(sq))
rect.set_height(10)
rect.set_width(15)
sq.set_side(5)
print(rect.get_amount_inside(sq))

# Run unit tests automatically
main(module='test_module', exit=False)
