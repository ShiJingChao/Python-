# 1. 给定一个以下字符串：统计大写字母的个数，小写字母的个数，非字母的个数。
# str1 = "ajdkkKDKEK1343KFKiriromfkfKKRIOWJF0928398jjee11djdDJJRH"

# str1 = "ajdkkKDKEK1343KFKiriromfkfKKRIOWJF0928398jjee11djdDJJRH"
# d_count = 0
# x_count = 0
# f_count = 0
# for i in str1:
#     if "A" <= i <= "Z":
#         d_count += 1
#     elif "a" <= i <= "z":
#         x_count += 1
#     else:
#         f_count += 1
# print("大写字母的个数为：{}，小写字母的个数为：{}，非字母的个数为：{}".format(d_count, x_count, f_count))

# 2. 给定一个路径名：
# String pathName="http://192.168.10.1:8080/Day33_Servlet/aa.jpeg";
# 获取文件名称：aa.jpeg

# pathName = "http://192.168.10.1:8080/Day33_Servlet/aa.jpeg"
# b = pathName.split('/')
# print(b[-1])

# 3. 字符串str="ABCDEFGHIJK"，要求输出最少一个最多八个的所有组合（向后连续字母）
# 输出如下：
# A
# AB
# ABC
# ABCD
# ABCDEFGH
# B
# BC
# BCD
# ...
# BCDEFGHI
# ...
# K

# str = "DEFGHIJK"
# str1 = "ABCDEFGHIJK"
# i = 0
# k = 0
# while k < 3:
#     for m in range(k, 8 + k):
#         print(str1[k:m + 1])
#     k += 1
# print()
# while i < 9:
#     for j in range(i, 8):
#         print(str[i:j + 1])
#     i += 1
# print()

s = "ABCDEFGHIJK"   # len(s) -->11
for i in range(0, len(s)):   # 0~10遍历出来切片的start [start::]
    for j in range(i+1, i+9):  # 8 遍历获取stop值
        if j > len(s):    # 如果stop结束值 > 字符串的长度
            break       # 结束内层循环
        print(s[i:j:])

# 4. 输入一个数，判断一个这个数是否是回文数。例如：121，这个数反过来还是121，所以这个是回文数；
# 再如：134，这个数反过来是431，所以这不是一个回文数；


# num = int(input("请输入一个数："))
# a = num
# b = 0
# while a > 0:
#     b = b*10+a%10
#     a = a//10
# if b == num:
#     print("是")
# else:
#     print("不是")

# 5.‘2018-11-12’去掉‘-’输出
# a = "2018-11-12"
# for i in a:
#     if i != "-":
#         print(i,end='')
#     else:
#         continue
s = 'abdefghdsa'
for i in s:
    if i == 'c':
        print(i)
else:
    print("没找到")