from time import time
# testing time by decorator


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'It took about {t2-t1} seconds to run this program')
        return result
    return wrapper


@performance
def calculate():
    for i in range(0, 1000):
        i*i


calculate()

# Performance-Decorator
# https://repl.it/@aneagoie/decorators

# Exercise-Repl
# https://repl.it/@aneagoie/decorators2-exercise

# Solution-Repl
# https://repl.it/@aneagoie/decorators-1
