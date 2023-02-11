#字符串的查询操作
'''
index() 查找substr第一次出现的位置，如果查找的子串不存在，抛出ValueError
rindex() 查找substr最后一次出现的位置，如果查找的子串不存在，抛出ValueError
find()查找substr第一次出现的位置，如果查找的子串不存在，返回-1
rfind()查找substr最后一次出现的位置，如果查找的子串不存在，返回-1
'''
s = 'hello,hello'
print(s.index('lo'))
# 3
print(s.find('lo'))
# 3
print(s.rindex('lo'))
# 9
print(s.rfind('lo'))
# 9

# print(s.index('world'))
# ValueError: substring not found
# print(s.rindex('world'))
# ValueError: substring not found

print(s.find('world'))
# -1
print(s.rfind('world'))
# -1

print(len(s))
# 11


