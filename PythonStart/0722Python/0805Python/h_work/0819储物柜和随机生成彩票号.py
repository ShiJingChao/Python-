import random
#   随机生成彩票 六个红球  一个蓝球
class Lottery:  # 彩票类
    z = "必中"
    def lott_creat(self):   # 生成彩票
        red_num = [i for i in range(1,35)]
        blue_num = [i for i in range(1,17)]
        blue_bol = random.sample(blue_num, 1)   # 在蓝球中取 1 个
        bol = random.sample(red_num,6)  # 在红球中取1个
        bol.extend(blue_bol)
        return bol
def main():
    while True:
        print("*"*30,
              "\n*\t\t小郭彩票生成器\t\t*\n*\t\t请输入“必中”生成彩票号 *")
        print("*"*30)
        b_in = input()
        a = Lottery()
        b = a.lott_creat()
        if b_in == a.z:
            print("红球为：")
            for i in range(len(b)-1):
                print(b[i],end=" ")
            print("蓝球为：%d"%b[-1])
        else:
            print("输错了，重新输入！")

if __name__ == "__main__":
    main()


# user = []
# bar_code = []
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
# class Locker:
#     def bar_c(self):
#         code = ""
#         for i in range(16):
#             a = random.randint(0, 6)
#             if 0 <= a < 2:
#                 code += str(random.randint(0, 9))
#             elif 2 < a <= 4:
#                 code += chr(random.randint(65, 90))
#             elif 4 < a <= 6:
#                 code += chr(random.randint(97, 122))
#         if code in bar_code:
#             self.bar_c()
#         else:
#             bar_code.append(code)
#             print(code)
#     def user_b(self,name):
#         if name in user:
#             print("请您归还上一个柜子后再来~")
#         else:
#             user.append(name)
#             print("柜子已打开，请放好您的物品，您的条形码为：")
#             self.bar_c()
# def main():
#     while True:
#         l = Locker()
#         print("*"*30,"\n*\t欢迎使用储物柜系统\t\t*\n*\t1.使用储物柜\t\t\t\t*\n*\t2.归还储物柜\t\t\t\t*\n*\t3.退出\t\t\t\t\t*")
#         print("*"*30)
#         choose = input()
#         if choose != "1" and choose != "2" and choose != "3":
#             print("输入有误!")
#         elif choose == "1":
#             if len(bar_code) >= 10:
#                 print("10个储物柜都被使用中，请您稍后再来!")
#                 continue
#             else:
#                 in_name = input("请输入您的姓名：")
#                 l.user_b(in_name)
#         elif choose == "2":
#             in_code = input("请输入条形码：")
#             if in_code in bar_code:
#                 print("验证成功...正在打开柜子...请不要走开...")
#                 del user[bar_code.index(in_code)]
#                 bar_code.remove(in_code)
#             else:
#                 print("您的条形码不存在或已被使用!")
#         elif choose == "3":
#             exit()
#
#
#
# if __name__ == "__main__":
#     main()





