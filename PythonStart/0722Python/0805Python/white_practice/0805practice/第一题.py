# 1老头 练习：员工类练习：
# 程序员类：属性（姓名、工号、工资、奖金），行为（工作：软件开发）
# 测试工程师类：属性（姓名、工号、工资），行为（工作：软件测试）
# 项目经理类：属性（姓名、工号、工资、奖金），行为（工作：控制进度）
class Programmer:
    def __init__(self, name, id, money, mmoney):
        self.name = name
        self.id = id
        self.money = money
        self.mmoney = mmoney
        print("{}的工号为：{}，工资为{}，奖金为{}".format(self.name, self.id, self.money, self.mmoney))

    def work(self):
        print("软件开发工作")


class Test_engineer(Programmer):
    def work(self):
        print("软件测试")


class Pm(Programmer):
    def work(self):
        print("控制进度")


peison = Programmer("小王", "1", "1", "1")
peison.work()
kaifa = Test_engineer("小李", "2", "2", "2")
kaifa.work()
ceshi = Test_engineer("小赵", "3", "3", "3")
ceshi.work()
