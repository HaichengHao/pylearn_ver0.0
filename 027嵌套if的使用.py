# editor hc
# date: 2023/1/22 21:15
"""
嵌套if的语法结构
if 条件表达式1:
    if 内层条件表达式:
          内层条件执行体1
    else:
        内层条件执行体2
else:
    条件执行体
"""
m = float(input("请输入您的消费金额:\n"))
q = input("您是会员吗? yes/no\n")#外层对会员身份进行判断
if q == 'yes':
    if m >= 200.0:
        print("打八折，折扣后仅需",m*0.8)
    else:
        print("打九折，折扣后只需",m*0.9)
else: print("打九五折，折扣后只需",m*0.95)
