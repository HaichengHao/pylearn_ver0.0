# editor hc
# date: 2023/1/3 17:10
from decimal import Decimal
a = 3.14159
print(a,type(a))
a1 = 1.1
a2 = 2.2
print(a1+a2)
#3.3000000000000003,we find the answer is not '3.3'，进行浮点运算需要导入模块
#引入decimal,‘from decimal import Deciaml'并且在运算数前运用decimal语句
print(Decimal('1.1')+Decimal('2.2'))
#3.3结果正确