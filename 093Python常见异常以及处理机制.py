# editor hc
# date: 2023/2/15 14:55
'''
Python常见的几种异常类型
1.ZeroDivisionError
2.IndexError
3.KeyError
4.NameError
5.SyntaxError
6.ValueError
'''

'''
异常处理机制
    traceback模块打印异常信息
'''

import traceback
try:
    n1 = int(input('输入被除数:'))
    n2 = int(input('输入除数:'))
    n3=n1/n2
except:
    traceback.print_exc()
#     输入被除数:10
# 输入除数:0
# Traceback (most recent call last):
#   File "D:\pylearnV0.0\093Python常见异常以及处理机制.py", line 22, in <module>
#     n3=n1/n2
# ZeroDivisionError: division by zero


