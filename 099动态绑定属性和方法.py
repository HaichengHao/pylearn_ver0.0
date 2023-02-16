# editor hc
# date: 2023/2/16 11:08
'''
Python是动态语言，在创建对象之后，可以动态的绑定属性和方法
'''
class Student():
    private_place = '致远星'
    def __init__(self,name,age):
        self.name=name
        self.age = age
    def info(self):
        print('我叫',self.name,'年龄',self.age)





def show():
    print('我是一个函数')
stu = Student('Jack',20)
stu.gender='男' #动态绑定性别
print(stu.name,stu.age,stu.gender)
stu.show=show #动态绑定方法
stu.show()