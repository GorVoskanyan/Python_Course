import time
from typing import Callable, Any

def timer(func: Callable, *args, **kwargs) -> Any:
    start = time.time()
    result = func(*args, **kwargs)
    runtime = time.time() - start
    print('Runtime:', runtime, 'seconds')
    return result    
    
def squares_sum():
    return sum(i**2 for i in range(10000))

def cubes_sum(n):
    return sum(i**3 for i in range(n))

# my_squares_sum = squares_sum()
# my_cubes_sum = cubes_sum()


my_squares_sum = timer(squares_sum)
my_cubes_sum = timer(cubes_sum, 100000)

# print(my_squares_sum)
# print(my_cubes_sum)


# def f(*args, **kwargs):
#     print(args)
#     print(kwargs)
    
    
# f(1,2,3,4, a=5, b=6)