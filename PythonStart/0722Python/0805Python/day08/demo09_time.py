"""
    time:
        python自带的管理时间的模块

        表示方法:
            1. 时间戳: 某个时间距离1970-01-01 00:00:00的秒数
                        时间戳 --> 浮点数  基准时间: 1970-01-01 00:00:00
            2. 时间元组:
            3. 时间字符串: '2019-08-15', '2019年8月15号', '08/15/2019'
            -----
            时间戳: 计算机用来记录时间
            时间元组: 在程序中操作时间
            时间字符串: 方便人看的


        time.sleep() : 睡眠功能, 让程序等待多少秒以后再执行
        time.time() : 时间戳
        time.localtime() : 获取当前时间的时间元组

        时间元组 VS 时间字符串
            time.strptime(string, format)  将时间字符串 --> 时间元组  参数1: 时间字符串  参数2: 字符串对应的格式
            time.strftime(format, t)  将时间元组 --> 时间字符串 参数1: 要转换的格式  参数2: 时间元组

        时间戳 --> 时间元组
            time.gmtime(secs)  将时间戳 --> UTC时间元组
            time.localtime(secs)  将时间戳 --> 当地时间-时间元组

        结构化时间
            time.asctime(t)  将时间元组结构化
            time.ctime(secs) 将时间戳结构化
"""
# -*- coding:utf-8 -*--
import time

# print("肉丝打卤面")
# time.sleep(3)  # 睡 3 s
# print("鸡蛋西红柿打卤面")

# print(time.time())  # 1565854947.6424704
# print(time.localtime())
# time.struct_time(tm_year=2019, tm_mon=8, tm_mday=15, tm_hour=15, tm_min=45, tm_sec=51, tm_wday=3, tm_yday=227, tm_isdst=0)

# time.strptime(string, format)  时间字符串 ---> 时间元组
s = "08-15-2019"
t1 = time.strptime(s, "%m-%d-%Y")
print(t1)

# time.strftime(format, t)  时间元组 ---> 时间字符串
# 将时间元组t1 转换成 时间字符串 "19年08月15日"
s1 = time.strftime("%y-%m-%d", t1)  # 19-08-15
print(s1)

# 时间戳 -- 时间元组之间的转换
t = time.time()
res1 = time.gmtime(t)  # 获取时间戳所对应的时间元组 UTC -- 格林尼治时间
res2 = time.localtime(t)  # 获取时间戳所对应的时间元组
print(res1)
print(res2)

# 结构化时间
res3 = time.asctime(t1)
res4 = time.ctime(t)
print(res3)  # Thu Aug 15 00:00:00 2019
print(res4)  # Thu Aug 15 16:12:57 2019
