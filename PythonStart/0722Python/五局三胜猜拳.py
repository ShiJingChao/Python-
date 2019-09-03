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



# 游戏 规则：
# ("1.猜题游戏一共有10个题，每个题10分，共一百分")
# ("2.您在这个游戏中可以猜测10次，不管您答对还是答错，都会消耗猜测的次数")
# ("3.每道题目开始时，系统都会提示是否使用锦囊，一共有三次的锦囊机会
# （锦囊一共有三种  ，并且可以重复选择！）。同时，锦囊不算在猜测的次数中。")
# ("4.锦囊包括：1.提示水果第一个字。2.提示水果第二个字3.这个水果的字数")
# ("5.游戏可以提前结束")
import random

# a = ['西瓜', '梨子', '香蕉', '核桃', '苹果', '桃子', '花生', '石榴', '西瓜', '梨子']
# b = ['绿色的，红心', '配冰糖，暖到心', '弯弯的月儿小小的船,小小的船儿两头尖', '皱肉皱骨头， 骨头生在肉外头。', '乔布斯', '胖娃娃，没手脚，红尖嘴，一身毛，背上一道沟，肚里好味道。',
#      '青藤藤，开黄花，地上开花不结果，地下结果不开。,', '小小红坛子，装满红饺子，吃掉红饺子，吐出白珠子。', '绿色的，红心', '配冰糖，暖到心']
# i = 0
# jinnang = 1
# count = 0
# print("猜题游戏开始！")
# print("游戏一共十道，每题十分，共100分")
# while i < 10:
#     while True:
#         timu = 1
#         for j in b:
#             # print("第{}题：".format(timu), j)
#             if jinnang > 3:
#                 while True:
#                     print("第{}题：".format(timu), b[j])
#                     answer = input("请输入您的答案：")
#                     if answer != a[j]:
#                         print("您猜错了！您还有{}次机会".format(9 - i))
#                         i += 1
#                         continue
#                     else:
#                         print("您猜对了！您还有{}次机会".format(9 - i))
#                         count += 1
#                         timu += 1
#                         i += 1
#                         j += 1
#                         continue
#             else:
#                 while jinnang <= 3:
#                     print("第{}题：".format(timu), j)
#                     n = input("您是否需要使用锦囊？1：是2：否")
#                     if n == "1":
#                         print("1:提示水果第一个字\n2:提示水果第二个字\n3：提示这个水果的字数")
#                         chose = input("请输入您要使用的锦囊")
#                         if jinnang > 3:
#                             print("你已经使用了三次锦囊，不能再使用了")
#                             continue
#                         elif chose == "1":
#                             print("水果的第一个字为：", a[i][0])
#                             shengyu = 3 - jinnang
#                             print("您还有{}次使用锦囊的机会".format(shengyu))
#                             jinnang += 1
#                         elif chose == "2":
#                             print("水果的第二个字为：", a[i][1])
#                             shengyu = 3 - jinnang
#                             print("您还有{}次使用锦囊的机会".format(shengyu))
#                             jinnang += 1
#                         elif chose == "3":
#                             print("水果的字数为：", len(a[i]))
#                             shengyu = 3 - jinnang
#                             print("您还有{}次使用锦囊的机会".format(shengyu))
#                             jinnang += 1
#                     elif n == "2":
#                         answer = input("请输入您的答案：")
#                         if answer != a[i]:
#                             print("您猜错了！您还有{}次机会".format(9 - i))
#                             i += 1
#                             continue
#                         else:
#                             print("您猜对了！您还有{}次机会".format(9 - i))
#                             count += 1
#                             timu += 1
#                             i += 1
#                             break
#                 else:
#                     answer = input("请输入您的答案：")
#                     if answer != a[i]:
#                         print("您猜错了！您还有{}次机会".format(9 - i))
#                         i += 1
#                         continue
#                     else:
#                         print("您猜对了！您还有{}次机会".format(9 - i))
#                         count += 1
#                         timu += 1
#                         i += 1
#                         break
#
# else:
#     print("你已经没有机会了，你一共答对题目{}次".format(count))
