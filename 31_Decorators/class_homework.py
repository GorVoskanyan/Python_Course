class Triangle:
    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def is_valid(self):
        if (self.first_side + self.second_side > self.third_side
                and self.first_side + self.third_side > self.second_side
                and self.third_side + self.second_side > self.first_side):
            return True
        return False


a, b, c = map(float, input("Write down the three sides of the triangle: a, b, c ").split(","))

triangle = Triangle(a, b, c)
result = triangle.is_valid()
print(result)
