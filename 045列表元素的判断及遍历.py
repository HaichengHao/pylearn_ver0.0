# editor hc
# date: 2023/1/31 13:02

# 列表元素的查询操作
'''
元素 in 列表名
元素 not in 列表名
'''

# 列表元素的遍历
'''
for 迭代变量 in 列表名:
    操作
'''

# 判断指定元素再列表中是否存在
lst = ['你好','aloha','bonjour',2023]
print('你好' in lst)
print('aloha' not in lst)
# True
# False

# 列表元素的遍历
print(len(lst))
for i in range(len(lst)):
    print(lst[i])
# 另一种写法
for j in lst:
    print(j)