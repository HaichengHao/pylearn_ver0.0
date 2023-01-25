# editor hc
# date: 2023/1/24 20:58
"""
range函数
创建range对象的三种方式
range(stop)-->创建一个[0,stop)之间的整数序列，步长为1
range(start,stop)-->创建一个[start,stop)之间的整数序列，步长为1
range(start,stop,step)-->创建一个[start,stop)之间的整数序列，步长为step
返回值是一个迭代器对象
range类型的优点：不管range对象表示的整数序列有多长，所有range对象占用的内存
空间是相同的，因为仅仅需要存储start,stop
"""

# range()第一种创建方式，只有一个参数(小括号中只给了一个数)
r=range(10)
print(r)#range(0, 10)，并没有展示出数列
print(list(r))#用于查看range对象中的整数序列 -->list是列表的意思-->[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 第二种创建方式，有两个参数，一个为起始值，一个为结束值（但是不包含结束值，左闭右开）
r1=range(1,10)#[1,10),开始为1，结尾为9
print(list(r1))#[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(10 in r)#结果为False,说明确实是左闭右开，不包含10

# 第三种创建方式，三个参数，一个起始值，一个结束值，一个步长
r2=range(1,10,2)
print(list(r2))#[1, 3, 5, 7, 9]
