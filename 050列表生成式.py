lst = [i for i in range(1,10)]
lst2 = list(range(1,10))
print(lst)
print(lst2)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

lst3 = [j*j for j in range(1,10)]
print(lst3)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

'''列表中的元素的值为2，4，6，8，10'''
lst4 = [u*2 for u in range(1,11)]
print(lst4)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lst5 = [o*2 for o in range(1,6)]
print(lst5)
# [2, 4, 6, 8, 10]