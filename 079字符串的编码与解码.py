#字符串的编码与解码

'''
编码与解码
编码 ：字符串 -->二进制数据
解码 ：二进制数据 --> 字符串
'''
s='天涯共此时'
print(s.encode(encoding='GBK'))  #编码，在GBK这种编码格式中，一个中文占2个字节
print(s.encode(encoding='UTF-8')) #在utf-8这种编辑格式中，一个中文占三个字节
# b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'
# b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6' < --确实比GBK多出5个字节

# 解码
bytes = b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'
print(bytes.decode(encoding='GBK'))
# 天涯共此时

s2 = '你好'
print(s2.encode(encoding='GBK'))
print(s2.encode(encoding='UTF-8'))
# b'\xc4\xe3\xba\xc3'
# b'\xe4\xbd\xa0\xe5\xa5\xbd'

bytes = b'\xc4\xe3\xba\xc3'
print(bytes.decode(encoding='GBK'))
# 你好
bytes = b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(bytes.decode(encoding = 'UTF-8'))
# 你好



'''  
字符串相关内容的总结
查询的方法 index(),rindex(),find(),rfind()
大小写转换 upper() ,lower(),swapcase(),capital(),title()
内容对齐 center(),rjust(),ljust(),zfill()
字符串劈分 split(sep,maxsplit)  rsplit(sep,maxsplit)
字符串的判断 isidentifer() isdecimal() isnumeric() isalpha() isspace() isalnum()
字符串的替换 replace(old,new,count)
字符串的合并 join()
字符串的比较 > < >= <= == !=
格式化字符串 '%宽度.精度' % 值   {0:宽度.精度}.format(值)
字符串编码解码 s.encode(encoding ='' )  解码 byte.decode(encoding ='')
 '''

