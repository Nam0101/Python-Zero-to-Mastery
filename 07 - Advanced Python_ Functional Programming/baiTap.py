my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'b', 'n', 'a']
my_list2 = list(set([char for char in my_list if my_list.count(char) > 1]))
print(my_list2)
