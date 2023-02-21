# editor hc
# date: 2023/2/21 17:25
'''
第三方模块的安装
pip install 模块名
第三方模块的使用
import 模块名
'''
import time
print(time.localtime(time.time()))
import schedule
def job():
    print('哈哈--------')
schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)