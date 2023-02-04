#列表元素的增加操作
'''
.append() 在列表的末尾添加一个元素
.extend() 在列表的末尾至少添加一个元素
.insert() 在列表的任意位置添加一个元素
切片  在列表的任意位置添加至少一个元素
'''
# lst = ['hello','aloha','world',2023,2,2]
# lst2 = ['playstation']
# print(id(lst))
# # 1885860451840
# lst.append('min')
# print(lst)
# # ['hello', 'aloha', 'world', 2023, 2, 2, 'min']
# lst.append(lst)
# # ['hello', 'aloha', 'world', 2023, 2, 2, 'min', [...]]
# print(lst)
# # ['hello', 'aloha', 'world', 2023, 2, 2, 'min']
# print(id(lst))
# # 1885860451840
# lst.extend('animal crossing')
# print(lst)
# # ['hello', 'aloha', 'world', 2023, 2, 2, 'min', 'a', 'n', 'i', 'm', 'a', 'l', ' ', 'c', 'r', 'o', 's', 's', 'i', 'n', 'g']
#
# print(id(lst))
# # 1885860451840
#
#
# lst.extend(lst2)
# print(lst)
# # ['hello', 'aloha', 'world', 2023, 2, 2, 'min', [...], 'a', 'n', 'i', 'm', 'a', 'l', ' ', 'c', 'r', 'o', 's', 's', 'i', 'n', 'g', 'playstation']


# 以下为正常内容
# 在列表末尾添加一个元素
lst = [10,20,30]
print('添加元素之前:',lst,id(lst))
lst.append(40)
print('添加元素之后:',lst,id(lst))
'''
添加元素之前: [10, 20, 30] 2944442029568
添加元素之后: [10, 20, 30, 40] 2944442029568
'''



# 在列表末尾一次性添加多个元素
lst2 = ['hello','world']
lst.extend(lst2)
print(lst)
# [10, 20, 30, 40, 'hello', 'world']

# 在任意位置上添加一个元素
lst.insert(0,5)
print(lst)
# [5, 10, 20, 30, 40, 'hello', 'world']


# 列表切片
lst3 = [True,False,'hello']
lst[1:]=lst3#从lst的序号1（也就是第二个元素，包含第二个元素）开始切掉，将其替换为lst3
print(lst)
# [5, True, False, 'hello']
