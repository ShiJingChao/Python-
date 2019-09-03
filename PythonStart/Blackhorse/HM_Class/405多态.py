# CLASS-405-406
# 基本概念
# 多态 不同的子类对象调用相同的父类方法，产生不同的执行结果
# 多态可以增加代码的灵活度
# 以继承和重写父类方法为前提
# 是调用方法的技巧，不会影响到类的内部设计


class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s蹦蹦跳跳的玩耍" % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s上天玩去" % self.name)


class Person:
    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        print("%s和%s快乐的玩耍。。。" % (self.name, dog.name))
        dog.game()

# 创建一个狗对象
# dog = Dog("尿尿")
dog = XiaoTianDog("粑粑")
# 在程序执行时，传入不同的狗对象 实参，就会产生不同的执行效果
# 创建一个人对象
person= Person("王小二")
# 让人和狗玩
person.play_with_dog(dog)



