#字符串的常用操作
'''
字符串的常用对齐方法
center() 居中对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度，则返回原字符串

ljust() 左对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度，则返回原字符串

rjust()右对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度，则返回原字符串

zfill() 右对齐，左边用0填充，该方法只接收一个参数，用于指定字符串的宽度，若指定的宽度小于等于字符串的长度，则返回字符串本身
'''
s = 'minkofox'
print(len(s))
# 8
print(s.center(5))
# minkofox  <--指定宽度小于等于实际宽度，则返回原字符串

print(s.center(12))  # <---指定宽度大于实际宽度，第二个参数未指定，则用空格
print(s.center(12,'~')) # <---置顶宽度大于实际宽度，第二个参数指定为'~'，用'~'填充
#   minkofox
# ~~minkofox~~
print(s.center(13,'~'))
# ~~~minkofox~~

print(s.ljust(10))
print(s.ljust(10,'*'))
# minkofox
# minkofox**

print(s.rjust(10))
print(s.rjust(10,'^'))
#   minkofox
# ^^minkofox

print(s.zfill(10))  #<--只能接收一个参数
# 00minkofox
print('-189'.zfill(8))
# -0000189   <---零填充到了负号之后
