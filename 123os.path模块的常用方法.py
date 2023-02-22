# editor hc
# date: 2023/2/22 15:50
'''
abspath(path) 用于获取文件或目录的绝对路径
exist(path) 用于判断文件或者目录是否存在，如果存在返回True,否则返回False
join(path,name) 将目录与目录或者文件名拼接起来
splitext()分离文件名与扩展名
basename(path) 从一个目录中提取文件名
dirname(path)从一个路径中提取文件路径，不包括文件名
isdir(path)用于判断是否为路径
'''
import os.path
print(os.path.abspath('123os.path模块的常用方法.py'))
# D:\pylearnV0.0\123os.path模块的常用方法.py
print(os.path.exists('123os.path模块的常用方法.py'),os.path.exists('121.py'))
# True False
print(os.path.join('package1','tst0.txt'))
# package1\tst0.txt
print(os.path.split('package1/demo1.py'))
# ('package1', 'demo1.py')
print(os.path.splitext('demo.txt'))
# ('demo', '.txt')
print(os.path.basename('package1\demo1.py'))
# package1\tst0.txt
print(os.path.dirname('D:\pylearnV0.0\package1\demo1.py'))
# D:\pylearnV0.0\package1
print(os.path.isdir('D:\pylearnV0.0\package1\demo1.py'))
# False <--路径的最后是一个demo1.py文件，不是目录
# 我们再来尝试
print(os.path.isdir('D:\pylearnV0.0'))
# True <--是目录，输出True