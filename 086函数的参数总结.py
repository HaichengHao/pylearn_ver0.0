def fun(a,b,c): #a,b,c在函数的定义处，所以是形式参数
    print('a',a)
    print('b',b)
    print('c',c)

fun(10,20,30) #函数调用时的参数传递，称为位置传参
# a 10
# b 20
# c 30


lst=[11,22,33]
# fun(lst)
# TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
# 需要三个参数，但只传了俩

# 解决办法
fun(*lst) #在函数调用时，将列表中的每个元素都转换为位置实参传入
# a 11
# b 22
# c 33


fun(a=100,c=200,b=300) #关键字实参，函数会根据关键字来执行参数的操作
# a 100
# b 300
# c 200

dic = {'a':111,'b':222,'c':333}
# fun(dic)
# TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
# 还是像上面的一样的错误，缺失参数

# 解决办法，把字典里的键值对转换为关键字实参
fun(**dic)
# a 111
# b 222
# c 333


def f1(a,b=10):#b是在函数的定义处，所以b是形参，而且进行了赋值，所以b称为默认形参
    print('a',a)
    print('b',b)

f1(10)
# a 10
# b 10
f1(20,30)

# a 20
# b 30

def f2(*args): #个数可变的位置形参
    print(args)

def f3(**args2): #个数可变的关键字形参
    print(args2)

f2(10,20,30)
# (10, 20, 30)  个数可变的位置形参，结果为数组

f3(a=11,b=2,c=4)
# {'a': 11, 'b': 2, 'c': 4} 个数可变的关键字形参，结果为字典

def f4(a,b,*,c,d):  #从*之后的参数，只能采用关键字传递
    print('a',a)
    print('b',b)
    print('c',c)
    print('d',d)


# f4(10,20,30,40)   #上边函数定义时我们已经定义了，*之后只能采用关键字传递
# TypeError: f4() takes 2 positional arguments but 4 were given
f4(a=10,b=20,c=30,d=40)
f4(10,20,c=30,d=40)


# 函数定义时的形参的顺序问题
def f5(a,b,*,c,d,**args):
    pass

def f6(*a,**b):
    pass
def f7(a,b=10,*args,**args2):
    print(a,b,args,args2)

a1=10
a2=20
a3=[10,20,30]
a4={'a':2,'b':5}
f7(a1,a2,a3,a4)
# 10 20 ([10, 20, 30], {'a': 2, 'b': 5}) {}