from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return __import__('math').pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return (self.base * self.height) / 2
    
# obj = Shape() # Dont use

circle = Circle(3)
rectangle = Rectangle(3, 4)
triangle = Triangle(5, 2)

area_of_circle = circle.area()
area_of_rectangle = rectangle.area()
area_of_triangle = triangle.area()

print(area_of_circle)
print(area_of_rectangle)
print(area_of_triangle)
