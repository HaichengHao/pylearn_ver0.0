# 函数调用，位置实参和关键字实参

# 位置实参
def multi(q,w): #q,w为形式参数
    e = q*w
    return e
print(multi(2,3)) #2,3为实际参数
# 6

# 关键字实参
def div(a,b):
    c = a/b
    return c

print(div(50,5))
print(div(b = 50,a=5))  #关键字实参中，根据形参名称进行参数传递
# 10.0
# 0.1


