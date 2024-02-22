import functools
import time
from datetime import datetime
from typing import Callable


# ZADACHA 1
# def how_are_you(func: Callable):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         text = "Inchka chka???"
#         patasxan = 'Lav chi eli lav chi. Lav de, gorct ara'
#         input(f'{text} >> ')
#         print(patasxan)
#         result = func(*args, **kwargs)
#         return result
#     return wrapper

# @how_are_you
# def zrozro(n):
#     for i in range(n):
#         print(f'{i+1}: {i*n}')
#
# zrozro(5)

# def func(start, stop, evens_sum, odds_sum):
#     if start == stop:
#         return evens_sum, odds_sum
#
#     if start % 2 == 0:
#         return func(start+1, stop, evens_sum + start, odds_sum)
#     else:
#         return func(start + 1, stop, evens_sum, odds_sum + start)

# evens, odds = func(start=1, stop=10, evens_sum=0, odds_sum=0)
# print(f"Evens: {evens}\nOdds: {odds}")

# ZADACHA 2
# def pause_5(func):
#     '''Pause code execution 5 seconds'''
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         time.sleep(5)
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
#
# @pause_5
# def printxxx(n):
#     for i in range(n):
#         print(f'{i+1}: aaaaaaaaaaa')
#
# print('Code ruuuuuns after 5 seconds...')
# printxxx(40000)
# print('DONE')


# ZADACHA 3
def logging(func):
    '''Pause code execution 5 seconds'''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            file = open('error.log', 'w')
            log_x = f'Time - {datetime.now()}, Error name - {e}\n'
            file.write(log_x)
            file.close()
    return wrapper

@logging
def ankapfunction(n):
    if n > 5:
        print(n * 5)
    else:
        print(n / 0)

ankapfunction(1)