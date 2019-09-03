#验证码第一种方式

# import random
# i = 0
# str = ""
# while True:
#     while i < 4:
#         if i < 1:
#             a = chr(random.randint(48, 57))
#             str += a
#         elif 1 <= i < 2:
#             a = chr(random.randint(65, 90))
#             str += a
#         else:
#             a = chr(random.randint(97, 122))
#             str += a
#         i += 1
#     print(str)
#     code = input("请输入验证码：")
#     if code == str:
#         print("验证成功")
#         break
#     else:
#         print("验证失败")

# 验证码另一种方式
# import random
# a = []
# b = []
# c = []
# print("请输入验证码：")
# for i in range(48,58):
#     a.append(i)
# for j in range(65,91):
#     a.append(j)
# for k in range(97,123):
#     a.append(k)
# for i in range(4):
#     str = random.choice(a)
#     b.append(str)
# # print(b)
# for n in b:
#         m = chr(n)
#         c.append(m)
# print(c)
# for i in c:
#     shuru = input()
#     for v in shuru:
#         if v == i:
#             print("正确")
#         else:
#             print("错误")
#             break

# a = [1, 2, 3, 4, 4, 5, 6, 7]
# print(a[0])
# print(a[1:1])
# print(a[0:1])

# list = [1, 2, 3, 4]
# it = iter(list)
# print(next(it))
# print(next(it))
