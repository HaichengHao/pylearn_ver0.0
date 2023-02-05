#字典的创建
'''
常用方式:
score = {'张三':89,'李四':89}
使用内置函数dict()
dict(name = '张三',age='56')
'''
score = {'张三':89,'李四':78}
print(score)
# {'张三': 89, '李四': 78}

# ---使用内置函数---
student = dict(name = '王五',grade = 90)
print(student)
# {'name': '王五', 'grade': 90}

# ----创建空字典-----
xx = {}
print(xx)
# {}