# editor hc
# date: 2023/1/19 21:30
# eval()函数
"""eval(s)函数将去掉字符串s最外侧的引号，并按照Python语句方式执行去掉引号后的字符串
语法格式
  变量=eval(字符串)
  eval函数经常和input函数来使用，用来获得用户输入的信息"""
s='3.14+3'
print(s,type(s))
x=eval(s)
print(x,type(x))
"""
3.14+3 <class 'str'>
6.140000000000001 <class 'float'>---eval将外围引号去掉，进行了加法运算
"""

age=eval(input("请输入您的年龄:\n"))
print(age,type(age))
if age >18 & age==18:
    print("您成年了")
else:
    print("您是未成年")
