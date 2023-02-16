# editor hc
# date: 2023/2/16 10:10
'''
类属性:类中方法外的变量称为类属性被该类的所有对象所共享
类方法：使用@classmethod修饰的方法，使用类名直接访问的方法
静态方法：使用@staticmethod修饰的方法，使用类名直接访问的方法
'''
class Student():
    native_place = '致远星' #类属性
    def __init__(self,name,age):  #实例属性
        self.name = name
        self.age = age

    #实例方法
    def eat(self):
        print(self.name,'在吃饭')
    def drink(self):
        print(self.name,'在喝水')
    def info(self):
        print('我叫',self.name,'我今年',self.age,'岁')

    @classmethod
    def cm(cls):
        print('这是类方法')
    @staticmethod
    def sm():  #静态方法无默认参数
        print('这是静态方法')


print(Student.native_place)#直接访问类属性
Student.cm()#调用类方法
Student.sm()#调用静态方法
# 致远星
# 这是类方法
# 这是静态方法

stu1 = Student('张三',20)
stu2 = Student('李四',20)
stu1.info()
stu2.info()
# 下面这种写法也可以
Student.info(stu1)
Student.info(stu2)
# 我叫 张三 我今年 20 岁
# 我叫 李四 我今年 20 岁
# 我叫 张三 我今年 20 岁
# 我叫 李四 我今年 20 岁

Student.native_place = '泽塔光环'
print(stu1.native_place)
print(stu2.native_place)
# 泽塔光环
# 泽塔光环