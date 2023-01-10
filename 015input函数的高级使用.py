# editor hc
# date: 2023/1/10 15:48
from decimal import Decimal
n1=float(input("请输入长方形的长\n"))
n2=float(input("请输入长方形的款\n"))
s=(Decimal(n1)*Decimal(n2))
print("长方形的面积为:\n","%.2f"%s)
