# 3 生成一百个一百以内随机数，判断其中不重复的有多少个（可借助set集合
import random
s = set()
for i in range(100):
    s.add(random.randint(0,100))
print(s)
print(len(s))