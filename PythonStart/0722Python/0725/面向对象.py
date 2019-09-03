# OOP面向对象
# 什么是面向对象
# 什么是类    什么是对象
#     整体和具体的关系
# 抽象和实例的关系
# 定义类
# class 类名（父名）：
#     def 方法（self）：
# 执行代码
class Person():
    def say(self):
        self.shenfen = '猴子'
        self.tixing = '大'
        self.diqu = '南美'
        self.age = 11
        print('%s的体型为%s，生活在%s,年龄为%d' % (self.shenfen, self.tixing, self.diqu, self.age))


p = Person()
p.say()

# p1 = Person()
# p1.say()
# p1.run()
# p1.play()

# class Man():
# #         self.name=" "
# #     def keywords(self):
# #         self.keyword=" "
# #     def character(self):
# #         self.xingge=" "
# #     return()

while True:
    class Computer():
        def tongji(self):
            self.count = 0

        def kaiji(self):
            self.count += 1
            print("Apple")

        def guanji(self):
            self.count += 1
            print("关机")

        def danji(self):
            self.count += 1
            print("单机")

        def yunxing(self):
            self.count += 1
            print("运行")

    # d = Computer()
    # if d.count == 10:


        


