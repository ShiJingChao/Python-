"""
2.银行卡作为类，
	属性：账户名，余额
	方法：存款，取款，转账(转账就是给其他银行卡转账)
"""


class BankCard:
    def __init__(self, name, money):
        self.account  = name
        self.price = money

    def save_money(self, money):  # 参数:存款钱数
        self.price += money
        print("尊敬的{}用户,您好,本次存款{:.2f}元,账户余额为{:.2f}元".format(self.account, money, self.price))

    def get_money(self, money):  # 参数: 取款金额
        if self.price >= money:
            self.price -= money
            print("尊敬的{}用户,本次取款金额为{:.2f}元,账户余额为{:.2f}元".format(self.account, money, self.price))
        else:
            print("尊敬的{}用户,您的账户余额不足,不能完成本次操作".format(self.account))

    def change_money(self, money, bank_obj):  # 转账金额, 转账账户(银行卡对象)
        if self.price >= money:
            self.price -= money  # 当前对象, 余额减少
            bank_obj.price += money  # 被转账账户, 余额增加

            print("尊敬的{}用户,您此次向{}用户,转账{:.2f}元,您的账户余额为{:.2f}元"
                  .format(self.account, bank_obj.account, money, self.price))
        else:
            print("尊敬的{}用户,您的账户余额不足,不能完成本次操作".format(self.account))


b1 = BankCard("小黄", 1000)
b2 = BankCard("小黄花", 1200)

b1.get_money(10)  # 取款
b1.save_money(100)  # 存款
b1.change_money(1000, b2)  # 转账

print(b2.price)  # 获取b2对象的余额
