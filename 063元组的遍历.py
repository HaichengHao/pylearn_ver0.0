#元组的遍历
'''
元组是可迭代对象,所以可以使用for .. in..进行遍历
eg:
    t = tuple(('Python','Hello',2023))
    for item in t:
        print(item)
'''
t = tuple(('Python', 'Hello', 2023))
for item in t:
    print(item)
# Python
# Hello
# 2023

# 还有一种笨方法,数字遍历,但要注意长度,不然会出错,这种方法很鸡肋,但也可以用巧妙办法
# for j in range(0,len(t)+1):
#     print(t[j])
#    print(t[j])
# IndexError: tuple index out of range <--超出范围,报错,错就错在len(t+1)

print(len(t))
for j in range(0,len(t)):
    print(t[j])
'''
3
Python
Hello
2023
'''