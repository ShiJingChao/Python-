"""
密码长度为10，每次生成10个密码
每次生成的10个密码的首位不能重复
存储在文件中，每个密码占一行

"""


import random
strs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ1234567890!@#$%^&*?"
str1 = set()
str11 = ""
file = open(r"D:/a.txt","a")
while True:
    if len(str1) == 10:
        break
    else:
        s = random.sample(strs,10)  # 从strs中取出10个，用s接收列表
        for i in s: # 遍历列表
            str11 += i  # 将列表中的字符拼接
        str1.add(str11[0])  # 将每个字符串的首字母存在集合中
        file.write(str11 + "\n")
        str11 = ""
        continue
file.close()
