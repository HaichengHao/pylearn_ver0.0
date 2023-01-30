# editor hc
# date: 2023/1/30 21:49
'''
获取列表中的多个元素
语法格式
  列表名[start:stop:step]
'''
lst = ['你好','hello','aloha',2023]
lst2 = [1,2,3,4,5,6,7,8,9]
print(len(lst))
# 4
print(lst[0:1])
# ['你好']
print(lst[0:2])
# ['你好', 'hello']
print(lst[0:4])
# ['你好', 'hello', 'aloha', 2023]
print(lst2[0:9:2])
# [1, 3, 5, 7, 9]

