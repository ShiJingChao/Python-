# # 第一题
# # 流程图
# #  开始
# #  |
# #  \/       不满足
# #  判断条件——————————>执行else语句
# #   |满足if条件
# #  \/
# #  执行if语句
#
# # 第二题
# a = int(input('请输入数字:'))
# if a == 1:
#     print('星期一')
# elif a == 2:
#     print('星期二')
# elif a == 3:
#     print('星期三')
# elif a == 4:
#     print('星期四')
# elif a == 5:
#     print('星期五')
# elif a == 6:
#     print('星期六')
# elif a == 7:
#     print('星期日')
# else:
#     print('输入错误!!')
#
# # 第三题
# a = int(input('请输入月份:\n'))
# if 3 <= a <= 5:
#     print('当前季节为春季')
# elif 6 <= a <= 8:
#     print('当前季节为夏季')
# elif 9 <= a <= 11:
#     print('当前季节为秋季')
# elif 1 <= a <= 2 or a == 12:
#     print('当前季节为冬季')
# else:
#     print('输入错误!!')
#
# # 第四题
# user = input('请输入你的用户名:\n')
# password = input('请输入你的密码:\n')
# if user == 'admin' and password == '123456':
#     print('登陆成功!')
# else:
#     print('登录失败!')
# # 第五题
# user = input('请输入你的用户名:\n')
# password = input('请输入你的密码:\n')
# if (user == 'feizhu123' or user == '18067451231') and password == '123456':
#     print('登陆成功!')
# else:
#     print('登录失败!')
#
# # 第六题
#
# price = float(input("请输入商品单价"))
# number = int(input("请输入商品数量："))
# money = price * number
# choose = input("付款方式为：\n1.现金\n2.微信\n3.支付宝\n4.刷卡\n请输入你的选择：")
# if choose == '1':
#     print("您要付款的金额为%.2f" % money)
# elif choose == '2':
#     all_money = money * 0.95
#     print("您要付款的金额为%.2f" % all_money)
# elif choose == '3':
#     all_money = money * 0.9
#     print("您要付款的金额为%.2f" % all_money)
# elif choose == '4':
#     if money < 100:
#         print("您要付款的金额为%.2f" % money)
#     else:
#         all_money = money - (money // 100) * 20
#         print("您要付款的金额为%.2f" % all_money)
#
# # 第七题
# year = int(input("请输入年份："))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("是闰年")
# else:
#     print("不是闰年")
# # 循环题
# # 1
# for i in range(1, 100):
#     if i % 7 == 0:
#         print(i, end='\t')
# # 2
# sum = 0
# for i in range(1, 100, 2):
#     sum += i
# print(sum)
# # 3
# count = 0
# for i in range(1, 100):
#     if i % 3 == 0 and i % 5 != 0:
#         print(i, end='\t')
#         count += 1
#         if count % 5 == 0:
#             print()
# print("\n一共有：%d个" % count)
# # 4
# for i in range(100, 1000):
#     if (i // 100) ** 3 + (i % 100 // 10) ** 3 + (i % 100 % 10) ** 3 == i:
#         print(i)
# # 5
# for i in range(100, 200):
#     if i % 3 == 1 and i % 4 == 2 and i % 5 == 3:
#         print(i)
# # 6
# for i in range(1, 1000):
#     for j in range(1, i):
#         if i // j == 3 and i % j == 10 and i + j + 13 == 163:
#             print(i, j)
#             break
#
# # 7
# for i in range(1000, 9999):
#     if (i % 1000) * 3 == i:
#         print(i)
#         break
# # 8
# for i in range(380, 450):
#     for j in range(1, 450):
#         if i * 76 == j * 75 + (i - j) * 80.1:
#             print("男生有%d人，女生有%d人" % (j, i - j))
# # 9
# for i in range(10, 100):
#     if 300 + i - i * 10 - 3 == 468 or 300 + i - i * 10 - 3 == -468:
#         print(i)
#
# # 10
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (j, i, i * j), end='\t')
#     print()
#
# # 11
# for x in range(1, 20):
#     for y in range(1, 33):
#         for z in range(1, 300):
#             if 5 * x + 3 * y + 1 / 3 * z == 100 and x + y + z == 100:
#                 print("买{}只公鸡，{}只母鸡，{}只小鸡".format(x, y, z))
#
# # 连锁题
# # 1
# price_xiaohua = int(input("请输入小花挖取的宝藏价值："))
# price_ergou = int(input("请输入二狗挖取的宝藏价值："))
# if price_ergou > price_xiaohua:
#     print("二狗的价值更高，二狗赢了")
# elif price_xiaohua == price_ergou:
#     print("价值一样高")
# else:
#     print("小花的价值更高，小花赢了")
#
# # 2
# price_s_xiaohua = 99
# price_s_ergou = 87
# price_t_sanpang = int(input("请输入三胖偷走的宝藏价值："))
# if price_s_xiaohua + price_s_ergou > price_t_sanpang:
#     print("小花和二狗的总价值更高")
# elif price_s_xiaohua + price_s_ergou == price_t_sanpang:
#     print("价值相等")
# else:
#     print("三胖的价值更高")
#
# # 3
# sum = 0
# for i in range(37, 98, 2):
#     sum += i
# print("和为：%d" % sum)
#
# # 4
# start = int(input("请输入起始数值："))
# end = int(input("请输入截止数值："))
# sum = 0
# for i in range(start, end + 1):
#     if i % 2 != 0:
#         sum += i
#     else:
#         continue
# print("和为%d" % sum)
#
# # 5
# start = int(input("请输入起始数值："))
# end = int(input("请输入截止数值："))
# sum = 0
# choose = input("1.求全部和\n2.求奇数和\n3.求偶数和\n请选择：")
# if choose == "1":
#     for i in range(start,end+1):
#         sum += i
#     print("所有数的和为：%d" % sum)
# elif choose == "2":
#     for i in range(start, end + 1):
#         if i % 2 != 0:
#             sum += i
#         else:
#             continue
#     print("奇数和为%d" % sum)
# elif choose == "3":
#     for i in range(start, end + 1):
#         if i % 2 == 0:
#             sum += i
#         else:
#             continue
#     print("偶数和为%d" % sum)
# else:
#     print("输入错误！")
l1 = [i for i in range(10)]


def mulTen(n):
    return n * 10


l3 = map(mulTen, l1)
for i in l3:
    print(i, end=" ")
l4 = [i for i in l3]
print(l4)
