# editor hc
# date: 2023/2/22 9:08
with open('dog.png','rb') as src_file: #<--打开dog.png作为源文件
    with open('copydog.png','wb') as target_file: #<--创建copydog.png作为目标文件
        target_file.write(src_file.read()) #<--目标文件调用写方法，写入源文件调用读方法读取的内容