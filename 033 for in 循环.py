# editor hc
# date: 2023/1/26 19:31
"""
for in 循环
 in 表达从（字符串、序列等）中依次取值，又称遍历
 for in 遍历的对象必须是可迭代对象
for in 的语法结构
 for 自定义的变量 in 可迭代对象
    循环体

"""

for item in 'HELLO':
    print(item)
for i in range(0,10):
    print(i)

# 如果在循环体中不需要使用自定义变量，可以将自变量写为”_“
for _ in  range(5):
    print("life is short ,we need Python")
"""
结果:
life is short ,we need Python
life is short ,we need Python
life is short ,we need Python
life is short ,we need Python
life is short ,we need Python
"""
# 使用for in 循环来计算1-100之间偶数的累加和
sum = 0
for i in range(1,101):
    if i%2==0:
        print(i)#打印出1-100所有偶数
        sum+=i
print(sum)
