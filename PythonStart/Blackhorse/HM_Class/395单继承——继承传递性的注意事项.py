class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")
class Dog(Animal):
    # 子类拥有父类所有的属性和方法
    def bark(self):
        print("汪汪叫")
class Cat(Animal):
    print("抓老鼠")
class xiaotianquan(Dog):
    def fly(self):
        print("我是神犬，我会飞")
xiaotianquan = xiaotianquan()

# 猫类继承动物类，但是xiaotianquan类并不能继承猫类（叔类不能继承）

