#字典元素的增删改操作
'''
-key的判断
 - in 指定的key在字典中有时就返回True
 - not in 指定的key在字典中不存在返回True

-字典元素的删除
    del scores['张三']
-字典元素的新增
    scores['jack'] = 89
'''
scores = {'张三':90,'李四':89}
print('张三' in scores)
# True
print('王五' not in scores)
# True

del scores['张三']
print(scores)
# {'李四': 89}

scores['王五']=99
print(scores)
# {'李四': 89, '王五': 99}

# 字典元素的修改
scores['李四']=98
print(scores)
# {'李四': 98, '王五': 99}