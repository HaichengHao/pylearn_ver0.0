#coding=gbk
# editor hc
# date: 2023/2/21 21:10

'''
编码格式的介绍
文件的读写原理
文件读写操作
文件对象的常用的方法
with语句（上下文管理器）
目录操作
'''
print('hello China')
'''
python默认的编码格式为UTF-8
'''
#如何修改编码格式？只需在文件开始写 '#coding = 编码格式' 或者'#coding:编码格式'
s = '海内存知己'
print(s.encode(encoding='GBK'))
# b'\xba\xa3\xc4\xda\xb4\xe6\xd6\xaa\xbc\xba'
bytes =  b'\xba\xa3\xc4\xda\xb4\xe6\xd6\xaa\xbc\xba'
print(bytes.decode(encoding='GBK'))
# 海内存知己
