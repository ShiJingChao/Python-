# CLASS 384——385-386面向对象封装案例
# 1.封装是面向对象编程的一大特点
# 2.面向对象编程的第一个步——将属性和方法封装到一个抽象的类中
# 3.外界使用类创建对象，然后让对象调用方法
# 4.对象方法的细节都被封装在类的内部

# 一个对象的属性可以是另一个类创建的对象

# 01 士兵突击

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


class Soldier():
    def __init__(self, name):
        self.name = name
        self.gun = None


# 1.创建枪对象
ak47 = Gun("AK47")
ak47.add_bullet(50)
ak47.shoot()

tuoni = Soldier("托尼")
tuoni.gun = ak47
print(tuoni.gun)

# 386——创建初始化方法
# 开发士兵类
# 假设每一个新兵都没有枪
# 定义没有初始值的属性
# 在定义属性时，如果不知道设置什么初始值，可以设置为None
# None关键字表示什么都没有
# 可以表示一个空对象，没有方法和属性，是一个特殊的常量
# 可以将None赋值给任意一个变量

# fire 方法需求
# 1.判断是否有枪，没有枪没办法冲锋
# 2.喊一声口号
# 3.填装子弹
# 4.射击
