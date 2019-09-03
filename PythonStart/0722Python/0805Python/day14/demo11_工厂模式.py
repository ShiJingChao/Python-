"""
    工厂模式:
        根据不同的条件, 创建不同的实例对象;

        汽车父类;
        奥拓子类;
        奥迪子类;
        三蹦子子类;

        工厂类:
            方法: 传入不同的钱, 给你返回不同的汽车对象

        商场类:
            属性: 工厂对象
            方法: 卖小汽车; 通过工厂对象卖小汽车;
"""


class Car:
    def run(self):
        print("---吧啦吧啦跑---")

    def stop(self):
        print("---滋滋滋刹车---")


class AoTuo(Car):
    def run(self):
        print("---咣当咣当奥拓跑---")
    def stop(self):
        print("---zzzzzzzzz停---")


class AoDi(Car):
    def run(self):
        print("---噗噗噗奥迪跑----")
    def stop(self):
        print("---z~停---")


class SanBengZi(Car):
    def run(self):
        print("---刚刚刚刚三蹦子有劲儿的跑---")
    def stop(self):
        print("---z达z达~停---")


class Factory:
    def get_money(self, money):
        if money < 10:
            return AoTuo()
        elif money < 100:
            return AoDi()
        else:
            return SanBengZi()


class SuperMarket:
    def __init__(self, f_obj):  # 参数: 工厂对象
        self.f_obj = f_obj

    def sale_car(self, money):
        return self.f_obj.get_money(money)


f = Factory()
# obj = f.get_money(9)
# obj.run()
# obj.stop()

s = SuperMarket(f)
car = s.sale_car(115)
car.run()
car.stop()







