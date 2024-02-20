import time
from typing import Callable, Any
import functools

def timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        runtime = time.time() - start
        print('Runtime:', runtime, 'seconds')
        return result  
      
    return wrapper

@timer
def squares_sum():
    """Squares sum documentation."""
    return sum(i**2 for i in range(10000))

@timer
def cubes_sum(n):
    return sum(i**3 for i in range(n))

my_squares_sum = squares_sum()
my_cubes_sum = cubes_sum(10000000)

# print(my_squares_sum)
# print(my_cubes_sum)

# print(squares_sum.__name__)
# print(squares_sum.__doc__)