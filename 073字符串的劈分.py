#字符串的劈分
'''
split()
-从字符串的左边开始劈分，默认的劈分符是空格字符串
返回的只都是一个列表
-以通过参数sep指定劈分字符串的劈分符
-通过参数maxsplit指定劈分字符串时的最大劈分次数在经过最大次劈分后，剩余的子串会单独作为一部分

rsplit()
-从字符串的右边开始劈分，默认的劈分符是空格字符串
返回的只都是一个列表
-以通过参数sep指定劈分字符串的劈分符
-通过参数maxsplit指定劈分字符串时的最大劈分次数在经过最大次劈分后，剩余的子串会单独作为一部分


'''

s = 'hello world python'
lst = s.split()
print(lst)
# ['hello', 'world', 'python']
s1 = 'hello|world|python'
print(s1.split())
# ['hello|world|python']

s2 = 'hello | github'
print(s2.split(sep='|'))
# ['hello ', ' github']

s3 = 'hello|world|2023'
print(s3.split(sep='|',maxsplit=1))
# ['hello', 'world|2023']

print(s3.rsplit(sep='|',maxsplit=1))
# ['hello|world', '2023']
