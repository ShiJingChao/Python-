from datetime import datetime # 引用datetime 库
now = datetime.now() # 获得当前日期和时间信息
print(now)
now.strftime("%x") # 输出其中的日期部分
print(now.strftime("%x"))
# print("------------------")
print(now.strftime("%X")) # 输出其中的时间部分
print(now.strftime("%A"))
print(now.strftime("%x  %X"))
print(now.strftime("%b %B"))