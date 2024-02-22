from functools import wraps
from typing import Callable, Any


def counter(func: Callable) -> Any:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(wrapper.count)
        return result

    wrapper.count = 0
    return wrapper


@counter
def test(): pass


#
# test()
# test()
# test()

# class MyClass:
#     pass
#
# obj = MyClass()
#
# obj.name= 'Alex'
# obj.age = 25
#
# print(obj.name)


def my_cache(func: Callable) -> Any:

    cache = dict()

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        if args not in cache:

            result = func(*args, **kwargs)
            cache[args] = result
            return result
        else:
            return cache[args]

    return wrapper


@my_cache
def fibonacci(n: int): return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(50)
print(result)
