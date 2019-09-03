# 0715史景超
# 混合数字类型
# a = True
# print(True + 3)
# b = False
# print(False * 2)

# 判断字符类型——type()
# a1 = 3
# b1 = 8.5
# print(a1 + b1)
# print(type(a1 + b1))
#
# 将int 转换为float
# a2 = float(3)
# b2 = 2.2
# print(a2)
# print(a2 + b2)
#
# a4 = input('输入字符：')
# print(a4, type(a4))
#
# a5 = int(input('请输入一个数字：'))
# print(a5, type(a5))
#
# num = int(input('请输入购买数量：'))
# price1 = float(input(('请输入西红柿单价：')))
# print('讲完价的结果为：', int(price1))
# print("%d斤总价为%d：" % (num, num * int(price1)))
#
# # 十进制转换为其他进制的函数
#
# a = 5454
# print(a, '转换十六进制为：', hex(a))
# print(a, '转换为八进制为：', oct(a))
# print(a, '转换为二进制为：', bin(a))
# print('转换进制后的类型为：', type(bin(a)))
#
# # 其他进制转换为十进制
#
# a = int('11', 2)
# print('二进制转换为十进制为：', a)
# b = int('11', 8)
# print('八进制转换为十进制：', b)
# c = int('11', 16)
# print('十六进制转换为十进制：', c)
#
# 练习
# num1 = input('请输入一个十六位进制数：')
# print('转换为十进制为：', int(num1, 16))
# num2 = input('请输入一个八进制数：')
# print('转换为十进制为：', int(num2, 8))
# num3 = input('请输入一个二进制数：')
# print('转换为十进制为：', int(num3, 2))
#
# a = input('十六进制：')
# b = int(a, 16)
# print(b)
# a = input('八进制：')
# b = int(a, 8)
# print(b)
# a = input('二进制：')
# b = int(a, 2)
# print(b)
#
# print(hex(0o7))
# print(hex(0b111))
# print(bin(0b100011))
# print(oct(0x3321232))
#
# # 变量的指向引用
# a = 5
# print(type(a))
# a = 'tom'
# print(type(a))
#
# 变量的共享引用
# a = 5
# b = a
# print(a == b)
# print(a is b)
#
# # 变量之间的计算
# a, b = 2, 5
# print(a + b)
# a, b = '4', '6'
# print(a + b)
# print(a * 3)
# #
# # 打印python的关键字
# import keyword
#
# print(keyword.kwlist)
#
# # 区分大小写
#
# a, A = 1, 3
# print(a, A)
# a = chr(65)
# print(a)
#
# ord()  # 方法可以将输出的字符转换为ASCII对应的码值
# chr()  # 方法相反，转换为对应的字符
# end = input('请输入一个大写字母：')
# n = ord(end) - 64
# print('这是英文字母中的第%d个字符' % n)
#
# num = int(input('请输入一个数字：'))
# print('对应的字符为：', chr(num))
#
# a = 9.2
# b = 2
# print(a // b)
# a = -3.2
# b = 2
# print(a // b)  # 结果为-1，向下取整为-2.0

# # 反向三位数
# num = int(input("请输入一个三位数："))
# a = num // 100
# b = num // 10 % 10
# c = num % 10
# d = c * 100 + b * 10 + a
#
# a = int(input('请输入：'))
# b = 0
# b = b * 10 + a % 10
# a = a // 10
# b = b * 10 + a % 10
# a = a // 10
# b = b * 10 + a % 10
# a = a // 10
#
# # 判断奇偶数
# num = int(input("请输入一个数："))
# print("是否为偶数：", num % 2 == 0)
#
# # 去掉个数和小数部分买菜，取整
# price = float(input("输入西红柿单价："))
# weight = float(input("输入数量："))
# sum = price * weight
# sum = int(sum)
# sum = sum - sum % 10  # 去掉个位
#
# a = 4
# a += 5
# print(a)
#
# a = 4
# a -= 5
# print(a)
#
# a = 4
# a *= 5
# print(a)
#
# a = 4
# a %= 5
# print(a)
#
# a = 4
# a //= 5
# print(a)
#
# a = 4
# a **= 5
# print(a)
#
# # eval()函数
# a = '1+2'
# print(a)
# b = eval(a)  # 将字符串中有效的表达式进行计算
# print(b)
#
# # 变量的指向引用
# a = 5
# print(type(a))  # a没有类型，是a所指的地址存储的内容的类型
# a = 'tom'
# print(type(a))
# # 变量的共享引用
# a = 5
# b = a
# print(b)
# print(a == b)
# print(a is b)
#
# # 变量之间的运算
# a, b = 2, 5
# print(a + b)
# a, b = '4', '6'
# print(a + b)
# print(a * 3)
#
# # 打印python的关键字
# import keyword
#
# print(keyword.kwlist)
#
# # 区分大小写
# a, A = 1, 2
# print(a, A)
# a = chr(65)
# print(a)
#
# # ord()方法可以将输出的字符转换为ASCII对应的码值
# # chr()方法相反，转换为对应的字符
# eng = input('输入一个大写字母：')
# b = ord(eng) - 64
# print('这是字母中的第%d个字母' % b)
#
# num = int(input('输入一个数字：'))
# print('对应的字符为：', chr(num))
#
# a = 9.5
# b = 2
# print(a // b)
# b = 2
# print(a // b)
#
# # 反转三位数
# num = int(input('请输入一个三位数：'))
# a = num // 100
# b = num // 10 % 10
# c = num % 10
# d = c * 100 + b * 10 + a
# print(d)
#
# a = int(input('请输入：'))
# b = 0
# b = b * 10 + a % 10
# a = a // 10
# b = b * 10 + a % 10
# a = a // 10
# b = b * 10 + a % 10
# a = a // 10
# print(b)
# # 判断奇偶数
# num = int(input('请输入一个数：'))
# print('是否为偶数：', num % 2 == 0)
#
# # 去掉个数和小数点的数值，取整
# price = float(input("输入西红柿单价："))
# weight = float(input('数量：'))
# sum = price * weight
# sum = int(sum)
# sum = sum - sum % 10
# print('取完整的结果：', sum)
#
# a = 4
# a += 5
# print(a)
# a = 4
# a -= 5
# print(a)
# a = 4
# a *= 5
# print(a)
# a = 4
# a /= 5
# print(a)
# a = 4
# a //= 5
# print(a)
# a = 4
# a %= 5
# print(a)
#
# a = 4
# a **= 5
# print(a)
#
# # eval()函数
#
# a = '1+2'
# print(a)
# b = eval(a)
# print(b)
# # 写完了
#
# # h_work 计算题
# # 1.计算 True+100的值
# print(True + 100)
# # 2.将3.14 转换成 整数和布尔值
# print(int(3.14))
# print(bool(3.13))
# # 3.将十进制20分别使用二进制、八进制、十六进制进行转换
# print(bin(20))
# print(oct(20))
# print(hex(20))
# # 4.将字符串‘123’转换为int类型的数值，赋值给num,并查看num数据类型
# num = int('123')
# print(type(num))
# # 5.计算2的10次方
# print(2 ** 10)
# # 6.计算出101除以3的余数
# print(101 % 3)
# # 7.将 65 转换成 A
# char = chr(65)
# print(char)
# # 8.计算 字符串 "10/2" 的值
# num = eval('10/2')
# print(num)
#
# # 9.超市买苹果
# # 收银员向机器输入苹果的单价，输入客户购买的数量，显示总价格
# price = input('请输入苹果单价：')
# weight = input('请输入重量：')
# price = float(price)
# weight = float(weight)
# all_money = price * weight
# print(all_money)
#
# # 10. 数字逆序输出
# a = int(input("请输入一个三位数："))
# b = a % 10
# c = a // 10 % 10
# d = a // 100 % 10
# f = b * 100 + c * 10 + d
# print(f)
# a = "19"
# # print(int(a, 16))

# a = int(input("输入"))
# # num1 = a % 1000 % 100 % 10
# # num2 = a // 1000
# # num3 = a // 100
# # num4 = a //100%10
# # sum = num1 * 1000 + num4 * 100 + num3 * 10 + num2
# # print(sum)


# 7.17课堂练习# 7.17课堂练习# 7.17课堂练习# 7.17课堂练习# 7.17课堂练习# 7.17课堂练习# 7.17课堂练习# 7.17课堂练习# 7.17课堂练习# 7.17课堂练习# 7.17课堂练习# 7.17课堂练习

# salary = int(input('请输入你的工资：'))
# if salary >= 10000 and salary < 20000:
#     print("买春风650")
# if salary >= 30000:
#     print("马自达CX5")
# if salary >= 20000 and salary <30000:
#     print("买野马")

# score = int(input('请输入英语四级成绩：'))
# if score >= 425:
# 	print('颁发英语四级证书')
# if score <425:
# 	print("不颁发证书")

# 易错点：elif跟随最近的if语句
# score = float(input('请输入成绩：'))
# if score >= 90 and score <= 100:
#      print('A')
# if score >= 80 and score <90:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('E')

# a = input("请输入字符：")
# a1 = ord(a)
# if 65 <= a1 < 91:
#     print("输入的是大写字母")
# elif 97 <= a1 < 123:
#     print('小写字母')
# elif '0' <= a <= '9':
#     print("数字")
# elif a == '_':
#     print("下划线")
# else:
#     print("特殊字符")

# zf = input("输入人一个字符")
# if 'a' <= zf <= 'z':
#     print('小写')
# elif 65 <= ord(zf) <= 90:
#     print('大写')
# elif '0' <= zf <= '9':
#     print("数字")
# elif zf == '_':
#     print('下划线')
# else:
#     print('特殊')

# money = float(input("请输入购物金额："))
# if money >= 500:
#     sex = input('请输入性别：')
#     if sex == '男':
#         print('送刮胡刀')
#     elif sex == '女':
#         print('送口红')
# else:
#     sex = input('请输入性别：')
#     if sex == '男':
#         print('送打火机')
#     elif sex == '女':
#         print('送发卡')


# price = float(input("输入西红柿单价："))
# num = float(input("输入购买数量："))
# money = price * num
# if money > 50:
#     vip = int(input("请输入vip级别[1-3]："))
#     if vip == 1:
#         money = money * 0.8
#         print('花费的金额为:', money)
#     elif vip == 2:
#         money = int(money) - int(money) % 10
#         print('花费的金额为:', money)
#     elif vip == 3:
#         money = int(money)
#         print('花费的金额为:', money)
# else:
#     sex = input("请输入性别：")
#     if sex == '男':
#         print("送劳斯莱斯玩具")
#     else:
#         print("送小猫一只")


# money = int(input('请输入钱：'))
# while money >= 10:
#     money -= 10
#     print("吃一次西瓜，剩余%d元" % money)

# 6到2的乘积
# j = 1
# i = 6
# while i >= 2:
#     j *= i
#     i -= 1
# print(j)


# sum = 0
# i = 0
# num = int(input('请输入一个数：'))
# while i <= num:
#     sum += i
#     i += 1
# print(sum)

# data = int(input('请输入一个数：'))
# if data % 2 == 0:
#     print(data, '为偶数')
# elif data % 2 == 1:
#     print(data, '为奇数')

# 1到100偶数和
# i = 1
# # sum = 0
# # while i <= 100:
# #     if i % 2 == 0:
# #         sum += i
# #     i += 1
# # print(sum)


# 1-2+3-4...99

# sum = 0
# count = 1
# while count < 100:
#     if count % 2 == 0:
#         sum -= count
#     else:
#         sum += count
#     count = count + 1
# print(sum)

# i = 1
# zf = -1
# he = 0
# while abs(i) <= 99:
#     he += i
#     i = abs(i) + 1
#     i = i * zf
#     zf *= -1
# print(he)

# i = 1
# he = 0
# while i <= 99:
#     he = he + (-1) ** (i - 1) * i
#     i += 1
# print(he)


# 求三个数的最大值
# i = 0
# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字："))
# num3 = int(input("请输入第三个数字："))
# if num1 > num2 and num1 > num3:
#     print("最大的数为：%d" % num1)
# if num2 > num1 and num2 > num3:
#     print("最大的数为：%d" % num2)
# if num3 > num1 and num3 > num2:
#     print("最大的数为：%d" % num3)

# a = int(input('第一个数'))
# b = int(input('第二个数'))
# c = int(input('第三个数'))
# max = a
# if b>max:
#     max = b
# if c>max:
#     max = c
# print(max)

# max = int(input("输入第一个数："))
# i = 1
# while i <= 4:
#     data = int(input("输入："))
#     if data > max:
#         max = data
#     i += 1
# print(max)


# i = 1
# # while i <= 5:
# #     age = int(input('输入年龄：'))
# #     if age < 0:
# #         print("输入有误", age)
# #         break
# #     i += 1


# i = 1
# while i < 20:
#     if i % 3 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

# i = 0
# sum = 0
# ave = 0     #平均年龄
# age1 = 0    #不符合的年龄个数
# while i < 10:
#     i += 1
#     age = int(input("请输入年龄："))
#     if age < 18:
#         age1 = i
#         continue
#     elif 18 <= age <= 65:
#         sum += age
#         ave = sum / (i-age1)
#     elif age > 65:
#         break
# print('平均年龄为：', ave)

# 月考会考
# a = int(input('请输入：'))
# b = 0
# while a > 0:
#     b = b * 10 + a % 10
#     a = a // 10
# print(b)
