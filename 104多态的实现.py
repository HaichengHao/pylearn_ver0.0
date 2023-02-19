# editor hc
# date: 2023/2/19 9:19
'''
多态
    -简单的说就是“具有多种形态”，它指的是：即使不知道一个变量所引用的
    对象到底是什么类型，仍然可以通过这个变量调用方法，在运行的过程中根
    据变量所引用对象的类型，动态决定调用哪个对象中的方法

'''
class Animal(object): #Animal继承object类
    def eat(self):
        print('动物要吃东西')
class Dog(Animal): #Dog继承Animal
    def eat(self): #重写eat方法
        print('狗吃肉')
class Cat(Animal):#Cat继承Animal  dog和cat都是animal的子类
    def eat(self): #重写eat方法
        print('猫吃鱼')
class Human(object):
    def eat(self):
        print('人吃五谷杂粮')

# 定义一个函数
def fun(a):
    a.eat()

# 调用函数
fun(Dog())
fun(Cat())
fun(Human())
fun(Animal())

# 狗吃肉
# 猫吃鱼
# 人吃五谷杂粮
# 动物要吃东西
