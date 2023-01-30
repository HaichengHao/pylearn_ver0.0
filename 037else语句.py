# editor hc
# date: 2023/1/28 20:17
# else语句
'''
else的搭配
if ... :
    ...
else:
    ...

while ... :
    ...
else:
    ...

for ... :
    ...
else:
    ...
'''
# 下面这个文件操作只是为了回忆
# fp =open('D:/桌面/test3.txt','a+')
# print('第三次了，怕忘',file=fp)
# fp.close()

# 写法1
# for i in range(3):
#     pwd = input('请输入密码:\n')
#     if pwd == '6771':
#         print('欢迎登录')
#         break
#     else:
#         print('请重新输入，您还有'+str(2-i)+'次输入密码的机会')

# 写法2
i=0
while i<3:
    pwd = input('请输入密码：\n')
    if pwd =='1223':
        print('欢迎登陆')
        break
    else:
        print('密码输入错误，您还有'+str(2-i)+'次机会')
        i+=1
else:print('三次均错，已锁死')



