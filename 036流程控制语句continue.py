# editor hc
# date: 2023/1/27 21:03
# continue语句，用于结束当前循环，进入下一次循环，通常与分支结构if一起使用
"""
语法示例
for ... in ... :
    ......
    if ...:
        continue

--------------------

while 条件:
   ......
   if ...:
       continue
"""
# 要求输入1-50之间所有5的倍数
for i in range(1,51):
    if i%5==0:
        print(i)
# 用continue
for i1 in  range(1,51):
    if i1%5!=0:
        continue
    else:
        print(i1)
"""
5
10
15
20
25
30
35
40
45
50
5
10
15
20
25
30
35
40
45
50
"""