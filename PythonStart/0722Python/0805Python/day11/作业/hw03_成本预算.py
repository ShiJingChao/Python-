"""
分析:
    材料: A,    B,    C
    数量: 50,  100,   30   --> 生产出一个水杯所需数量,单位为g

    变量: A_price, B_price, C_price, 价格 --> 属性

[注意]: AttributeError: 'A' object has no attribute 'get_num1'
    python中类的属性和方法使用的都是同一个单词 attribute(属性)

    a: 属性
    b, c : 方法
"""


class Cup:
    def __init__(self, a_p, b_p, c_p):
        self.a_price = a_p
        self.b_price = b_p
        self.c_price = c_p

    def get_sum_price(self, count):  # 给出生产个数,得出总成本
        res = self.get_single_price(count)
        all_money = 0  # 用来记录所有原材料的总成本
        for v in res.values():
            all_money += v[1]  # 每次遍历一种原材料, 就将该材料的成本加入到总成本中去
        return all_money  # 循环遍历结束, 所有材料的成本都加入到all_money中了

    def get_single_price(self, count):  # count 生产个数
        """
        给出生产个数得出每种原材料的使用量和总成本
        :param count: 生产个数
        :return: {"原材料": (使用量, 总成本)}
        """
        # 使用量 --> 每种原材料的总数量 = 每种原材料做一个的数量 * 需要做的生产个数
        a_count = 50 * count
        b_count = 100 * count
        c_count = 30 * count
        # 成本 --> 每种原材料的总成本 = 总数量 * 单价
        a_money = a_count * self.a_price
        b_money = b_count * self.b_price
        c_money = c_count * self.c_price
        # a, b, c
        return {"a材料": (a_count, a_money), "b材料": (b_count, b_money), "c材料": (c_count, c_money)}


c = Cup(50/100, 30/100, 100/100)
print(c.get_single_price(100))
"""
a : 50/100 * 50 * 100  = 2500
总使用量: 5000
b : 30/100 * 100 * 100 = 3000
总使用量:10000
c : 100/100 * 30 * 100 = 3000
总使用量:3000
总成本 = 8500
"""
print(c.get_sum_price(100))  # 计算100个水杯的总成本



