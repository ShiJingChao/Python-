# 1.西游记: 3个徒弟
# 类：父类：唐僧的徒弟
# name，age，吃饭，取经，
# 子类：
# 孙悟空：name，age，武器，吃饭，取经，除妖。。。
#
# 猪八戒：name，age，属性：字符串媳妇，吃饭，取经，牵马。。
#
# 沙和尚：name，age，属性：流沙河，吃饭，取经，挑行李。。。

# class Apprentice:   # 父类徒弟类
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         print("吃斋...")
#     def qj(self):
#         print("历经81难...")
# class Monkey(Apprentice):
#     def __init__(self,name,age,weapon):
#         super().__init__(name,age)
#         self.weapon = weapon
#     def cy(self):
#         print("%d岁的%s用%s除妖怪..." % (self.age,self.name,self.weapon))
# class Pig(Apprentice):
#     def __init__(self,name,age,wife):
#         super().__init__(name,age)
#         self.wife = wife
#     def qm(self):
#         print("妻子是%s的%d岁的%s牵着马..." % (self.wife,self.age,self.name))
# class Monk_sha(Apprentice):
#     def __init__(self,name,age,home):
#         super().__init__(name,age)
#         self.home = home
#     def txl(self):
#         print("家住%s的%d岁的%s挑着行李..." % (self.home,self.age,self.name))
#
#
# t1 = Monkey("孙悟空",18,"如意金箍棒")
# t1.eat()
# t1.qj()
# t1.cy()
# t2 = Pig("猪八戒",17,"高小姐")
# t2.eat()
# t2.qj()
# t2.qm()
# t3 = Monk_sha("沙和尚",16,"流沙河")
# t3.eat()
# t3.qj()
# t3.txl()


# 有三种动物：狗、猫、猪，
# 	父类：动物、
# 	子类：狗、猫、猪
#
# 	动物的属性：动物的名字
# 	动物的方法是eat（就是打印自己的名字）
# 有一个饲养员：饲养员
#
# 饲养员的方法：feed_animal(需要饲养的动物)
#
# 函数的实现是（其实就是调用动物的eat方法）

# class Feeder:
#     def __init__(self,name):
#         self.name = name
#     def feed_animal(self,animal_obj):
#         print("饲养员开始喂食了...")
#         animal_obj.eat()
#
# class Animals:
#     def __init__(self,name):
#         self.name =name
#     def eat(self):
#         print("%s要开始吃东西了..." % self.name)
# class Dog(Animals):
#     pass
#     # def eat(self):
#     #     print("%s吃狗粮..." % self.name)
# class Cat(Animals):
#     pass
#     # def eat(self):
#     #     print("%s吃猫粮..." % self.name)
# class Pig(Animals):
#     pass
#     # def eat(self):
#     #     print("%s吃湿垃圾..." % self.name)
#
# def func(obj):
#     if isinstance(obj,Animals):
#         obj.eat()
#     else:
#         print("没有这个宠物...")
#
# b = Feeder("饲养员")
# d = Dog("狗")
# c = Cat("猫")
# p = Pig("猪")
#
# b.feed_animal(d)
# b.feed_animal(c)
# b.feed_animal(p)
# func(d)
# func(c)
# func(p)


# 1.士兵突击
# 			1.士兵许三多有一把AK47
# 			2.士兵可以开火
# 			3.枪能够发射子弹
# 			4.枪装填子弹，增加子弹数量
# 士兵：类
# 	姓名
# 	开火()
#
# 许三多：对象
#
# 枪：类
# 	ak47：对象
# 	发射子弹()
# 	装子弹()
class Gun:
    def __init__(self,count):
        self.count = count
    def shoot(self):
        if self.count >=7:
            self.count -= 7
            print("哒哒哒~")
        else:
            print("没子弹了")
    def add_bullet(self,num):
        if self.count < 35:
            self.count = 35 if self.count + num >= 35 else self.count + num
        print("已装填子弹...当前子弹数量为：%d" % self.count)
class Soldier:
    def __init__(self,name,gun = None):
        self.name = name
        self.gun = gun
    def fire(self):
        if self.gun:
            self.gun.shoot()
        else:
            print("你还没有枪呢...")
    def add_gun_bullet(self,num):
        if self.gun:
            self.gun.add_bullet(num)
        else:
            print("没有枪...")
s = Soldier("许三多","AK-47A")
g = Gun(35)
s.gun = g
s.add_gun_bullet(10)
s.fire()
s.fire()
s.fire()
s.fire()
s.fire()
s.fire()



