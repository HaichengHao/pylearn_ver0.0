# editor hc
# date: 2023/1/23 20:09
"""
从键盘录入两个整数，比较两个整数的大小
"""
a = int(input("请输入第一个数:\n"))
b = int(input("请输入第二个数:\n"))
# if a > b:
#     print(a,'>',b)
# elif a == b:
#     print(a,'=',b)
# else:print(a,'<',b)

'''简写，使用条件表达式'''
"""格式：
X if 判断句A else Y"""
print(str(a)+'>='+str(b) if a>=b else str(a)+'<'+str(b))
