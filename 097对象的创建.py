# editor hc
# date: 2023/2/16 9:10
'''
对象的创建又称为类的实例化
语法：
    实例名 = 类名()
eg:
    #创建Student类的对象
    stu=Student('jack',20)
    print(stu.name) #实例属性
    print(stu.age) #实例属性
    stu.info()      #实例方法
意义：有了实例，就可以调用类中的内容
'''
class Student:
    native_place='致远星'#类属性
    def __init__(self,name,age): #name,age为实例属性
        self.name=name
        self.age=age
    #实例方法
    def info(self):
        print('我叫:',self.name)
        print('我',self.age,'岁')

    def eat(self):
        print(self.name,'在吃饭')

    def drink(self):
        print(self.name,'在喝水')
    #类方法
    @classmethod
    def cm(cls):
        print('类方法')
    #静态方法
    @staticmethod
    def sm():
        print('静态方法')

#创建Student类的对象
stu=Student('jack',20)
print(stu.name) #实例属性
print(stu.age) #实例属性
stu.info()      #实例方法
stu.eat()
# 也可以这样写 Student.eat(stu)
stu.drink()
# jack
# 20
# 我叫: jack
# 我 20 岁
# jack 在吃饭
# jack 在喝水
