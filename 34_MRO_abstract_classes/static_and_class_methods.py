class Cat:
    CALLS = 0
    
    def __init__(self, legs):
        self.legs = legs
        self.has_a_tail = True
    
    # @staticmethod
    # def sound():
    #     return 'Meow!'
    
    @classmethod
    def sound(cls):
        cls.CALLS += 1
        print(cls.CALLS)
        return 'Meow!'
    
# cat = Cat(4)
# print(cat.sound())
# print(cat.sound())
# print(cat.sound())
# print(cat.sound())
# print(cat.sound())


from dataclasses import dataclass

@dataclass
class Coordinates:
    x: float
    y: int
    
    
obj = Coordinates(1, 2)
print(obj.y)