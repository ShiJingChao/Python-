"""
3.手机作为类：
	属性：品牌，型号
	方法：show_info()显示自己的属性信息，打电话()
"""


class MobilePhone:

    def __init__(self, brand, model, tel):
        self.brand = brand
        self.model = model
        self.tel = tel  # 电话号码

    def show_info(self):
        print("我是{}品牌{}型号的新型移动手机"
              .format(self.brand, self.model))

    def call_phone(self, mobile_obj):  # 参数,被呼叫的手机对象
        print("呼叫方为: %s" % self.tel)
        print("被呼叫方为: %s" % mobile_obj.tel)
        print("嘟..嘟..嘟...")


m1 = MobilePhone('华为', '鸿蒙', '18010047927')
m2 = MobilePhone('小米', 'readme', '13366669780')

m1.show_info()
m2.show_info()

m1.call_phone(m2)











