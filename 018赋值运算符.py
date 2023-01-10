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