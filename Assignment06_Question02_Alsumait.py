# Assignment 06, Question 02

import math

class Shape:
    
    def area(self):
        print("Shape.area")
        
    def perimeter(self):
        print("Shape.perimeter")
        
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        Area = math.pi*(self.radius**2)
        print(f"The area of the circle is {Area}")
        
    def perimeter(self):
        Perimeter = 2*math.pi*self.radius
        print(f"The perimeter of the circle is {Perimeter}")
    
class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        Area = self.length*self.width
        print(f"The area of the rectangle is {Area}")
        
            
    def perimeter(self):
        Perimeter = 2*self.width + 2*self.length
        print(f"The perimeter of the rectangle is {Perimeter}")



class Triangle(Shape):
    
    def __init__(self, base, height, side):
        self.base = base
        self.height = height
        self.side = side
        
    def area(self):
        Area = 0.5*self.base*self.height
        print(f"The area of the triangle is {Area}")
        
    def perimeter(self):
        Perimeter = self.base + 2*self.side
        print(f"The perimeter of the triangle is {Perimeter}")
        
def main():
    circle = Circle(5)
    rectangle = Rectangle(2,4)
    triangle = Triangle(3,6,4)
    shapes = [circle, rectangle, triangle]
    
    for a in shapes:
        a.area()
        a.perimeter()
        
main()

        
        