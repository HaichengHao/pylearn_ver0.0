#列表元素的排序操作

'''
常见的两种方法
    -调用sort()方法，列中所有的元素默认按照从小到大的顺序排序，可以指定
 reverse = True ,进行降序（从大到小）排序
    -调用内置函数sorted(),可以指定reverse=True,进行降序排序，原列表不发生改变
'''
lst = [10,20,40,50,30]
lst.sort()
print(lst)
# [10, 20, 30, 40, 50]
lst.sort(reverse=True)
print(lst)
# [50, 40, 30, 20, 10]


# ---sorted()----,增加新元素
lst2 = [20,39,201,29]
print(lst2)
# [20, 39, 201, 29]
newlst = sorted(lst2)
print(newlst)
# [20, 29, 39, 201]

nnlst = sorted(lst2,reverse=True)
print(lst2)
# [20, 39, 201, 29]
print(nnlst)
# [201, 39, 29, 20]
