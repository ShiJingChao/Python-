"""
    策略模式:
        达到某个目标, 有多种不同的方式, 这些方式都有可能会使用到;
        具体使用哪种方式, 根据需求来定;

"""

# 通知客户搞活动, 发邮件, 发短信;

# 发送信息的父类
class Msg:  # 信息的内容, 联系方式, 发送的方法
    def __init__(self, info, way):
        self.info = info
        self.way = way  # 1336669999 lixiaohua@offcn.com

    def send(self):
        pass


# 发邮件
class Email(Msg):
    def send(self):
        return "用邮件的方式, 给{}发送活动信息: {}".format(self.way, self.info)


# 发短信
class ShortMsg(Msg):
    def send(self):
        return "用短信的方式, 给{}发送活动信息: {}".format(self.way, self.info)


class Customer:
    def __init__(self, name, tel, email):
        self.name = name
        self.tel = tel
        self.email = email
        self.receive_way = None  # 接收信息的方式

    def receive_info(self):
        return self.receive_way.send()

    def set_receive_way(self, obj):  # 设置接收信息的方式  obj可能是邮件对象, 也有可能是短信对象
        self.receive_way = obj


customer = Customer("李小花", "13366669999", "lixiaohua@offcn.com")

email = Email("本店周年庆,买一送一(双鞋带)", customer.email)
short_msg = ShortMsg("本店周年庆,买一送一(双鞋带)", customer.tel)

customer.set_receive_way(short_msg)  # 设置接收信息的方式就是短信
print(customer.receive_info())













