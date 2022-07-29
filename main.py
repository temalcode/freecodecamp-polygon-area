import math

class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return  ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    picture_string = ""
    if (not(self.width > 50 or self.height > 50)):
      for i in range(self.height):
        for j in range(self.width):
          picture_string += "*"
        picture_string += "\n"
      return picture_string
    else:
      return 'Too big for picture.'

  def get_amount_inside(self, shape):
    user_shape_area = shape.height * shape.width
    shape_area = self.height * self.width
    return math.floor(shape_area / user_shape_area)
  
  def __str__(self):
    return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'

class Square(Rectangle):
  
  def __init__(self, sideLength):
    self.height = sideLength
    self.width = sideLength
    super().__init__(sideLength, sideLength)
  
  def set_side(self, sideLength):
    self.width = sideLength
    self.height = sideLength
    super().set_width(sideLength)
    super().set_height(sideLength)

  def set_height(self, height):
    self.width = height
    self.height = height
    super().set_height(height)
    super().set_width(height)
  
  def set_width(self, width):
    self.width = width
    self.height = width
    super().set_width(width)
    super().set_height(width)
  
  def __str__(self):
    return 'Square(side='+str(self.width)+')'
