# editor hc
# date: 2023/1/21 21:01
money = 8000.0
q = float(input("请输入取款金额:\n"))
if money>=q:
    money-=q
    print("取款成功，共取出",q,"元"+"剩余",money,"元")
else:print("余额不足")