# editor hc
# date: 2022/12/29 13:40
'''python 输出函数 print'''
#输出字符串,必须加引号
print("hi i just wanna leran python")
#输出数字
print(520)
#含有运算符的表达式,会直接输出结果
print(5+1)
#输出到文件中,没有则创建，有则继续追加
fp=open('D:/桌面/pylearn.txt','a+')
print("helloworld",file=fp)
fp.close()

#不进行换行输出
print('hello','world','Python')
