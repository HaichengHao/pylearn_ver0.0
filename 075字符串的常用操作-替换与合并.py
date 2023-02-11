#字符串的替换与合并
'''
替换
    -replace(old,new,count) ，第一次参数指定被替换的子串，第二个参数指定替换子串的字符串，
该方法返回替换后得到的字符串，替换前的字符串不发生变化，调用该方法时可以通过第三个参数指定最大
替换次数。

合并
    -join()将列表或元组中的字符串合并成一个字符串

'''

s='hello,world,2023'
print(id(s))
s.replace('world','minkofox')
print(s,id(s))
# 2498746812256
# hello,world,2023 2498746812256
'''发现输出后并未变化，这说明replace()方法产生了一个新的字符串，我们需要一个新变量来接收这个新的字符串'''
# 第一种输出方式
s1 = 'hello,world,2023'
s1 = s1.replace('world','minkofox')
print(s1)
# hello,minkofox,2023

# 第二种输出方式
print(s1.replace('hello','HELLO'))
# HELLO,minkofox,2023


s2 = 'hello,hello,bonjour,aloha,hello'
print(s2.replace('hello','~',1))
# ~,hello,bonjour,aloha,hello
print(s2.replace('hello','~',2))
# ~,~,bonjour,aloha,hello


# 合并
lst = ['hello','world','python']
print('|'.join(lst))
# hello|world|python
print(''.join(lst))
# helloworldpython
print('*'.join('hello'))
# h*e*l*l*o
