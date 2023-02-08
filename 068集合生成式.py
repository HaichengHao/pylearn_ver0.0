#字典生成式
'''
与列表生成式只是外围括号不同
[i for i in range(1,10)]
{i for i in range(1,10)}
'''

set1 = {i for i in range(1,10)}
print(set1)
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

set2 = {j*2 for j in range(1,5)}
print(set2)