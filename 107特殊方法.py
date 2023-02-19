'''
特殊方法
__len__()通过__len__()方法，让内置函数len()的参数可以是自定义类型
__add__()通过重写__add__()方法，可以用自定义对象具有“+”功能
__new__()用于创建对象
__init__()对创建的对象进行初始化
'''
s1 = 'qwertyuiop'
q = s1.__len__()
print(q)
# 10





a=20
b=100
c=a+b #两个整数类型对象的相加操作
# 底层操作其实是这样的
c = a.__add__(b)
print(c)

class Student:
    def __init__(self,name):
        self.name = name
    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)
    # 实现了两个对象的加法运算
stu1 = Student('jack')
stu2 = Student('Aimy')
s = stu1+stu2
print(s)
# jackAimy

# print(len(stu1))
# TypeError: object of type 'Student' has no len() stu作为一个实例对象，它并没有len()方法，但我们可以在类中定义

# 再次尝试
print(len(stu1))
# 4 'jack'长度为4，结果正确
