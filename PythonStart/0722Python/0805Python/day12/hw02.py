"""
    商场储物柜;
        储物柜:
            * 10个柜子, 10个条形码;

            1. 提供一个空柜子
            2. 打开存储物品的柜子
        人:
            * 条形码
"""
import random


class Person:
    def __init__(self):
        self.card_code = None


class Cabinet:
    def __init__(self):
        self.code_list = []  # 条形码 -- 柜子的数量统一

    # 获取一个空柜子
    def get_empty_cabinet(self, p_obj):  # 参数: 获取柜子的人
        if p_obj.card_code:
            print("请先归还柜子后,再次获取")
        else:
            # 柜子是不是满了, 如果没有满可以给他一个柜子
            if len(self.code_list) >= 10:
                print("目前柜子已满, 请稍后获取~")
            else:
                while True:
                    # 1. 随机生成一个验证码
                    s = self.get_card_code()
                    if s in self.code_list:
                        # 重复, 重新生成
                        continue  # 结束当前的循环, 继续下一次循环
                    else:
                        # 2. code_list和人的card_code分别存储验证码
                        p_obj.card_code = s
                        self.code_list.append(s)
                        print("成功获取柜子, 当前条形码为'%s'" % s)
                        break  # 结束循环

    # 归还储物柜
    def return_cabinet(self, p_obj):  # 参数: 人对象
        # 1. 判断条形码是否有效
        if p_obj.card_code in self.code_list:
            # 2. 如果有效 --> 删除人和储物柜的条形码记录
            self.code_list.remove(p_obj.card_code)
            p_obj.card_code = None
            print("您已成功打开柜子, 欢迎下次光临")
        else:
            p_obj.card_code = None
            print("您还没有柜子, 请先获取一个")

    def get_card_code(self):  # 随机生成验证码
        s = ""
        for char in random.sample("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM", 16):
            s += char
        return s


c1 = Cabinet()
p1 = Person()


c1.return_cabinet(p1)  # 您还没有柜子, 请先获取一个
c1.get_empty_cabinet(p1)  # 成功获取柜子, 当前条形码为'Kyv9p8ZmC5zHsSE6'
print(p1.card_code)  # Kyv9p8ZmC5zHsSE6
print(c1.code_list)  # ['Kyv9p8ZmC5zHsSE6']

for x in range(10):  # 产生10个数字,
    p = Person()
    c1.get_empty_cabinet(p)
    print(" -----------------------  ")

c1.return_cabinet(p1)  # 您已成功打开柜子, 欢迎下次光临

