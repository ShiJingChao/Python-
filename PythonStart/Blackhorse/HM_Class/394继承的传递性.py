# ClASS——394继承的传递性
# C类从B类继承，B类又从A类继承
# 那么C类就具有B类和A类的所有的属性和方法，子子孙孙无穷尽
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
class xiaotianquan(Dog):
    def fly(self):
        print("我是神犬，我会飞")
class xxtianquan(xiaotianquan):
    def gun(self):
        print("我会滚")
xiaotianquan = xxtianquan()
xiaotianquan.eat()
xiaotianquan.drink()
xiaotianquan.run()
xiaotianquan.sleep()
xiaotianquan.bark()
xiaotianquan.fly()
xiaotianquan.gun()