class Car(object):
    def __init__(self, color, brand, texture, torsion):
        self.color = color
        self.brand = brand
        self.texture = texture
        self.torsion = torsion

    def __str__(self):
        return "颜色：%s,品牌：%s,材质：%s,扭力：%s" % (self.color, self.brand, self.texture, self.torsion)


class Kache(Car):
    def run(self):
        print("卡车可以拉货")


class Taxi(Car):
    def fds(self):
        print("可以自驾游")


c = Kache("红色", "金杯", "钢", "200扭")
print(c)
c.run()

d = Taxi("白色", "速腾", "碳纤维", "300扭")
print(d)
d.fds()
