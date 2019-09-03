# a = int(input('请输入一个正整数：'))
# b = 0
# max = 0
# small = 0
# while a > 0:
#     b = a % 10
#     a = a // 10
#     small = max
#     if max < small:
#         max = small
#     if max < b:
#         max = b
# print(max)

# data = int(input("请输入一个正整数"))
# max = 0
# while data>0:
#     if data%10>max:
#         max = data%10
#     data = data//10
# print(max)


# i = 0
# k = 0
# j = 0
# a = 0
# b = 0
#
# while k < 10:
#     zf = input('请输入字符：')
#     if k == 1:
#         max = ord(zf)
#         min = ord(zf)
#     if '0' < zf < '9':
#         i += 1
#     if 65 <= ord(zf) <= 90:
#         j += 1
#     a = ord(zf)
#     if max < ord(zf):
#         max = ord(zf)
#     elif small > ord(zf):
#         small = ord(zf)
#     k += 1
# print("数字的个数：{}，大写字母的个数{}，最大的数为：{}，最小的数为：{}".format(i, j, max, small))
#
# i = 1  # 控制循环
# dx, num = 0, 0  # 记录大写字母,记录数字
# chara = input('请输入的字符：')
# new_chara = ord(chara)  # 求字符的ASCII
# max, min = ord(chara), ord(chara)
# while i < 10:
#     i += 1
#     if 65 <= new_chara <= 90:
#         dx += 1
#     if '0' <= chara <= '9':
#         num += 1
#     if new_chara > max:
#         max = new_chara
#     if min > new_chara:
#         min = new_chara
#     chara = input('请输入的字符：')
#     new_chara = ord(chara)  # 求字符的ASCII
# print('大写字母有%d个，数字有%d个,最大的ASCII为%d,最小的ASCII为%d' % (dx, num, max, min))


# 10 -20之间，遇到7的倍数跳过，尾数为7结束
# i = 0
# while i < 20:
#     i += 1
#     if i % 7 == 0:
#         continue
#     if i % 10 == 7:
#         break
#     print(i)


for i in range(1, 100):
    if i % 2 == 0:
        print(i, end=" ")
    else:
        continue
    print()
for j in range(1, 100):
    if j % 2 != 0:
        print(j, end=" ")
    else:
        continue

