#字符串的大小写转换操作
'''
upper() ,所有字符转为大写
lower(),所有字符转为小写
swapcase(),大转小，小转大
capitalize(),第一个字符大写，其余小写
title(),每个字符的第一个字符转为大写，其余转为小写
'''

s = "hello,my name is steve"
s1 = 'KAMENRIDER BUILD'
s2 = 'HeLlO , wOrLd'
print(id(s))
print(s.upper())#小转大
# HELLO,MY NAME IS STEVE
print(s1.lower())#大转小
# kamenrider build

print(s2.swapcase()) #小转大大转小
# hElLo , WoRlD


print(s.capitalize())  #第一个字符大写，其余小写
# Hello,my name is steve
print(s.title())  #每个单词第一个首字母大写
