#字符串的比较操作
'''
字符串的比较操作
运算符: > ,, >= ,< , <= , == ,!=
比较规则：首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符
，依次比较下去，知道两个字符串中的字符不相等时，其比较结果就是两个字符串
的比较结果，两个字符串中的所有后续字符将不再比较

比较原理:两个字符串进行比较时，比较的是其oridinal value(原始值),调用
内置函数ord可以得到指定字符的oridinal value。与内置函数ord对应的是内置
函数chr,调用内置函数chr时指定oridianl value可以得到其对应的字符'''

s = 'hello,world'
s2 = 'hello,world'
print(s == s2)
# True

al1 = 'a'
al2 = 'b'
print(ord(al1))
# 97 ASCII的码位
print(ord(al2))
# 98

al1 = 'A'
al2 = 'b'
al3 = 'B'
print(ord(al1),ord(al2),ord(al3))
# 65 98 66

print(ord('好'))
# 22909
# 调用chr(初始值)可以将初始值转换为字符
print(chr(22909))
# 好
print(ord('张'),ord('王'))
# 24352 29579



'''
== 与 is 的区别
== 比较的是value
is 比较的是id是否相等'''
a=b='python'
c='python'
print(a==b)
print(b==c)
print(a is b)
print(a is c)
# True
# True
# True
# True
print(id(a),id(b),id(c))
# 1932694445168 1932694445168 1932694445168