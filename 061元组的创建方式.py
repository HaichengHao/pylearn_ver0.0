#元组的创建方式
'''
1.直接小括号
eg: t = ('hello','python')
2.使用内置函数tuple()
eg: t = tuple(('hello','python'))
3.只包含一个元组的元素需要使用小括号和逗号
eg: t =(10, )
'''

# 1
t = ('hello','python',2023)
print(type(t),id(t))
# 2
t2 = tuple(('hello','python',2023))
print(type(t2),id(t2))
# 运行结果
# <class 'tuple'> 2069990477056
# <class 'tuple'> 2069990477056

t3 = (1,)
print(type(t3))
# <class 'tuple'>  类型也是元组类型

# 空元组
t5 = ()
# t5 = tuple()
print(t5,type(t5))
# () <class 'tuple'>
# 空字典
d = {}
# d = dict()
print(d,type(d))
# {} <class 'dict'>
# 空列表
li = []
# li = list()
print(li,type(li))
# [] <class 'list'>

