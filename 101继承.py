# editor hc
# date: 2023/2/16 20:10
'''
继承
    语法格式:
        class 子类类名(父类1,父类2……):
            ....

    如果一个类没有继承任何类，则默认objecct
    Python支持多继承
    定义子类时，必须在其构造函数中调用父类的构造函数
'''
class Person(object): #Person继承了object
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name,self.age)) #格式化字符串

#定义子类
class Student(Person): #子类Student继承父类Person
    def __init__(self,name,age,stu_num):
        super().__init__(name,age)
        self.stu_num = stu_num
#测试
stu=Student('jack',20,'425')
stu.info()

class Teacher(Person):
    def __init__(self,name,age,yot):
        super().__init__(name,age)
        self.yot=yot