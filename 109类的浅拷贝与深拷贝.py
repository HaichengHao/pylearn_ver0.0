# editor hc
# date: 2023/2/20 15:36
'''
变量的赋值操作
    -只是形成两个变量，实际上还是指向同一个对象

浅拷贝
    ·Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，
    因此，源对象与拷贝对象会引用同一个子对象
深拷贝
    ·使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和
    拷贝对象所有的子对象也不相同
'''
class cpu:
    pass
class disk:
    pass
class computer:
    def __init__(self,cpu,disk): #初始化实例属性
        self.cpu =cpu
        self.disk =disk

#变量的赋值
cpu1 = cpu()
cpu2=cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))
# <__main__.cpu object at 0x000002211FDC0FD0> 2341291691984
# <__main__.cpu object at 0x000002211FDC0FD0> 2341291691984

# 类的浅拷贝
'''
浅拷贝
    ·Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，
    因此，源对象与拷贝对象会引用同一个子对象
    '''
print('---------------------------')
disk = disk() #创建一个disk类的对象
computer =computer(cpu1,disk) #创建一个计算机类对象

# 浅拷贝
import copy
computer2 = copy.copy(computer) #浅拷贝
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
# <__main__.computer object at 0x000001613B681E50> <__main__.cpu object at 0x000001613B681FD0> <__main__.disk object at 0x000001613B681F70>
# <__main__.computer object at 0x000001613B681D60> <__main__.cpu object at 0x000001613B681FD0> <__main__.disk object at 0x000001613B681F70>
# 可以发现子对象的内容的内存地址并未发生变化（.cpu和.disk)，源对象computer和拷贝对象computer2共用同一个子对象

print('---------------------------------')
# 深拷贝
'''
深拷贝
    ·使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和
    拷贝对象所有的子对象也不相同
    '''
computer3 = copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)
# <__main__.computer object at 0x0000020FB8641E50> <__main__.cpu object at 0x0000020FB8641FD0> <__main__.disk object at 0x0000020FB8641F70>
# <__main__.computer object at 0x0000020FB8641C70> <__main__.cpu object at 0x0000020FB8641970> <__main__.disk object at 0x0000020FB86419A0>
# 可以发现源对象和拷贝对象的所有子对象的内存地址都不相同，深拷贝实际是将源对象的值也拷贝一份，然后给到拷贝对象
