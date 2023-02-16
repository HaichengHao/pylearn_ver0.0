# editor hc
# date: 2023/2/15 15:50
'''
类的创建
语法
 class 类名:
    .....


类的组成
 -类属性
 -实例方法
 -静态方法
 -类方法

 在类之外定义的叫函数，在类之内定义的叫方法
'''
class Student:
    native_place='致远星'#类属性
    def __init__(self,name,age): #name,age为实例属性
        self.name=name
        self.age=age
    #实例方法
    def info(self):
        print('我叫:',self.name)
    #类方法
    @classmethod
    def cm(cls):
        print('类方法')
    #静态方法
    @staticmethod
    def sm():
        print('静态方法')