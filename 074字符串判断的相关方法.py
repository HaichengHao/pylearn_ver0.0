#字符串判断的相关方法
'''
isidentifer() ,判断指定的字符串是否全为合法的标识符
isspace() ,判断指定的字符串是否全由空白字符组成（回车，换行，水平制表符）
isalpha(),判断指定的字符串是否全由字母组成
isnumeric(),判断指定的字符串是否全由数字组成
isalnum(),判断指定的字符串是否由字母和数字组成
'''

s = 'hello world 2023'
s1 = '123,4,'
s2 = '    '
s3 = '12,223'
s4 = 'abcdefg'
print(s.isalpha())
# False
print(s1.isidentifier())
# False <--s1 不是合法的标识符，合法的标识符为字母数字下划线 ,且不能以数字开头
print(s2.isspace())
# True
print(s3.isdecimal())
# False
print(s3.isnumeric())
# False
print(s4.isalpha())
# True

print(s.isalnum())
# False

str = 'ab12_'
str0='12ab_'  #< -- 不是合法标识符
str1='_ab12'
str2='      '
str3='abcdefghijklmn'
str4='123'
str5='1233445514523'
str6 = '12a34f'
print(str.isidentifier())
print(str0.isidentifier())
print(str1.isidentifier())
print(str2.isspace())
print(str3.isalpha())
print(str4.isdecimal())
print(str5.isnumeric())
print(str6.isalnum())
# True
# False
# True
# True
# True
# True
# True
# True

str7='\t' #<--水平制表符
print(str7.isspace())
# True

str8 = '一二三四'
print(str8.isnumeric())
# True
str9 = 'ⅠⅡⅢⅣⅨⅩ'
print(str9.isnumeric())
# True