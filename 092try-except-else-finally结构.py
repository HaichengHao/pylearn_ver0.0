# editor hc
# date: 2023/2/15 14:18
'''
try…except…else结构
如果try块中没有抛出异常，则执行else块，如果try中抛出异常，则执行except块
'''

'''for i in range(100):
    try:
     n1 = int(input('请输入被除数:'))
     n2 = int(input('请输入除数:'))
     result = n1/n2
    except BaseException as e:
        print('出错了')
        print(e)
    else:
        print('结果为:',result)'''


'''
try - except -else -finally 结构
finally块无论是否发生异常都会被执行，常用来释放try中申请的资源
'''
try:
    num1 = int(input('请输入被除数:'))
    num2 = int(input('请输入除数:'))
    num3 = num1/num2
except BaseException as e:
    print('出错了')
    print(e)
else:
    print(num3)
finally:
    print('无论是否发生异常，finally块都会被执行')
    print('结束了')
'''
请输入被除数:6
请输入除数:6
1.0
无论是否发生异常，finally块都会被执行
结束了'''