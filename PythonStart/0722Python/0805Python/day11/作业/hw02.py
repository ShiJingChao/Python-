"""
1.士兵突击
			1.士兵许三多有一把AK47
			2.士兵可以开火
			3.枪能够发射子弹
			4.枪装填子弹，增加子弹数量
士兵：类
	姓名  属性
	开火()  方法
    许三多：对象

枪：类
	ak47：对象
	子弹数量 --> 属性
	发射子弹()  方法
	装子弹()  方法

if "":
if []:
if {}:
if ():
if None:
if 0:
if (0):  # (0) == 0; (0,)-->元组; 0, --> 元组
以上都可以当做 if False:

if "0":
if (0,):
以上数据类型中只要有内容,不是空,则当做True使用
"""


class Gun:
    def __init__(self, count):
        self.count = count  # 子弹数量

    def shoot_bullet(self):  # 发射子弹
        if self.count > 0:
            self.count -= 1  # 子弹数量减少
            print("发射子弹...PiuPiuPiu...")
        else:
            print("赶紧跑吧..乌拉乌拉...")

    def add_bullet(self, num):  # 最多容纳35颗子弹; 参数num : 装的子弹的数量
        if self.count < 35:
            # 需求,装子弹, 最多35颗, 不到35颗也能装; 三元运算符;
            self.count = 35  if self.count + num >= 35 else self.count + num
            print("当前子弹数量为 : %d" % self.count)
            # if self.count + num >= 35:
            #     self.count = 35
            # else:
            #     self.count += num
        else:
            print("弹夹已满,憋装了...")


class Solder:
    def __init__(self, name, gun=None):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun:   # 有, obj;  没有: None  if None--> if False
            # 有枪, 调用枪的方法进行射击....
            self.gun.shoot_bullet()
        else:  # 没有枪
            print("没枪也敢挑事, 你以为你是小黄???")

    def add_gun_bullet(self, num):  # 参数: 子弹的数量
        if self.gun:
            self.gun.add_bullet(num)
        else:
            print("你目前还木有枪...")


g = Gun(30)
s = Solder("许三多", g)
s.fire()
s.add_gun_bullet(10)


