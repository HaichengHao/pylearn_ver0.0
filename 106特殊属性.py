'''
特殊方法和特殊属性
特殊属性
__dict__ 获得类对象或实例对象所绑定的所有属性和方法的字典
__class__查看实例对象所属的类
__bases__ 查看父类
__base__ 查看基类
__mro__ 查看一个类的层次结构
__subclasses__ 查看一个类的子类

'''
print(dir(object))
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age
x = C('jack',18) #x是C类型的实例对象
print(x.__dict__)#实例对象的属性字典
# {'name': 'jack', 'age': 18}
print(C.__dict__) #类对象
# {'__module__': '__main__', '__init__': <function C.__init__ at 0x0000029F32DEE1F0>, '__doc__': None}
print(x.__class__) #查看实例对象x所属的类

# <class '__main__.C'>  可以通过__class__方法来查看实例对象所属的类

print(C.__bases__) #C类的父类类型的元组
# (<class '__main__.A'>, <class '__main__.B'>) 可以看到C继承自A,B类
print(C.__base__)
# <class '__main__.A'> 离C类最近的父类-->可以这样记忆 ，class C(A,B)C离A近，所以用__base__方法是A，若写成class(B,A)则是B
print(C.__mro__) #输出C的类的层次结构
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(A.__subclasses__()) #查看A的子类
# [<class '__main__.C'>]
print(A.__mro__)