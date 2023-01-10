# editor hc
# date: 2023/1/3 17:30
name='张三'
age=20
print(type(name),type(age))
#<class 'str'> <class 'int'>类型不同
'''p rint('我叫'+name+'今年'+age+'岁')'''
#TypeError: can only concatenate str (not "int") to str
#这样写会报错，因为它们并不是同一类型
#修正方式
print('我叫'+name+'今年'+str(age)+'岁')
#我叫张三今年20岁  运行正常，↑↑↑只是在age这个整形前面加了’str()‘
a = 10
b =19.8
c = False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))
'''
<class 'int'> <class 'float'> <class 'bool'>
10 19.8 False <class 'str'> <class 'str'> <class 'str'>
类型转换成功

'''
s1  = '128'
f1 = 98.7
s2 ='76.77'
ff = True
s3 = 'hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))#将str类型转为int类型，字符串为数字串
print(int(f1),type(int(f1)))#将float类型转换为int类型，但是会进行截取整数部分，舍去小数部分
#print(int(s2),type(int(s2)))#这样会报错，在将str类型转化为int时报错，因为字符串中有小数
#将字符串转化成int类型时，字符串必须时数字串，且不能含小数