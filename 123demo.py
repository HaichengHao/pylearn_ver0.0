# editor hc
# date: 2023/2/22 22:28
# 获取当前目录下的所有.py文件
import os
path = os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)

