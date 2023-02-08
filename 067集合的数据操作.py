s1 = {10,20,30,40,50}
s2 = {20,30,40,50,60}
print(s1.intersection(s2))#s1和s2的交集
# {40, 50, 20, 30}
print(s1 & s2)
# {40, 50, 20, 30}

print(s1.union(s2))#s1和s2的并集
# {40, 10, 50, 20, 60, 30}
print(s1|s2)
# {40, 10, 50, 20, 60, 30}


print(s1.difference(s2))#s1和s2的差集，s1并s2 - s2
# {10}
print(s1 - s2)
# {10}

print(s2.difference(s1))#s2和s1的差集，s1并s2 - s1
# {60}
print(s2 - s1)
# {60}

print(s1.symmetric_difference(s2)) #s1和s2的对称差集，也就是A并B - A交B
# {10, 60}
print((s1|s2)-(s1&s2))
# {10, 60}