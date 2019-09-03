"""
    观察者模式:
        小喇叭: 一个人喊, 全村的人听;

    通知中心: 村长用喇叭喊
    观察者: 可以有n多个观察者, 一直在监听通知;
"""


# 通知中心(村长)
class Monitor:
    observer_list = []  # 观察者列表
    info = ""  # 通知的内容
    name = ""  # 名字

    def set_observer(self, obj):  # 绑定观察者, 参数:观察者对象
        Monitor.observer_list.append(obj)

    def show_info(self):  # 发布通知
        for observer in Monitor.observer_list:  # 遍历获取每一个观察者
            observer.receive_info()  # 调用观察者的接收信息的方法


# 观察者(村名)
class Student:

    def __init__(self, name, monitor):
        self.name = name
        self.monitor = monitor  # 通知中心

    def receive_info(self):
        print("接收方:{}, {}发布了通知, 通知的内容为:{}".format(self.name, self.monitor.name, self.monitor.info))


m = Monitor()
Monitor.info = "来来来,今天周测,周测时间是:19:30"
Monitor.name = "慢羊羊"

s1 = Student("喜洋洋", m)
s2 = Student("美羊羊", m)

m.set_observer(s1)
m.set_observer(s2)

m.show_info()



















