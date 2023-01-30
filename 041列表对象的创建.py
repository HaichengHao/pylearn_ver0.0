# editor hc
# date: 2023/1/30 10:37
# 列表的创建
'''
列表使用中括号[]，元素之间使用英文的逗号进行分隔
        lst = ['汪淼','史强']
        ^   ^
        |   |
列表对象名   赋值号

列表的创建方式
1,使用中括号
2,使用内置函数list()
eg:
ls = ['aloha','bonjour']
ls = list(['aloha','bonjour'])
'''
lst1 = ['你好','hello','bonjour',2023]
lst2 = list(['你好','hello','bonjour',2023])
print(id(lst1)==id(lst2)) #False
print(id(lst1))
print(id(lst2))
# 2006983759360
# 2006984023168