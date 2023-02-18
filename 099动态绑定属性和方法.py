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





def show(): #定义在类之外的，是函数，不是方法
    print('我是一个函数，我定义在类之外')

stu1 = Student('Jack',20)
stu2 =Student('Bob',21)
stu1.gender='男' #动态绑定性别,stu1加个性别

print(stu1.name,stu1.age,stu1.gender)
stu1.show=show #动态绑定方法
stu1.show()
# 我是一个函数，我定义在类之外

# stu2.show()
# AttributeError: 'Student' object has no attribute 'show'
# 为啥报错呢，因为show并不是类之内的方法，而是一个单独的函数，所以需要先动态绑定
stu2.show = show #动态绑定
stu2.show()
# 我是一个函数，我定义在类之外
