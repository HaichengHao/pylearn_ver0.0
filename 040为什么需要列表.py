# editor hc
# date: 2023/1/30 10:26
'''
关于列表的内容
1.列表的创建与删除
2.列表的查询操作
3.列表的增、删、改操作
4.列表元素的排序
5.列表推导式


为什么需要列表
~变量可以存储一个元素，而列表是一个大容器，可以存储多个元素
，程序可以方便地对这些数据进行整体操作
~列表相当于其它语言中的数组

'''

a=10
b=10
print(id(a),id(b))
# 2544559063568 2544559063568
# 变量存储的是一个对象的索引
lst = ['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)
print(lst[0])
''' 
1235820664320
<class 'list'>
['hello', 'world', 98]
hello
'''