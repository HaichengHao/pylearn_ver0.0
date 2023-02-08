#元组
'''
元组是python的内置数据结构之一，是一个不可变序列

不可变序列与可变序列
    不可变序列:字符串，元组
        -不可变序列:没有增删改查操作
    可变序列:列表、字典
        -可变序列:可以对序列进行增删改操作，对象地址不发生改变

'''
lst = ['hello',98]
print(lst,id(lst))
lst.append(88)
print(lst,id(lst))
lst.remove(98)
print(lst,id(lst))
lst[1:3] = [99,33]
print(lst,id(lst))
# ['hello', 98] 2436217558528
# ['hello', 98, 88] 2436217558528
# ['hello', 88] 2436217558528
# ['hello', 99, 33] 2436217558528
dic1 = {'name': 'jack', 'age':19}
print(dic1,id(dic1))
dic1['sex'] = 'male'
print(dic1,id(dic1))
del dic1['name']
print(dic1,id(dic1))
dic1['age']=18
print(dic1,id(dic1))
# {'name': 'jack', 'age': 19} 2242679629440
# {'name': 'jack', 'age': 19, 'sex': 'male'} 2242679629440
# {'age': 19, 'sex': 'male'} 2242679629440
# {'age': 18, 'sex': 'male'} 2242679629440


# 字符串不可变序列
s='hello'
print(id(s))
s=s+'world'
print(id(s))
# 1432569275888
# 1432569309424
# 发生了变化

# 元组
'''
t = ('hello','world',2023)'''