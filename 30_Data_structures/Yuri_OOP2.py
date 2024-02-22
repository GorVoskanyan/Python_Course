''' Exercice 2 - Karma '''
# from random import randint, choice

# class LifeError(Exception):
#     def __str__(self) -> str:
#         return super().__str__() + '\n'

# class KillError(LifeError): 
#     def __init__(self, msg = 'Kill Error') -> None:
#         super().__init__(msg)

# class DrunkError(LifeError): 
#     def __init__(self, msg = 'Drunk Error') -> None:
#         super().__init__(msg)

# class CarCrashError(LifeError): 
#     def __init__(self, msg = 'Car Crush Error') -> None:
#         super().__init__(msg)

# class GluttonyError(LifeError): 
#     def __init__(self, msg = 'Gluttony Error') -> None:
#         super().__init__(msg)

# class DepressionError(LifeError): 
#     def __init__(self, msg = 'Depression Error') -> None:
#         super().__init__(msg)


# def oneday():
#     error_list = LifeError.__subclasses__()
#     if randint(1, 10) == 10:
#         raise choice(error_list)
#     return randint(1, 7)


# def start_game():
#     karma = 0
#     day_count = 0
#     file = open('karma.log', 'w')
#     while karma < 500:
#         try:
#             karma += oneday()
#             day_count += 1
#         except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as error:
#             file.write(f'Day {day_count} - {str(error)}')
#             day_count += 1
#     file.close()

#     print(f'Karma program ended in {day_count} days. You are now Budda')


# if __name__ == '__main__':
#     start_game()
    


''' Exercice 3 - MyDict '''
# class MyDict(dict):
    # def get(self, key):
    #     if key in self:
    #         return super().get(key)
    #     return 'O'
    # def get(self, key, default='O'):
    #     return self[key] if key in self else default
# dicti = {
#     1: 'value1',
#     2: 'value2',
#     3: 'value3'
# }
# mydict = MyDict({key: value for key, value in dicti.items()})

# print(mydict.get(5))

