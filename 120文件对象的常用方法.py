# editor hc
# date: 2023/2/22 7:55
'''
文件对象的常用方法
read([size]) 从文件中读取size个字节或字符的内容返回。若省略[size]，
则读取到文件末尾，即一次读取文件所有内容
readline()从文本文件中读取一行内容
readlines()把文本文件中每一行都作为独立的字符串对象，并讲这些对象放入列表返回。
write(str)将字符串str内容写入文件
writelines(s_list)将字符串列表s_list写入文本文件，不添加换行符
seek(offset[,whence])
    把文件指针移动到新的位置，
    offset表示相对于whence的位置
    offset:为正往结束方向移动，

tell()返回文件指针的当前位置
flush()把缓冲区的内容写入文件，但不关闭文件
close()把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关资源

'''
#
# file  = open('D:/pylearnV0.0/118demo.txt','')
# print(file.read(2)) #<--读取两个字符
# print(file.readline())#<--读取一行内容
# print(file.readlines())#<--每一行都作为独立的字符串对象，并将这些对象放入列表返回
# file.close()

# file2 = open('D:/pylearnV0.0/b.txt','a')
# # file2.write('hello') #<--写入str
# lst = ['hello','python']
# file2.writelines(lst) #<--将字符串列表lst写入文件，不添加换行符
# file2.close()

file = open('a.txt','r')
print(file.read())
# hello
file.seek(2)
print(file.read())
# llo <--文件内容为hello ,指针移动两位，跳过了'he',所以读取了'llo'
# 若文件中有中文，但是seek()内的参数写了1，就会报错，因为一个汉字两个字节
print(file.tell()) #<--返回文件指针位置
# 5 #<--在文件末尾，因为’hello'刚好五个字节

file.close()