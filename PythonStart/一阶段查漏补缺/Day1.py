# 小数在运算涉及到二进制问题
# a = 0.1+0.2
# print(a)
# if (round(0.1) + round(0.2)) == round(0.3):
#     print(True)
# else:
#     print(False)  # True




"""

高级版
4位验证码：
要求不能重复，且必须含有字母

"""
# import random
# str = ""
# s_str = set()
# letter = [chr(i) for i in range(65,91)]
# letter1 = [chr(i) for i in range(97,123)]
# letter.extend(letter1)
# f = False
# while True:
#     for i in letter:
#         if i in s_str:
#             f = True
#     if len(s_str) == 4 and f == True:
#         break
#     else:
#         a = random.choice([chr(random.randint(48, 57)),chr(random.randint(65,90)),chr(random.randint(97,122))])
#         s_str.add(a)
# for i in s_str:
#     str += i
#
# print(str)
# code = input("请输入验证码：")
# if code == str:
#     print("验证成功")
# else:
#     print("验证失败")


# 格式 {:填充的字符 填充的方式 填充的宽度}

# a = "Python等级考试"
# b = "="
# c = ">"
# # {0:"=">25}
# print("{0:{1}{3}{2}}".format(a,b,25,c)) # 0 是a  0是后面索引值    {1}是b ，{3}是c {2}是25
#
# # [练习] 字符串'i love python' 将python填充长度为10, 右对齐, 填充字符为p
# s5 = 'i love {:p>10}'.format('python')
# print(s5)   # i love pppppython

# print(oct(8))
import os
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



