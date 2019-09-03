"""
    抽象类:
        抽象类是一个特殊的类, 这个类只能被继承, 不能被实例化;
        python中使用抽象类是通过一个模块实现的;

        * 子类必须要实现父类中规定好的方法;

    1. 为甚么要有抽象类
        类: 对同一类事物抽象的描述;
        类是从一堆对象中抽取的相同的内容;
        抽象类是从一堆类中抽取的相同的内容;

        [举个栗子]:
            苹果类, 橘子类, 葡萄类...
            继承自水果类, eat()

        抽象类, 只能有抽象的方法, 没有实现的功能;
-------------------------
    关于支付功能的实现;
        微信支付;
        支付宝支付;
        qq支付;
        银联支付;
"""
from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):  # 抽象类需要继承自abc.ABCMeta   元
    @abstractmethod
    def pay(self):
        pass


class WeChat(Payment):
    def pay(self):
        print("微信支付的功能...")


class Bank(Payment):
    def pay(self):
        print("银联支付的功能....")


# p = Payment()  TypeError: Can't instantiate abstract class Payment with abstract methods pay

b = Bank()
b.pay()

w = WeChat()
w.pay()



