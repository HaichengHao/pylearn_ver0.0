# editor hc
# date: 2023/2/22 9:21
import os
print(os.getcwd())#<--输出当前的工作目录
# D:\pylearnV0.0
lst=os.listdir('package1')
print(lst)
# ['demo1.py', 'module1.py', 'module2.py', '__init__.py', '__pycache__']

# 也可以这样写
print(os.listdir('package1'))
# ['demo1.py', 'module1.py', 'module2.py', '__init__.py', '__pycache__']

# 创建目录
# os.mkdir('testdir')
# 创建多级目录
# os.mkdir('D:/pylearnV0.0/A/B/C')
# 删除目录
# os.rmdir('testdir')

# 改变工作目录路径
os.chdir('D:/pylearnV0.0/package1')
print(os.getcwd())
# D:\pylearnV0.0\package1 <--工作目录改变
# os.mkdir('demodir')
