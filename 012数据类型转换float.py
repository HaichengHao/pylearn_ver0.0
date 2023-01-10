# editor hc
# date: 2023/1/10 15:24
#将其它数据类型转换为浮点型
s1='12.8'
s2='76'
s3='hello'
ff=True
i=98
print(type(s2),type(s2),type(s3),type(ff),type(i))
#print(float(s1),float(s2),float(s3),float(ff),float(i))
"""Traceback (most recent call last):
  File "D:\pylearnV0.0\012数据类型转换float.py", line 10, in <module>
    print(float(s1),float(s2),float(s3),float(ff),float(i))
ValueError: could not convert string to float: 'hello'
"""
#可以发现，转化为float类型和转化为int类型一样，不能转化非数字类型的字符串
#这次我们不转化s3,查看是否会报错
print(float(s1),float(s2),float(ff),float(i))
"""<class 'str'> <class 'str'> <class 'str'> <class 'bool'> <class 'int'>
12.8 76.0 1.0 98.0<--可以发现没错了"""