# editor hc
# date: 2023/1/28 20:36
# for i in range(1,10):
#     for j in range(1,10):
#         k=i*j
#         print( )
import math
# 打印一个三行四列的矩形
for i in range(1, 4):#行表，执行三次，一次一行
    for j in range(1, 5):#列表，执行四次，一次一列
        print('*',end='\t')  # 不换行输出
    print()#打行,()括号里什么都没有，其实起到的作用就是打印完换行,python中打印操作，若无附加操作，即为打印完自动换行
'''
*	*	*	*	
*	*	*	*	
*	*	*	*	
'''
# 关于第12行代码的深度剖析：

# 我们可以再打印一个三行四列的矩阵，不过这次我们将最后的print()改为print('一个路过的字符串')
for m in range(1,4):
    for n in range(1,5):
        print('*',end='\t')
    print('一个路过的字符串')
'''
*	*	*	*	一个路过的字符串
*	*	*	*	一个路过的字符串
*	*	*	*	一个路过的字符串

我们发现，最后的print()如果置空，那么其实结合python中的print语法，其实就是利用其打印完就换行的特点罢了'''


# 打印一个直角三角形
for q in range(1,10):#(1,10)--> 1-9,共九行
    for w in range(1,q+1):
        print('*',end='\t')

    print()

for e in range(1,10):#9行
    for r in range(1,e+1):#第一次循环从[1,2)中，也便只有1
        s=e*r
        print(str(r)+'*'+str(e)+'='+str(s),end='\t')
    #     也可写为print(r,'*',e,'=',r*e,end='\t')
    print()
