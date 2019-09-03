"""
    彩票

    抽样sample()
"""
import random


class Lottery:
    def __init__(self):
        self.red_list = []  # 红球数列
        self.blue_list = []  # 篮球数列

    def get_lottery_nums(self):  # 生成一组彩票号
        self.red_list = random.sample(range(1, 35), 6)
        self.blue_list.append(random.choice(range(1, 17)))
        # 红球  1-34 --> 6
        # 篮球  1-16 --> 1
        return self.red_list + self.blue_list


lot = Lottery()
print(lot.get_lottery_nums())  # 生成一组彩票号
print(lot.red_list)  # 获取红球数列
print(lot.blue_list)  # 获取篮球数列




