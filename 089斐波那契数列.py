#斐波那契数列
'''
使用递归来计算阶乘
斐波那契 1，1,2,3,5,8…… 从第三项开始，每一项均是前两项之和

'''

def fiber(n):
    if n <=2:
        return 1
    else:
        return fiber(n-1)+fiber(n-2)
print(fiber(6))
# 8

# 下面尝试输出前六位数字,输成列表样式，好看
lst=[]
for i in range(1,7):
    tmp = fiber(i)
    lst.append(tmp)
print(lst)
# [1, 1, 2, 3, 5, 8]