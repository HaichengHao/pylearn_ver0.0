#变量的作用域
'''
变量的作用域
    -程序的代码能访问该变量的区域
    -根据变量的有效范围可分为
        1.局部变量
            -在函数内定义并使用的变量，只在函数内部有效，局部变量使用global声明，
            这个变量就会成为全局变量
        2.全局变量
            -函数体外定义的变量，可作用于函数内外
    '''

def fun(a,b):
    c = a+b #c,就称为局部变量，因为c是在函数体内定义的变量，a,b为函数的形参，作用范围也是函数内部，相当于局部变量
    print(c)

# print(c)
# print(a)
#上面输出a,c都会报错，因为a,c超出了起作用的范围

name = 'kk'
print(name)
# kk

def fun2():
    print(name)

fun2()
# kk

def fun3():
    global age  #将age设置为全局变量
    age=20
    print(age)

# 调用函数fun3
fun3()
# 20
print(age)
# 20