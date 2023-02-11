#字符串的切片操作
'''
字符串是不可变类型
    -不具备增删改等操作
    -切片操作会产生新的对象
'''
s1 = 'hello,aloha'
s2 = s1.split(sep=',')  #<---劈分操作
print(s2)
# ['hello', 'aloha']
print('|'.join(s2))  #<--合并操作
# hello|aloha


# 切片操作  [strat:stop:step]
str = 'hello,python'
str1 = str[:5]
str2 = str[6:]
str3 = '!'
newstr = str1+str2+str3
print(str)
print(str1)
print(str2)
print(str3)
print(newstr)
print(id(str),id(str1),id(str2),id(str3),id(newstr))
# ['hello', 'aloha']
# hello|aloha
# hello,python
# hello
# python
# !
# hellopython!
# 2324940817968 2324945686192 2324945365680 2324945362544 2324945362800

print(str[::2])
# hlopto
print(str[::-1])#默认从字符串的最后一个元素开始，到字符串的第一个元素结束，因为步长为负数
# nohtyp,olleh
print(str[-6::1]) #
# python