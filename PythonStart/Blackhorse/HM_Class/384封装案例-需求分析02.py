class Gun:
    def __init__(self, model):
        # 1.枪的型号
        self.model = model
        # 2.子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("%s没有子弹，请加子弹" % self.model)
        self.bullet_count -= 1
        print("%s哒哒哒，剩余子弹%d" % (self.model, self.bullet_count))


# 创建战士
class Soldier():
    def __init__(self, name):
        # 1.姓名
        self.name = name
        # 2.新兵没有枪
        self.gun = None

    def fire(self):
        # 1.判断士兵是否有枪
        if self.gun is None:
            print("%s还没有枪" % self.name)
            return
        print("%s冲啊" % self.name)
        # 2.让枪装子弹
        self.gun.add_bullet(50)
        # 3.开火
        self.gun.shoot()


# 1.创建枪对象
# ak47 = Gun("AK47")
# tuoni = Soldier("托尼")
# tuoni.gun = ak47
# print(tuoni.gun)


jiatelin = Gun("加特林")
jiesen = Soldier("杰森")
jiesen.gun = jiatelin
jiesen.fire()
print(jiesen.gun)
