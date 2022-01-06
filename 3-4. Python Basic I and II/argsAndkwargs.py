# *args and **kwargs
def supper_sum_func(name, *args, i='hi', **kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    return total + sum(args)


print(supper_sum_func('Andy', 1, 2, 3, 4, 5, 6, num1=5, num2=10))
