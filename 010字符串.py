# editor hc
# date: 2023/1/3 17:21
str1 = 'life is short , you need python'
str2 = " life is short ,you need python"
str3 = """life is short , 
you need python"""
str4 = '''life is short , 
you need python'''
#三引号可以将字符串分行写
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))
#字符串索引
str5='hello world'
print(str5[4])
print(str5[5])#第五个是空格
print(str5[-1])
print(str5[-11])
"""
o
 
d
h
"""
#字符串切片
# 语法结构 字符串或字符变量[N:M]
#切片获取字符串从N到M（不包含M）的字符串
print(str5[0:3])
"""hel"""

length = len(str5)
print(length)
s4 = 'HELLOWORLD'
ll=len(s4)
print(ll)
print(s4[0:])
print(s4[-8:-1])
print(s4[:10])
