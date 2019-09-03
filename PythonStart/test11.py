# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))

#
# a = 5
# b = 10
# c = 3
# d = 4
# e = 5
# a += b
# print("a= ", a)
# a -= c
# print("a= ", a)
# a *= d
# print("a= ", a)
# a /= e
# print("a = ", a)
#
# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not flag1
# print("flag1 = ", flag1)
# print("flag2 = ", flag2)
# print("flag3 = ", flag3)
# print("flag4 = ", flag4)
# print("flag5 = ", flag5)
# print(flag1 is True)
# print(flag2 is not False)
#
# import math
#
# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)

# year = int(input('请输入年份: '))
# # 如果代码太长写成一行不便于阅读 可以使用\或()折行
# is_leap = (year % 4 == 0 and year % 100 != 0 or
#            year % 400 == 0)
# print(is_leap)

# username = input('请输入用户名: ')
# password = input('请输入口令: ')
# # 如果希望输入口令时 终端中没有回显 可以使用getpass模块的getpass函数
# # import getpass
# # password = getpass.getpass('请输入口令: ')
# if username == 'admin' and password == '123456':
#     print('身份验证成功!')
# else:
#     print('身份验证失败!')

#
# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print('f(%.2f) = %.2f' % (x, y))


# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# else:
#     if x >= -1:
#         y = x + 2
#     else:
#         y = 5 * x + 3
# print('f(%.2f) = %.2f' % (x, y))


# value = float(input('请输入长度: '))
# unit = input('请输入单位: ')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 = %f厘米' % (value, value * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%f厘米 = %f英寸' % (value, value / 2.54))
# else:
#     print('请输入有效的单位')


# 掷骰子

# from random import randint
# face = randint(1, 6)
# if face == 1:
#     result = '唱首歌'
# elif face == 2:
#     result = '跳舞'
# elif face == 3:
#     result = '学狗叫'
# elif face == 4:
#     result = '做俯卧撑'
# elif face == 5:
#     result = '绕口令'
# else:
#     result = '讲笑话'
# print(result)

# 练习3：百分制成绩转等级制
# """
# 百分制成绩转等级制成绩
# 90分以上    --> A
# 80分~89分    --> B
# 70分~79分	   --> C
# 60分~69分    --> D
# 60分以下    --> E

# score = float(input('请输入成绩：'))
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'E'
# print('对应的等级是：', grade)


# 练习4：输入三条边长如果能构成三角形就计算周长和面积
# """
# 判断输入的边长能否构成三角形
# 如果能则计算出三角形的周长和面积

# import math
# a = float(input('a= '))
# b = float(input('b= '))
# c = float(input('c= '))
# if a + b > c and a+c > b and b+c > a:
#     print('能构成三角形')
#     p = (a + b + c)/2
#     area = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print(area)
# else:
#     print('不构成三角形')


# 用for循环实现1~100求和

# sum = 0
# for x in range(101):
#     sum += x
# print(sum)

# 用for循环实现1~100之间的偶数求和

# sum = 0
# for x in range(2, 101, 2):
#     sum += x
# print(sum)

'''
while循环
如果要构造不知道具体循环次数的循环结构，
我们推荐使用while循环，
while循环通过一个能够产生或转换出bool值
的表达式来控制循环，表达式的值为True循环继续，
表达式的值为False循环结束。
下面我们通过一个“猜数字”的小游戏
（计算机出一个1~100之间的随机数，
人输入自己猜的数字，计算机给出对应的提示信息，
直到人猜出计算机出的数字）来看看如何使用while循环。

猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
'''

# import random
#
# answer = random.randint(1, 100)
#
# count = 0
# while True:
#     count += 1
#     a = int(input('请输入你要猜的一个整数：'))
#     if a > answer:
#         print('您猜的数大了')
#     elif a < answer:
#         print('您猜的数小了')
#     else:
#         print('您猜对了！')
# print('您一共猜了'+count+'次')
# if count > 7:
#     print('您的智商有待提升！')


# from math import sqrt
#
# num = int(input('请输入一个正整数: '))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)


# name = "尼古拉斯赵四"
# age = 38
# gender = False
# height = 1.78
# weight = 60.3
# print(name, age, gender, height, weight)


# prise = 3.5
# count = 4
# print("单价为：", prise, "数量为：", count, "\n的榴莲总价格为：", prise*count)

# 十进制转换为其他进制
# print(hex(100))  # 十六进制
# print(oct(100))  # 八进制
# print(bin(100))  # 二进制
# # 其他进制转换为十进制
# print(0b100)
# print(0o100)
# print(0x100)


#
# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break

# 倒叙输出三位整数
#  num = int(input("请输入一个三位整数"))
# a = num % 10
# b = num // 100
# c = num // 10 % 10
# print(a*100+c*10+b)

# a = int(input("请输入两位以上整数："))
# b = 0
#
# b = b * 10 + a % 10
# a = a // 10
# b = b * 10 + a % 10
# a = a // 10
# b = b * 10 + a % 10
# a = a // 10
# print(b)
# 打印各种三角形图案

# row = int(input())
# for i in range(row):
#     for j in range(i+1):
#         print('*', end='')
#     print()


# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()
# #
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     # print()


# print(10+2 and 3//2 or 4**2/5 and 5*2)

# print(2//-9)
# print(-1 % 2)
#
# price = float(input("请输入水果的价格(元/kg)："))
# weight = float(input("请输入要买水果的重量(kg)："))
# money = price*weight
# print("水果的总价格为{}元".format(money))


# r = float(input("请输入圆的半径："))
# PI = 3.14
# area = PI*r*r
# c = 2*r*area
# print("半径为{}的圆的面积为{}，周长为{}".format(r, area, c))

# 寻找三位数水仙花数
# for i in range(100, 999):
#     if (i//100)**3+(i % 100//10)**3+(i % 10)**3 == i:
#         print(i)
# for i in range(100, 999):
#     if (i//100)**3+(i % 100//10)**3+(i % 10)**3 == i:
#         print(i)
# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print("欢迎来到成人世界~")
# else:
#     print("年龄太小了，好好学习，过几年再来吧~")
#
#
# age = int(input("请输入女生的年龄："))
# high = int(input("请输入女生的身高（cm）："))
# weight = int(input("请输入女生的体重（斤）"))
# beautiful = int(input("请输入这个女生是否好看（好看输入1，不好看输入2）"))
# rich = int(input("请输入这个女人是否有钱（是请输入1，不是输入2）："))
# if 18 <= age < 22 and high > 170 and weight < 100 and beautiful == 1 or rich == 1:
#     print("你可以表白")
# else:
#     print("这个女生不适合你~")


# num = int(input("请输入一个数字（1~7）："))
# if num == 1:
#     print("今天是周一")
# elif num == 2:
#     print("今天是周二")
# elif num == 3:
#     print("今天是周三")
# elif num == 4:
#     print("今天是周四")
# elif num == 5:
#     print("今天是周五")
# elif num == 6 or num ==7:
#     print("今天是周末")
# else:
#     print("输入信息有误")


# high = float(input("请输入身高（m）："))
# weight = float(input("请输入体重（kg）："))
# BMI = weight/high**2
# if BMI < 18.5:
#     print("过轻")
# elif BMI < 25:
#     print("正常")
# elif BMI < 28:
#     print("过重")
# elif BMI < 32:
#     print("肥胖")
# else:
#     print("严重肥胖")

# 找出1~9999之间的所有完美数
# 完美数是除自身外其他所有因子的和正好等于这个数本身的数

# import math
#
# for num in range(1, 99999):
#     sum = 0
#     for j in range(1, int(math.sqrt(num)+1)):
#         if num % j == 0:
#             sum += j
#             if j > 1 and num / j != j:
#                 sum += num/j
#     if sum == num:
#         print(num)


# x = int(input("请输入两个数："))
# y = int(input())
# max = x if x > y else y
# print(max)


# import random
# pc_ges = random.randint(1, 3)
# print("请输入你要出的：（1：石头 2：剪刀 3：布）")
# gesture = int(input())
# print("电脑出的手势为：", pc_ges)
# if gesture == pc_ges:
#     print("平局")
# elif:

# year = int(input("请输入年份："))
# if year%4 == 0 and year % 100 != 0 or year%400 == 0:
#     print("{}年为闰年".format(year))
# else:
#     print("{}年不是闰年".format(year))

# user = input("请输入用户：")
# if user == "root":
#     print("您的权限为超级管理员")
# elif user == "test":
#     print("您的权限为普通管理员")
# elif user == "test1" or user == "test2":
#     print("您的权限为业务主管")
# else:
#     print("您的权限为普通用户")


# num1 = float(input("请输入一个数字："))
# operator = input("请输入你要做的运算（+、-、*、/）:")
# if operator == "+":
#     num2 = float(input("请输入第二个数字："))
#     result = num1 + num2
#     print("{}{}{}={}".format(num1, operator, num2, result))
# elif operator == "-":
#     num2 = float(input("请输入第二个数字："))
#     result = num1 - num2
#     print("{}{}{}={}".format(num1, operator, num2, result))
# elif operator == "*":
#     num2 = float(input("请输入第二个数字："))
#     result = num1 * num2
#     print("{}{}{}={}".format(num1, operator, num2, result))
# elif operator == "/":
#     num2 = float(input("请输入第二个数字："))
#     result = num1 / num2
#     print("{}{}{}={}".format(num1, operator, num2, result))

# gender = input("您的性别是（m为男，f为女）：")
# # age = int(input("您的年龄为："))
# # if gender == "f" or gender == "F":
# #     if 10 <= age <= 12:
# #         print("你可以加入球队")
# #     else:
# #         print("你不可以加入球队")
# # else:
# #     print("你不可以加入球队")

# n = 100
# while n < 999:
#     n += 1
#     num1 = (n // 100)**3
#     num2 = (n % 100 // 10)**3
#     num3 = (n % 100 % 10)**3
#     if n == num1 + num2 + num3:
#         print(n)
# n = 0
# while n < 9:
#     n += 1
#     print(n)
#
# n = 0
# sum = 0
# while n < 10:
#     n += 1
#     sum += n
# print(sum)

# n = 0
# sum = 0
# while n < 99:
#     n += 2
#     sum += n
# print(sum)

# n = 0
# sum = 0
# while n < 99:
#     n += 3
#     sum += n
# print(sum)
#
# sum = 0
# count = 1
# while count < 101:
#     if count % 2 == 0:
#          sum -= count
#     else:
#          sum += count
#     count = count + 1
# print(sum)

# distance = 380000000000
# a4 = 0.088
# i = 0
# while a4 < distance:
#     a4 = a4 * 2
#     i += 1
# print(i)

# people = 14
# add = 0.0053
# count = 0
# while people < 20:
#     people = people*(1+add)
#     count +=1
# print(count)
import random

# age = random.randint(1,3)
# i = 0
# while i < 3:
#     guess = int(input("请输入你要猜的年龄："))
#     if guess == age:
#         print("猜对了")
#         break
#     i += 1

# import random
# i = 3
# times1 = 0
# times2 = 0
# print("五局三胜猜拳游戏开始~\n")
# while True:
#     pc_ges = random.randint(1, 3)
#     print("请输入你要出的：（1：石头 2：剪刀 3：布）")
#     gesture = int(input())
#     print("电脑出的手势为：", pc_ges)
#     if (gesture == 1 and pc_ges == 2 or gesture == 2 and pc_ges == 3
#             or gesture == 3 and pc_ges == 1):
#         print("你赢了")
#         times1 += 1
#     elif (gesture == 1 and pc_ges == 3 or gesture == 2 and pc_ges == 1
#             or gesture == 3 and pc_ges == 2):
#         print("你输了")
#         times2 += 1
#     else:
#         print("平局")
#     if times1 == 2:
#         print("你已经赢了两局，你胜了")
#         break
#     elif times2 == 2:
#         print("电脑已经赢了两局，你输了")
#         break


# num = eval(input('请输入一个数字:'))
# if num <= 1:
#     print('这不是质数')
# elif num == 2:
#     print('这是一个质数!')
# else:
#     i = 2
#     while i < num:
#         if num % i == 0:
#             print('这不是一个质数')
#             break
#         i += 1
#     else:
#         print('这是一个质数!')


# age = random.randint(1, 99)
# # i = 0
# # while True:
# #     guess = int(input("请输入你要猜的年龄："))
# #     if guess == age:
# #         print("猜对了，你还要继续猜吗？（Y：继续 N：退出）")
# #     else:
# #         print("猜错了，你还要继续猜吗？（Y：继续 N：退出）")
# #     answer = input("")
# #     if answer == "N":
# #         break

# age = random.randint(1, 99)
# i = 0
# while i < 3:
#     i += 1
#     guess = int(input("请输入你要猜的年龄："))
#     if guess == age:
#         print("猜对了")
#         break
#     else:
#         print("猜错了")
#     if i == 3:
#         answer = input("是否继续？Y:继续N：停止\n")
#         if answer == "Y":
#             i = 0
#         else:
#             break

# cout = 0
# age = 18
# while True:
#     if cout == 3:
#         ans = input("继续Y,否N")
#         if ans == "Y" or ans == "y":
#             cout = 0
#         else:
#             break
#     input_age = int(input("猜的年龄："))
#     if input_age == age:
#         print("对了")
#     else:
#         print("错了")
#     cout += 1


# n = 0
# i = 4
# while i > 0:
#     i -= 1
#     n += 1
#     print(" "*i, "*"*(2*n-1))

# user = "12345"
# pwd = "0000"
# i = 0
# while i < 3:
#     i += 1
#     in_user = input("请输入用户名：")
#     if in_user == user:
#         in_pwd = input("请输入密码：")
#         if in_pwd == pwd:
#             print("登录成功")
#         else:
#             print("密码错误，剩余", 3-i, "次")
#             continue
#     else:
#         print("用户名错误，剩余", 3-i, "次")
#         continue
#     if i == 3:
#         break

# n = 100
# while n < 999:
#     n += 1
#     num1 = (n // 100)**3
#     num2 = (n % 100 // 10)**3
#     num3 = (n % 100 % 10)**3
#     if n == num1 + num2 + num3:
#         print(n)


# 求100 以内所有的质数
# from time import time
#
# from math import sqrt
#
# begin = time()
i = 2

# while i < 100:
#     judge = True
#     j = 2
#     while j <= i**0.5:
#         if i % j == 0:
#             judge = False
#             break
#         j += 1
#     if judge:
#         print(i)
#     i += 1
# end = time()
# print(end - begin)


# player = "任思锦"
# print("=" * 20, "欢迎来到《{}大战白骨精》休闲小游戏".format(player), "=" * 20)
# cos = input("请输入你要扮演的角色：\n\t1：{}\n\t2：白骨精\n请选择（1-2）：".format(player))
# health_point = 2
# attack = 2
# judge = True
# boss_health = 50
# boss_attack = 10
# if cos == "1":
#     print("恭喜你将以{}的身份进行游戏!\n".format(player), "=" * 60)
# elif cos == "2":
#     print("什么？！看看游戏名，太不要脸了，你竟然选择白骨精，白骨精可是BOSS\n"
#           "你已经被系统分配以->{}-<身份进行游戏\n".format(player), "=" * 60)
# else:
#     print("你输入的信息有误，系统自动分配，你将以->{}<-的身份进行游戏".format(player))
# print("\n你的身份是->{}<-,你的攻击力是2 你的生命值是：2\n".format(player))
# while True:
#     choose = input("请选择你要进行的操作：\n\t1:练级\n\t2:打BOSS\n\t3:逃跑"
#                    "\n请选择要做的操作[1-3]:")
#     if choose == "1":
#         health_point += 2
#         attack += 2
#         print("恭喜你升级了，你现在的生命值为{}，攻击力为{}\n".format(health_point, attack), "-" * 60)
#     elif choose == "2":
#         while True:
#             print("-" * 20, "\n->{}攻击了->白骨精,白骨精受到了{}点伤害".format(player, attack))
#             boss_health -= attack
#             if boss_health > 0:
#                 print("-" * 20, "\n白骨精没有死，轮到白骨精攻击，{}受到{}点伤害".format(player, boss_attack))
#             if boss_health <= 0:
#                 print("{}打败了白骨精，{}是比白骨精更磨人的小妖精~".format(player, player))
#                 game_over = input("游戏结束，请输入任意键退出")
#                 if game_over == "Y":
#                     judge = False
#                     break
#                 else:
#                     judge = False
#                     break
#             else:
#                 health_point -= boss_attack
#                 if health_point <= boss_attack:
#                     game_over1 = input("{}太弱了，被白骨精的妖娆迷惑住了，你挂了\n游戏结束，请输入任意键退出".format(player, boss_attack))
#                     if game_over1 == "Y":
#                         judge = False
#                         break
#                     else:
#                         judge = False
#                         break
#     elif choose == "3":
#         print("{}迅雷不及掩耳之势神扭头，拍屁股撒腿就跑~".format(player))
#         game_over2 = input("游戏结束，请输入任意键退出")
#         if game_over2 == "Y":
#             break
#         else:
#             break
#     elif choose != "1" or choose != "2" or choose != "3":
#         print("输入错误，请重新输入！")
#     if judge == False:
#         break


# my_list = [1, 2, 3, 4, 5]
# i = 0
# print(my_list[::2])
# while True:
#     print(my_list[i])
#     i += 1
#     if i == 5:
#         break

#
# stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
# print(stus)
# stus[0] = 'sunwukong'
# print(stus)
# del stus[2]
# print(stus)
# stus[1:1] = ['牛魔王']
# print(stus)
# stus.insert(3,'傻屌')
# print(stus)

# i = 0
# for i in range(len(stus)):
#     print(stus[i])
#     i += 1


# for i in stus:
#     print(i)


# print("=" * 30, "欢迎使用员工管理系统", "=" * 30)
# i = 0
# ems_tips = "序号\t姓名\t年龄\t性别\t住址"
# ems_num = []
# ems_name = []
# ems_age = []
# ems_gender = []
# ems_address = []
# while True:
#     print("请选择要做的操作：\n\t\t1.查询员工\n\t\t2.添加员工\n\t\t"
#           "3.删除员工\n\t\t4.退出系统")
#
#     choose = input("请选择（1-4）：")
#     print("=" * 80)
#     if choose == "1":  # 打印所有员工信息
#         print(ems_tips)
#         for i in range(len(ems_name)):  # 将列表中的员工信息对应打印
#             print(ems_num[i], "\t\t", ems_name[i], "\t\t", ems_age[i], "\t\t", ems_gender[i], "\t\t", ems_address[i])
#     elif choose == "2":
#         # ems_num.append(len(ems_num)+1)
#         name = input("请输入姓名：")
#         ems_name.append(name)
#         age = input("请输入年龄：")
#         ems_age.append(age)
#         gender = input("请输入性别：")
#         ems_gender.append(gender)
#         address = input("请输入住址：")
#         ems_address.append(address)
#         print("保存成功！")
#     elif choose == "3":
#         in_name = input("请输入您要删除的员工名字：")
#         for j in range(len(ems_name)):  # 将输入的名字和员工名字一一对照检查，删除其它列表中员工对应的资料
#             if ems_name[j] == in_name:
#                 del(ems_num[j])
#                 del(ems_name[j])
#                 del(ems_age[j])
#                 del(ems_gender[j])
#                 del(ems_address[j])
#                 print("删除成功！")
#                 break
#             if ems_name[j] != in_name:
#                 print("没有此员工，请重新输入！")
#     elif choose == "4":
#         break
#     else:
#         print("输入错误，请重新输入！")


# 显示系统的欢迎界面
# print("=" * 30, "欢迎使用员工管理系统", "=" * 30)

# emps = ['\t孙悟空\t18\t\t男\t\t花果山', '\t猪八戒\t29\t\t男\t\t高老庄']
# while True:
#     print("请选择操作：")
#     print('\t1.查询员工')
#     print('\t2.添加员工')
#     print('\t3.删除员工')
#     print('\t4.退出系统')
#     user_choose = input('请选择[1-4]:')
#     print('=' * 80)
#     if user_choose == '1':  # 查询员工
#         print('\t序号\t姓名\t年龄\t性别\t住址')
#         n = 1
#         for emp in emps:
#             print(f'\t{n}\t{emp}')
#             n += 1
#     elif user_choose == '2':  # 添加员工
#         # 获取要添加员工的信息，年龄，性别，住址
#         emp_name = input("请输入员工的姓名：")
#         emp_age = input("请输入员工的年龄：")
#         emp_gender = input("请输入员工的性别：")
#         emp_address = input("请输入员工的住址：")
#
#         emp = f'\t{emp_name}\t\t{emp_age}\t\t{emp_gender}\t\t{emp_address}'
#         # 显示提示信息
#         print('以下员工将会被添加到系统中')
#         print('姓名\t年龄\t性别\t地址')
#         print(emp)
#         print('=' * 60)
#         user_confirm = input('是否确认该操作[Y/N]')
#
#         # 判断
#         if user_confirm == 'y' or user_confirm == 'Y':
#             emps.append(emp)
#         else:
#             # 取消操作
#             print("插入已取消！")

##字典
# 使用{}来创建字典
# d = {}  # 创建了一个空字典
# print(type(d))

# 创建一个保护有数据的字典
# 语法：
#   {key：value，key：value， key：value}
#   字典的key可以是任意的不可变对象（int、str、bool、tuple..）     但是一般我们都会使用str
#   字典的键是不能重复的，如果出现重复的，后面的会替换掉前面的
#  d = {'name': '孙悟空', 'age': '18', 'gender': '男'}
# print(d)

#   需要根据键来获取值
# print(d['name'], d['age'], d['gender'])

# 如果使用了字典中不存在的键，会报错

# 使用dict（）函数来创建字典
# 每一个参数都是一个键值对，参数名就是键，参数名就是值（这种方式创建的字典，key都是字符串）

# d = dict(name='孙悟空', age=18, gender='男')

# 也可以将一个包含有双值子序列的序列转换为字典
# 双值序列，序列中只有两个值，[1,2]('a',3) 'ab'
# 子序列， 如果序列中的元素也是序列，那么我们就称这个元素为子序列
# [（1, 2）, (3, 4)]
# d = dict[('name', '孙悟空'), ('age', 18)]
# print(d, type(d))
# d = dict(name='孙悟空', age=18, gender='男')  # 自动会给键加引号

# len() 获取字典中键值对的个数
# print(len(d))

# in 检查字典中是否包含指定的键
# not in 检查字典中是否包含指定的键
# print('name' in d)

# 获取字典中的值，根据键来获取值
# 语法： d[key]
# print(d['name'])  # 键要在适当的时候加上引号
# n = 'name'
# print(d[n])  # 此时就不用加上引号

# 通过[]来获取时，如果键不存在， 会抛出异常 KeyError
# get(key[, default]) 该方法用来根据键来获取字典中的值
# print(d.get('name'))
# print(d.get('hello'))  # 字典中的键没有hello，不会报错，会返回None
# 也可以指定一个默认值，来作为第二个参数，这样获取不到值得时候回返回默认值

# print(d.get('hello', '默认值'))    # 如果hello不存在，返回默认值

# 修改字典
# d[key] = value

# d['name'] = 'sunwufan'  # 修改字典的Key-value
# d['address'] = '花果山'    # 字典中没有address 向字典中添加key-value

# setdefault（key[, default]）   可以用来向字典中添加key-value
#   如果key已经存在于字典中，则返回key的值，不会对字典进行任何操作
#   如果key不存在，则向字典中添加这个key，并设置value

# result = d.setdefault('name', '猪八戒')
# d.setdefault('name', ' 猪八戒')  # 字典中有key  name 返回孙悟空
# d.setdefault('hello', '猪八戒')  #
# print('result = ', result)
# print(d)

# update([other])   将其它字典中的key-value添加到当前字典中

# d = {'a': 1, 'b': 2, 'c': 3}
# e = {'d': 4, 'e': 5, 'c': 6}
# d.update(e)
# print(d)    # 如果e中有相同的键名，会被后面的替换掉
#   输出结果：{'a': 1, 'b': 2, 'c': 6, 'd': 4, 'e': 5}

#   ASCII a = input("请输入一个大写字母（输出是第几个：）")
# print(ord(a)-64)

# 删除，可以使用del来删除字典中的key-value
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
# del d['a']
# del d['b']
# print(d)  # 运行结果：{'c': 3}

# popitem()
# 随机删除字典中的一个键值对，一般都会删除最后一个键值对
# 删除之后，它会将删除的key-value作为返回值返回
# 返回的是一个元组，元组有两个元素，第一个元素是删除的key，第二个元素是删除的value
# d.popitem()

# print('result=', d)
# print(d)      运行结果：result= {'a': 1, 'b': 2, 'c': 3}

# pop(key[,default])
# 根据key删除字典中的key-value
# 会将被删除的value返回！
# 如果删除不存在的key，会抛出异常
# 如果指定了默认值，再删除不存在的key时，不会报错，而是直接返回默认值
# result = d.pop('d')
# # print(d)    # 运行结果： {'a': 1, 'b': 2, 'c': 3, 'e': 5, 'f': 6}
# # result = d.pop('z', '这是默认值')    # 运行结果 result= 这是默认值

# del d['z'] 不存在，抛出异常
# result = d.popitem()
# result = d.popitem()
# result = d.popitem()
# result = d.popitem()
# result = d.popitem()
# result = d.popitem()    #用 popitem()删除空字典时，会抛出异常 KeyError: 'popitem(): dictionary is empty'

# clear() 用来清空字典
# d.clear()  # 将字典清空
# print('result=', result)
# print(d)

# copy()
# 该方法用于对字典进行浅复制（只会复制对象里面的值，如果字典中还有字典）
# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d  # 这种不算复制，因为指向的对象一样,并且修改一个会影响另一个
# d3 = d.copy()  # 这样为复制，和原对象独立

# d = {'a': {'name': '孙悟空', 'age': 18}, 'b': 2, 'c': 3}
# d2 = d.copy()
# d2['a']['name'] = '猪八戒'     #注意：浅复制只会简单的复制对象内部的值，如果值也是一个可变对象，这个可变对象不会被复制
# print('d = ', d)
# print('d2=', d2)
# print('d3= ', d3)


# 字典的遍历
# keys()该方法会返回字典的所有的key
# 该方法会返回一个序列，序列中保存所有字典的所有的键

