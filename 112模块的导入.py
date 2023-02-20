# editor hc
# date: 2023/2/20 17:08
'''
自定义模块
    ·新建一个.py文件，名称尽量不要和Python自带的标准模块重名
导入模块
    - import 模块名称 as 别名
    - from 模块名称 import 函数/变量/类
'''

import math
print(id(math))
print(type(math))
print(math)
# 2474610395312
# <class 'module'>
# <module 'math' (built-in)>

print(math.pi)
print(math.pow(2,3))
# 3.141592653589793
# 8.0
print(math.ceil(9.001)) #天花板，往上升
# 10
print(math.floor(9.999))#地板，往下
# 9
