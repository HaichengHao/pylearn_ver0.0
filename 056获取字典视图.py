#获取字典视图
'''
获取字典的三个方法
-keys()  -> 获取字典所有key
-values() -> 获取字典所有value
-items() ->获取字典键值对
'''
scores = {'张三':54,'李四':89,'王五':90}
print(scores.keys())
print(scores.values())
print(scores.items())
# dict_keys(['张三', '李四', '王五'])
# dict_values([54, 89, 90])
# dict_items([('张三', 54), ('李四', 89), ('王五', 90)])