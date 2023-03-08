import math


class Rectangle:
  width = None
  height = None

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    area = (self.width * self.height)
    return area

  def get_perimeter(self):
    perimeter = (2 * self.width + 2 * self.height)
    return perimeter

  def get_diagonal(self):
    diagonal = ((self.width**2 + self.height**2)**.5)
    return diagonal

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      picture = "Too big for picture."
    else:
      picture = ""
      width_line = ""
      for i in range(0, self.width):
        width_line += "*"

      for i in range(0, self.height):
        picture += width_line
        #if i < (self.height - 1):
        picture += "\n"

    return picture

  def get_amount_inside(self, other_shape): 
    if other_shape.height > self.height or other_shape.width > self.width:
      return 0    
    
    amount_inside = 0
    amount_in_width = 0
    amount_in_height = 0

    if other_shape.height <= self.height:
      amount_in_width = int(self.width / other_shape.width)    

    if other_shape.width <= self.width:
      amount_in_height = int(self.height / other_shape.height)
    
    if amount_in_height != 0 and amount_in_width != 0:
      amount_inside = amount_in_height*amount_in_width
    elif amount_in_width == 0:
      amount_inside = amount_in_height
    else:
      amount_inside = amount_in_width      

    return amount_inside

  def __repr__(self) -> str:
    return "Rectangle(width=" + str(self.width) + ", height=" + str(
      self.height) + ")"


class Square(Rectangle):

  def __init__(self, side):
    self.width = side
    self.height = side

  def set_width(self, new_width):
    self.width = new_width
    self.height = new_width

  def set_height(self, new_height):
    self.height = new_height
    self.width = new_height

  def set_side(self, new_side):
    self.set_width(new_side)
    self.set_height(new_side)

  def __repr__(self) -> str:
    return "Square(side=" + str(self.height) + ")"
