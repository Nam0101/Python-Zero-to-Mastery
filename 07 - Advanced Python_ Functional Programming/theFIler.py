from functools import reduce


def only_Odd(item):
    return item % 2 != 0


my_list = [1, 2, 3, 4]
your_list = [10, 20, 30, 40]


def accumulator(acc, item):
    print(acc, item)
    return acc+item


print(reduce(accumulator, my_list, 0))
#print(list(filter(only_Odd, my_list)))
#print(list(zip(my_list, your_list)))
