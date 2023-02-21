# editor hc
# date: 2023/2/21 13:08
'''
sys 与Python解释器及其环境操作相关的标准库
time 提供与时间相关的各种函数的标准库
os 提供了访问操作系统服务功能的标准库
calendar 提供与日期相关的各种函数的标准库
urllib 用于读取来自网上（服务器）的数据标准库
json 用于使用Jason序列化和反序列化对象
re 用于在字符串中执行正则表达式匹配和替换
math 提供标准算数运算函数的标准库
decimal 用于进行精确控制运算精度，有效数位和四舍五入操作的十进制运算
logging 提供了灵活的记录事件，错误，警告和调试信息等日志信息的功能
'''
import sys
import time
import os
import urllib.request
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
# 28
# 28
# 28
# 24
print(time.time())
# 1676970448.3392222 <--输出的是秒
print(time.localtime(time.time()))
# time.struct_time(tm_year=2023, tm_mon=2, tm_mday=21, tm_hour=17, tm_min=7, tm_sec=28, tm_wday=1, tm_yday=52, tm_isdst=0)
# 输出的年月日时分秒，一周的第几天，一年的第几天
print(urllib.request.urlopen('http://www.baidu.com').read()) #<--发送请求，读取网址'www.baidu.com'