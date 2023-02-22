# editor hc
# date: 2023/2/22 8:55
'''
with语句
·with语句可以自动管理上下文资源，不论什么原因跳出with块，
都能确保文件正确的关闭，以此来达到释放资源的目的
'''
with open('a.txt','r') as file:  #相当于file = open('a.txt'.'r')
    print(file.readlines())
#    with自动管理上下文，保证文件正确关闭，不用写.close()
