my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = list(map(lambda x: x**2, my_list))
print(new_list)


a = [(1, 2), (4, 4), (10, -1), (41, 3)]
a.sort(key=lambda x: x[1])
print(a)
