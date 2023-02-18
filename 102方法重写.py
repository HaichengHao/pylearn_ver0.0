# editor hc
# date: 2023/2/17 20:36
'''
方法重写
如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其进行重新编写
子类重写后的方法可以通过super().xxx()调用父类中被重写的方法
'''
class Person(object):
    def __init__(self,name,age): #定义类属性
        self.name = name
        self.age = age
    def info(self):#定义方法
        print('姓名:{0},年龄:{1}'.format(self.name,self.age))#这样用格式化字符串来写纯粹是为了回忆

#定义子类
class Student(Person): #子类Student继承Person
    def __init__(self,name,age,stunumber):
        super().__init__(name,age)
        self.stunumber=stunumber
    def info(self):   #重写Python中的方法
        super().info() #方法重写后调用方法
        print('学号:{0}'.format(self.stunumber))
class Teacher(Person):
    def __init__(self,name,age,yot):
        super().__init__(name,age)
        self.yot=yot
    def  info(self): #重写Person中的info方法
        super().info() #方法重写后调用方法
        print('教龄:{0}'.format(self.yot))

#开始测试
stu1 = Student('jack',20,456)
techer1 = Teacher('aymi',43,10)
stu1.info()
techer1.info()
# 姓名:jack,年龄:20
# 学号:456  <--方法重写成功了，多了学号这个属性
# 姓名:aymi,年龄:43
# 教龄:10 <--教龄也出现，重写info()方法成功