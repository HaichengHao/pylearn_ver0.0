# editor hc
# date: 2023/1/27 20:46
# break语句，用于结束循环结构，通常与分支结构if一起使用
"""
语法示例
for ... in ... :
    ......
    if ...:
        break

--------------------

while 条件:
   ......
   if ...:
        break
"""
# 从键盘录入密码，最多录入三次，如果正确就结束循环
for i in range(3):
    pwd = input("请输入密码:\n")
    if pwd =='88888':
        print("欢迎登录！")
        break#密码正确，跳出循环
    else:
        a=2-i
        print("密码错误，请重新输入，您还有"+str(a)+"次机会")