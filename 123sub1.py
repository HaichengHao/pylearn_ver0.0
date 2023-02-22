# editor hc
# date: 2023/2/22 22:38
import os
path = os.getcwd()
lst_files = os.walk(path)
print(lst_files)
for dirpath,dirname,filename in lst_files:
    # print(dirpath)
    # print(dirname)
    # print(filename)
    # print('------------------')
    for dir in dirname:
        print(os.path.join(dirpath,dir))