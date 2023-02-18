# editor hc
# date: 2023/2/16 16:13
'''
1.封装
2.继承
3.方法重写
4.object类
5.多态
6.特殊方法和特殊属性

面向对象的三大特征
封装：提高程序的安全性
    -将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，
    在类对象的外部调用方法。这样，无需关心方法内部的实现细节，从而隔离了复杂度。
    -在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部
    被访问，前面使用两个下划线'__'
继承
    提高代码的复用性
多态
    提高程序可扩展性和可维护性
'''
class Car:
    def __init__(self,brand,type):
        self.brand =brand
        self.type = type
    def info(self):
        print(self.brand,'类型',self.type)

car1 = Car('兰博基尼雷文顿','超跑')
car2 = Car('长城','SUV')
Car.info(car1)
Car.info(car2)
# 兰博基尼雷文顿 类型 超跑
# 长城 类型 SUV

# 在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前面使用两个下划线'__'
# eg
class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age  #<---这里我们将实例属性age设置成不被外部访问的形式
    def show(self):
        print(self.name,self.__age) #<--可以在内部被使用
stu = Student('张三',20)
stu.show()
# 张三 20


# 在类的外部使用name和age
print(stu.name)
# 张三


# print(stu.__age)
# AttributeError: 'Student' object has no attribute '__age'
# 在外部不能被直接使用，but
print(dir(stu))
# ['_Student__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'show']
#   我们看到了上面的_Student__age,所以
print(stu._Student__age)
# 20 <--被获取到了，在类的外部可以通过'_类名__实例属性'来访问