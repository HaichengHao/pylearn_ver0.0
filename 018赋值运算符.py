# editor hc
# date: 2023/1/10 16:14
a=3+4
print(a)
print(id(a))
b=4
print(b)
b+=3
print(b,id(b))
n1=n2=n3=7
print(id(n1),id(n2),id(n3))
n1+=2
print(id(n1))
'''
7
2382014185904
4
7 2382014185904
2382014185904 2382014185904 2382014185904
2382014185968
'''
x=40
x-=20
print(x)
x/=10
print(x)
x%=2
print(x)
y=3
y**=2
print(y)
m=8
m//=2
print(m)
n=9
n//=2
print(n)
#Python支持链式赋值
a=b=c=100#相当于执行了给a,b,c分别赋值
print(a,b,c)
#Python支持系列解包赋值
a,b,c=10,20,30
print(a,b,c)
#10 20 30
#系列解包赋值支持值的交换
a,b=10,20
print("a=,b=",a,b)
a,b=b,a
print("a=,b=",a,b)
"""
a=,b= 10 20
a=,b= 20 10

"""
