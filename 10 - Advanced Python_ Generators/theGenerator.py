# Generator

from time import time
# def my_generator(num):
#     for i in range(num):
#         yield i

# print(my_generator(100))


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'It took about {t2-t1} seconds to run this program')
        return result
    return wrapper


@performance
def test1():
    for i in range(100000000):
        i*i


@performance
def test2():
    for i in list(range(100000000)):
        i*i


test1()
test2()
