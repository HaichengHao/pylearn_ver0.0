#字典元素的获取
scores={'张三':89,'李四':98}
# 获取张三的成绩
# 第一种方式
print(scores['张三'])
# 89

# 第二种方式
print(scores.get('张三'))
# 89


'''上面两种方法中
[]取值法，如果字典中不存在指定的key,抛出keyError
get方法中，如果字典中不存在指定的key,并不会抛出keyError而是返回None,
可以通过参数设置默认的Value，以便指定的key不存在时返回'''
# print(scores['王五'])
# KeyError: '王五'

print(scores.get('王五'))
# None

# 另一种情况
print(scores.get('赵六',99))
# 99 <--‘赵六’不存在时提供的默认值