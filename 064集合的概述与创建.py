#什么是集合
'''
集合
 python语言提供的内置数据结构
 与列表,字典一样都属于可变类型的序列
 集合是没有value的字典
'''
# 集合的创建方式
s = {1,2,3,4,5,6}
q = {2,3,4,6,90}
print(s&q)
# {2, 3, 4, 6}  交集
print(s | q)
# {1, 2, 3, 4, 5, 6, 90} 并集

w = {1,22,3,3,4,3,44,5,5}
print(w)
# {1, 3, 4, 5, 22, 44} <--集合中的元素不允许重复

# 第二种创建方式
s1 = set(range(6))
print(s1)
# {0, 1, 2, 3, 4, 5}
s2 = set([1,4,1,5,56,4,3])
print(s2)
# {1, 3, 4, 5, 56} <--集合中的元素是无序的
s3 = set((1,4,5,2,4,1,2))
print(s3)
# {1, 2, 4, 5} <--集合无序
s4 = set('python')
print(s4)
# {'h', 'p', 'o', 'n', 'y', 't'}

# 定义空集合
s5=set()
s6={}
print(s5,type(s5))
print(s6,type(s6))
# set() <class 'set'>
# {} <class 'dict'>    <--发现这是字典了,也是应了开篇,集合就是没有值的字典,所以智能用set()去定义一个空集合