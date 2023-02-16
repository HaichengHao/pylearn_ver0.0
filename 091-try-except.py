# editor hc
# date: 2023/2/15 10:26
'''
bug的常见类型
    -被动掉坑问题的解决方案
    -python提供了异常处理机制，可以在异常出现时及时捕获，然后内部’消化‘
    ，让程序继续运行'''
'''try:
    n1 = int(input('请输入一个整数:'))
    n2 = int(input('请输入另一整数:'))
    result = n1/n2
    print('相除结果为:',result)
except ZeroDivisionError:
    print('除数不能为零哦')'''


'''
请输入一个整数:5
请输入另一整数:0
除数不能为零哦
'''

# 多个except结构
'''捕获异常的顺序按照先子类后父类的顺序，为了避免遗漏
可能出现的异常，可以在最后增加BaseException
'''

try:
    num1 = int(input('请输入被除数:'))
    num2 = int(input('请输入除数:'))
    num3 = num1/num2
    print('相除结果为:',num3)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('不能将字符串转换为数字')
except BaseException as e:
    print(e)