# editor hc
# date: 2023/2/21 21:40
'''
文件的读写原理
·文件的读写俗称io操作
内置函数open()创建文件对象
语法规则： file = open(filename[mode,encoding])

'''
fp = open('D:/pylearnV0.0/118demo.txt','a+')
# 也可以这样写
# fp = open('D:/pylearnV0.0/118demo.txt',mode='a+',encoding='UTF-8')
# print('China',file=fp)
print(fp.readlines())
fp.close()