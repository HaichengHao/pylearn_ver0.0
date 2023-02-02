#列表元素的增加操作
'''
.append() 在列表的末尾添加一个元素
.extend() 在列表的末尾至少添加一个元素
.insert() 在列表的任意位置添加一个元素
切片  在列表的任意位置添加至少一个元素
'''
lst = ['hello','aloha','world',2023,2,2]
print(id(lst))
# 1885860451840
lst.append('min')
print(lst)
# ['hello', 'aloha', 'world', 2023, 2, 2, 'min']
lst.append(lst)
# ['hello', 'aloha', 'world', 2023, 2, 2, 'min', [...]]
print(lst)
# ['hello', 'aloha', 'world', 2023, 2, 2, 'min']
print(id(lst))
# 1885860451840
lst.extend('animal crossing')
print(lst)
# ['hello', 'aloha', 'world', 2023, 2, 2, 'min', 'a', 'n', 'i', 'm', 'a', 'l', ' ', 'c', 'r', 'o', 's', 's', 'i', 'n', 'g']

print(id(lst))
# 1885860451840
