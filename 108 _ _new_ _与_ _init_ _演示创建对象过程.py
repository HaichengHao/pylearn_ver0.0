# editor hc
# date: 2023/2/19 22:54
'''
__new__()用于创建对象
__init__()对创建的对象进行初始化
'''

class Person():
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的id为:{}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        print('__init__被调用了，self的id值为:{}'.format(id(self)))
        self.name = name
        self.age = age
print('object这个类对象的id为{}'.format(id(object)))
print('Person这个类对象的id为{}'.format(id(Person)))

p1 = Person('张三',20)
print('p1这个Person类的实例对象的id为：'.format(id(p1)))

# object这个类对象的id为140717854608896
# Person这个类对象的id为2676588131984
# __new__被调用执行了，cls的id值为2676588131984
# 创建的对象的id为:2676589268752
# __init__被调用了，self的id值为:2676589268752
# p1这个Person类的实例对象的id为：