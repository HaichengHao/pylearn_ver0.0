# editor hc
# date: 2023/1/30 11:23
'''
列表的查询操作
1.获取列表中指定元素的索引
.index()
如果列表中存在n个相同元素，只返回相同元素中的第一个元素的索引
如果查询的元素再列表中不存在，则会抛出ValueError
还可以在指定的start和stop之间进行查找
'''
lst = ['hello', 'world', 98, 'hello']
print(lst.index('hello'))
# 0  当列表中有n个相同的元素，只把相同元素第一个元素的索引返回
#  print(lst.index('python'))
# ValueError: 'python' is not in list  显然字符串'python'并不在列表当中
print(lst.index('hello',0,2))
print(lst.index('hello',1,4))
print(lst.index(98,0,4))
'''
0
3
2
'''

# ----------------

"""
2.获取列表中的单个元素
正向索引从0到N-1  举例lst[0]
逆向索引从-N到-1  举例lst[-N]
指定索引不存在，抛出IndexError
"""

print(len(lst))
# 4
print(lst[0])
# hello
print(lst[-4])
# hello
# print(lst[4])
# IndexError: list index out of range
