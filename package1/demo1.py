# editor hc
# date: 2023/2/21 10:27
import package1.module1 #导入package1包中的module1模块
import package1.module2 #导入package2包中的module2模块
print(package1.module1.a)
print(package1.module2.b)
# 10
# 100

# 也可以更方便一点，起别名
import package1 as pg1 #<--pg1是package1的别名
print(pg1.module1.a)
print(pg1.module2.b)
# 10
# 100

import package1
import cal
# 使用import方式进行导入时，其后只能跟包名或者模块名
from package1 import module1
from package1.module1 import  a
# 使用from···import···时可以导入模块，包，或者是函数，变量等。

