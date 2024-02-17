class Property:
    def __init__(self, worth) -> None:
        self.worth = worth

    def calculate(self):
        if isinstance(self, Apartment):
            return self.worth / 1000
        elif isinstance(self, Car):
            return self.worth / 200
        elif isinstance(self, Countryhouse):
            return self.worth / 500
    
class Apartment(Property):
    def __init__(self, worth) -> None:
        super().__init__(worth)

class Car(Property):
    def __init__(self, worth) -> None:
        super().__init__(worth)

class Countryhouse(Property):
    def __init__(self, worth) -> None:
        super().__init__(worth)


poxer = int(input('How much money you have? '))
tesak = int(input('What are you going to buy?\n 1. Apartment\n 2. Car\n 3. Countryhouse\n >> '))
guyqigin = int(input(f'How much is this? '))

if tesak == 1:
    x = Apartment(guyqigin)
elif tesak == 2:
    x = Car(guyqigin)
elif tesak == 3:
    x = Countryhouse(guyqigin)

hark = x.calculate()

print(f'You have money: {poxer}$\nYou need to pay tax: {hark}$')
if poxer < hark: print(f'You have to add another {hark - poxer}$ to pay tax {hark}')