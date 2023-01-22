# editor hc
# date: 2023/1/21 20:49
"""
Python 一切皆对象，所有对象都有一个布尔值
获取对象的布尔值，可以使用内置函数bool
以下对象的布尔值皆为False
1.False
2.数值0
3.None
4.空字符串
5.空列表
6.空元组
7.空字典
8.空集合
"""
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(""))
print(bool([]))
#空列表也可写为print(bool(list[]))
print(bool(()))
#也可写为print(bool(tuple()))
print(bool({}))
#也可写为print(bool(dict()))
print(bool(set()))
print("-------除上面几种情况，其它的都为True-------")


