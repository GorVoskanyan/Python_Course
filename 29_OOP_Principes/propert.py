# property

class Property:
    def __init__(self, worth):
        self.worth = worth
        
    def calculate_tax(self):
        pass

class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def calculate_tax(self):
        return self.worth / 1000

class Car(Property):
    def __init__(self, worth):
       super().__init__(worth)
       
    def calculate_tax(self):
        return self.worth / 200

class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def calculate_tax(self):
        return self.worth / 500

