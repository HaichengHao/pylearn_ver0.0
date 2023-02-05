# 字典元素的遍历
scores = {'张三':54,'李四':89,'王五':90}
for item in scores:
#     print(item)
#     # 张三
#     # 李四
#     # 王五
    #print(item,scores[item])
# 张三 54
# 李四 89
# 王五 90

    print(item,scores.get(item))
# 张三 54
# 李四 89
# 王五 90