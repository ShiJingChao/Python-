# 方法的重写——覆盖父类方法，重写子类方法
# 子类拥有父类的所有的方法和属性
# 子类继承自父亲，可以直接享受父类中已经封装好的方法，不需要再次开发
# 当父类的方法实现不能满足子类需求时，可以对方法进行重写（override）

# 覆盖父类方法有两种情况：
# 1.覆盖父类的方法
# 2.对父类方法进行扩展
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
        print("我是神狗，我会飞")
# 覆盖父类的方法
# 1.如果在开发中，父类的方法实现和子类的方法实现，完全不同
# 就可以使用覆盖的方式，在子类中重新编写父类的方法实现
# 具体的实现方式，在子类中重新编写父类的方法实现
    # 就是相当于在子类中，定义了一个和和父类同名的方法并且实现
    # 重写之后，在运行时，只会调用子类中重写的方法，而不再会调用父类封装的方法

    def bark(self):
        print("嘤嘤嘤")

xtq = xiaotianquan()
xtq.bark()


