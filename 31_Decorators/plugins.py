from typing import Dict, Callable

PLUGINS: Dict[str, Callable] = dict()

def register(func: Callable) -> None:
    PLUGINS[func.__name__] = func
    
@register
def f1(): pass

def f2(): pass

@register
def f3(): pass

print(PLUGINS)