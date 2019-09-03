"""
    1. 定义一个圆类, 可以计算该圆的周长和面积
"""
class Circle:
    def __init__(self, r):
        self.r = r  # 属性: 半径

    def get_perimeter(self): # 周长
        return 2 * 3.14 * self.r

    def get_area(self): # 面积
        return 3.14 * self.r * self.r


c1 = Circle(1)  # 创建对象, 自动调用init, 给属性赋值
print(c1.get_perimeter())
print(c1.get_area())  # self.r


# 1. 奔跑吧兄弟:
# 奔跑: 每跑一次步, 掉肉2.5斤
# 吃: 没吃一顿饭, 涨3斤肉
class RuningMen:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        if self.weight > 2.5:
            self.weight -= 2.5
            print("%s,你此刻的体重为%.1f" % (self.name, self.weight))
        else:
            print("%s,可不能在跑了,再跑的话,骨灰都没了" % self.name)

    def eat(self):
        self.weight += 3
        print("%s, 恭喜您此刻体重为%.1f" % (self.name, self.weight))


r1 = RuningMen("迪丽热巴", 90)
r1.eat()
r1.eat()
r1.eat()
r1.run()
r1.eat()
r1.run()


# 2. 公路和汽车类, 计算车在公路上行走完的时间
# 分析: 时间 = 路程 / 速度
# 路程: 公路的长度  --->  长度(名词)
# 速度: 汽车的速度  --->  速度(名词)
#           功能: 计算车在公路上行走完的时间
class Road:
    def __init__(self, length, name):
        self.name = name
        self.length = length

    def get_time(self, car_obj):  # 形参:本质变量  car_obj 小汽车对象
        t = self.length / car_obj.v
        print("%s小汽车在%s公路上行驶完全程的时间是%.2f" % (car_obj.brand, self.name, t))


class Car:
    def __init__(self, v, brand):  # 属性v, 代表速度
        self.v = v
        self.brand = brand  # 汽车品牌

    def get_time(self, road_obj):  # 形参: 公路对象
        t = road_obj.length / self.v
        print("%s小汽车在%s公路上行驶完全程的时间是%.2f" % (self.brand, road_obj.name, t))


road1 = Road(100, "康庄大道")
car1 = Car(300, "奥拓")

road1.get_time(car1)  # 奥拓小汽车在康庄大道公路上行驶完全程的时间是0.33
car1.get_time(road1)  # 奥拓小汽车在康庄大道公路上行驶完全程的时间是0.33


# 3. 装修房子娶媳妇
# 房子类 平米数, 2000, 60
# 家具类 占地面积; 床 沙发 桌子
# 查看可以往房子里放多少家具,以及剩余平米数
class House:
    def __init__(self, area):
        self.area = area   # 房子总共的平米数
        self.free_area = area  # 剩余面积的初始值为总面积
        self.f_list = []   # 家具列表

    def add_furniture(self, f_obj):  # 参数: 所放置的家具
        if self.free_area >= f_obj.f_area:
            self.free_area -= f_obj.f_area
            self.f_list.append(f_obj)
            print("%s, 可以放, 该家具面积为%d, 此时剩余面积为%d" % (f_obj.name, f_obj.f_area, self.free_area))
        else:
            print("%s, 该家具面积%d, 剩余面积%d, 没地了, 放不下" % (f_obj.name, f_obj.f_area, self.free_area))

    def get_furniturn_name(self):  # 获取房子中每个家具的名字
        for f_obj in self.f_list:
            print(f_obj.name)


class Furniture:
    def __init__(self, name, f_area):
        self.name = name  # 家具的名字
        self.f_area = f_area  # 家具的占地面积


bed = Furniture("床", 20)
cabinet = Furniture("柜子", 10)
desk = Furniture("桌子", 45)
bookshelf = Furniture("书架", 50)

h1 = House(100)
h1.add_furniture(bed)  # 实参: 确定了家具是床
h1.add_furniture(cabinet)
h1.add_furniture(desk)
h1.add_furniture(bookshelf)
print("剩余面积:", h1.free_area)
print("总平米数", h1.area)
h1.get_furniturn_name()


# 4. 狙击手开枪打敌人,砰砰砰PiuPiuPiu
# 枪类
# 狙击手类
# 功能: 有子弹,开火;没子弹,开跑...
# 对象1: 人(狙击手) --> sniper类
# 对象2: 枪 --> gun类

class Sniper:  # 狙击手类
    def __init__(self, gun=None):
        self.gun = gun   # 枪, 枪类对象

    def fire(self):
        if self.gun:        # 有没有枪
            if self.gun.count == 0:  # 枪里有木有子弹
                print("快跑吧..没子弹...")
            elif self.gun.count == 1:
                self.gun.shooting()  # 发射子弹
                print("就这一发子弹了, 打完赶紧跑吧...")
            else:
                self.gun.shooting()  # 发射子弹
                print("开枪...PiuPiuPiu...")
        else:
            print("别打了, 没有枪, 快跑吧 .....")

    def add_gun_bullet(self):  # 人添加子弹
        self.gun.add_bullet()


class Gun:  # 枪类
    def __init__(self, count):
        self.count = count  # 子弹的数量

    def add_bullet(self):
        self.count = 10
        print("子弹已装满, 请全速前进....")

    def shooting(self):  # 射击
        self.count -= 1


g = Gun(2)
p = Sniper()
p.fire()
p.gun = g
p.fire()  # 2
p.fire()  # 1
p.fire()  # 0
p.add_gun_bullet()


