#字典生成式
items = ['fruits','books','others']
price = [44,32,45]
price2 = [90,392,2,2,4,52,1]
# 内置函数zip()
'''
用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组
然后返回由这些元组组成的列表
'''
lst = zip(items,price)
print(list(lst))
# [('fruits', 44), ('books', 32), ('others', 45)]

dic2 = {items : price for items,price in zip(items,price)}
print(dic2)
# {'fruits': 44, 'books': 32, 'others': 45}

# 对比实验 price2中的元素明显多
dic3 = {items : price2 for items,price2 in zip(items,price2)}
print(dic3)
# {'fruits': 90, 'books': 392, 'others': 2}发现只按长度来匹配了键值对