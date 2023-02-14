#函数的返回值
'''
函数返回多个值时，结果为元组
'''
def fun(num):
    odd = [] #偶数列表
    even = [] #奇数列表
    for i in num:
        if i%2==0:  #这一点也可写为i%2: 因为i%2，例如，若i=2,2%2=0,对象的布尔值为False
            odd.append(i)
        else:  #布尔值为True,则为奇数，其实这里的逻辑判断还是用的对象的布尔值
            even.append(i)
    return odd , even

    # ---写法2----
   ## print('偶数',odd)
    ## print('奇数',even)
print(fun([i for i in range(10,21)]))
# ([10, 12, 14, 16, 18, 20], [11, 13, 15, 17, 19])  多个返回值，结果是元组



# # 写法2
# fun([i for i in range(10,21)]) #判断10 - 20 之间的奇数和偶数
# # 偶数 [10, 12, 14, 16, 18, 20]
# # 奇数 [11, 13, 15, 17, 19]


def fun1():
    print('hello')
fun1()
# hello

def fun2():
    return 'hello'
res = fun2()
print(res)
# hello

def fun3():
    return 'hello','world'

print(fun3())
# ('hello', 'world')


# 函数在定义时，是否需要返回值，视情况而定。

