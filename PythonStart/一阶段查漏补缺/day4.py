# import sys
# print(sys.path)


# import time
# s = "2019-09-01-10-10-09"
# print(time.strftime("%Y=%m-%d@%H>%M>%S",time.gmtime()))

#
# class CaiZhu:
#     def __init__(self):
#         self.__land = "1000万平方公里"
#         self.__name = "财主"
#         self.gander = "男"
#         self.hobby = "make money"
#         self.__money = 100000
#     def makemoney(self,money):
#         print("{}每秒赚{}欧元".format(self.__name,money))
#     def cook(self,cooks):
#         print("{}喜欢{}".format(self.__name,cooks))
#     def invest(self,invests):
#         print("{}每晚都会{}".format(self.__name,invests))
#     def eat(self):
#         self.__money -= 1000
#     def say(self):
#         print("说话")
#     def __str__(self):
#         return "{}{}{}{}".format(self.__name,self.gander,self.__land,self.hobby)

from datetime import datetime


# class ShiJian:
#
#     def shijian(self):
#         # 构造一个将来的时间
#         future = datetime.strptime('2019-09-13 00:00:00', '%Y-%m-%d %H:%M:%S')
#         # 当前时间
#         now = datetime.now()
#         # 求时间差
#         delta = future - now
#         hour = delta.seconds / 60 // 60
#         minute = (delta.seconds - hour * 60 * 60) // 60
#         seconds = delta.seconds - hour * 60 * 60 - minute * 60
#         print_now = now.strftime('%Y-%m-%d %H:%M:%S')
#         print("\r今天是：", print_now, "距离中秋节还剩下：", delta.days, '天', hour, '小时', minute, '分', seconds, '秒', end='')
#
# a=ShiJian()
# while 1:
#     a.shijian()


# t = datetime.strptime('2019-09-13 00:00:00',"%Y-%m-%d %H:%M:%S")


#
# class Father:
#     def __init__(self):
#         self.house = "草房"
#     def hobby(self):
#         pass

# class Ta:
#     def __init__(self):
#         self.blood = 500
#
# class Hero:
#     def __init__(self,name,genre,design,attack):
#         self.attack = attack
#         self.name = name
#         self.genre = genre
#         self.design = design
#     def touta(self):
#         print("{}正在偷塔")
#     def farm(self):
#         print("打野")
#     def zhuangbei(self,equit):
#
#
#
#
# jiansheng = Hero("剑圣","敏捷型","帅气",100)
# print(jiansheng.name,jiansheng.design,jiansheng.genre,jiansheng.attack)
# jiansheng.touta()
# jiansheng.farm()

# time 库的使用


import time
t = time.time()
tm = time.localtime()
t1 = time.strftime("%Y-%m-%d %H:%M:%S",tm)
t2 = time.strptime(tm,"%Y-%m-%d %H:%M:%S")
t3 = time.gmtime()
t4 = time.mktime(tm)
t5 = datetime.t



