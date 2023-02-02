# editor hc
# date: 2023/1/30 21:49
'''
获取列表中的多个元素
语法格式
  列表名[start:stop:step]

切片的结果 ->原列表片段的拷贝
切片的范围 -> [start,stop] ->左闭右开，包含start,不包含stop
step默认为1 -> 简写为[start:stop]
step为正数（从start开始往后计算切片）
- [:stop:step] ->切片的第一个元素默认是列表的第一个元素
- [start::step] ->切片的最后一个元素默认是列表的最后一个元素

step为负数(从start往前计算切片)
-[:stop:step] ->切片的第一个元素默认是列表的最后一个元素
-[start::step] ->切片的最后一个元素默认是列表的第一个元素
'''
lst = ['你好','hello','aloha',2023]
lst2 = [1,2,3,4,5,6,7,8,9]
print(len(lst))
# 4

# ----step默认为1 -> 简写为[start:stop]
print(lst[0:1])
# ['你好']
print(lst[0:2])
# ['你好', 'hello']
print(lst[0:4])
# ['你好', 'hello', 'aloha', 2023]

# ----step为正数（从start开始往后计算切片）
print(lst2[:9:2])#- [:stop:step] ->切片的第一个元素默认是列表的第一个元素
# [1, 3, 5, 7, 9]
print(lst2[0::2])#- [start::step] ->切片的最后一个元素默认是列表的最后一个元素
# [1, 3, 5, 7, 9]

# step为负数(从start往前计算切片)
print(lst2[::-1])
# [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(lst2[6:0:-2])
# [7, 5, 3]
print(lst2[8::-1])
# [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(lst2[:-10:-2])
print(lst2[-1::-2])
# [9, 7, 5, 3, 1]
# [9, 7, 5, 3, 1]
