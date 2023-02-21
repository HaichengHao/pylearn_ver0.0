# editor hc
# date: 2023/2/21 7:53
# 在此文件中导入自定义的模块
import cal
# from cal import add,div,multi,minus 也可以这样写来导入
a=int(input('请输入数字a:'))
b=int(input('请输入数字b:'))
print('a+b=',cal.add(a,b))
print('a-b=',cal.minus(a,b))
print('a*b=',cal.multi(a,b))
print('a/b=',cal.div(a,b))