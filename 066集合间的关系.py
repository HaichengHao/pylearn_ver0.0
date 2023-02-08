#集合间的关系
'''
两个集合是否相等
    可以使用运算符==或！=进行判断
一个集合是否是另一个集合的子集
    可以使用issubset来判断
一个集合是否是另一个集合的超集
    可以使用issuperset来判断
两个集合是否有交集
    使用isjoint来判断
'''
set1 = {1,3,2,6,7,4,5}
set2 = {1,2,3,4,5,6,7,8,9}
print(set1 == set2)
# False
print(set1 != set2)
# True
print(set1.issubset(set2))
# True 集合1是集合2的子集
print(set2.issuperset(set1))
# True 集合2是集合1的超集

print(set1.isdisjoint(set2))
# False <--集合1和集合2有交集

set3 = {88,77,66,55}
print(set3.isdisjoint(set2))
# True