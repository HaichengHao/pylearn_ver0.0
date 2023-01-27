# editor hc
# date: 2023/1/27 16:34
"""输出100-999之间的水仙花数
水仙花数：eg:153=3*3*3+5*5*5+1*1*1"""
# 输出100-999之间的水仙花数
import math
for i in range(100, 1000):
    gw = i % 100 % 10
    sw = i % 100 //10
    bw = i//100
    m = gw*gw*gw+sw*sw*sw+bw*bw*bw
    if i == m:
        print(i)
"""
153
370
371
407
"""
# 另一种写法举例
a=789
print(a%10)
print(a//10%10)
print(a//100)


for i2 in range(100,1000):
    ge = i2 % 10
    shi = i2 // 10 % 10
    bai = i2 // 100
    if i2 == pow(ge,3) + pow(shi,3) +pow(bai,3):#ge*ge*ge+shi*shi*shi+bai*bai*bai ,ge**3+shi**3+bai**3
        print(i2)
