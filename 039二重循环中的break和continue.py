# editor hc
# date: 2023/1/29 20:54
# 二重循环中的break和continue
for i in range(5):#代表外循环要执行5次--> 0，1，2，3，4
    for j in range(1,11):
        if j%2==0:
            # break
            continue
        print(j)