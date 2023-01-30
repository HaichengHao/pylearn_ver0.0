# editor hc
# date: 2023/1/30 10:55
'''
列表的特点
1,列表元素按顺序有序排序
2,索引映射唯一一个数据
3,列表可以存储重复数据
4,任意数据类型混存
5,根据需要动态分配和回收内存
'''
lst = ['你好','hello','world','世界']
print(len(lst))
print(lst[0])
print(lst[-1])
print(lst[-4])
print(lst[3])
'''
4
你好
世界
你好
世界
'''

# 列表可以存储重复数据
lst2 = ['hello','hello','hello']
print(id(lst2[0]))
print(id(lst2[1]))
# 1861913044208
# 1861913044208
# 列表可以混存
lst3 = ['hello',89,789.2]
print(lst3)
# ['hello', 89, 789.2]