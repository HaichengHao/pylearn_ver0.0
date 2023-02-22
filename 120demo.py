# editor hc
# date: 2023/2/22 8:50
file = open('d.txt','a+')
file.write('hello')
file.flush() #<--flush将文件从缓冲区刷写入磁盘
file.close()

# file.flush()
# ValueError: I/O operation on closed file. <-写完再刷，程序会报错