# CLASS 391
# 继承
# 面向对象三大特征
# 1.封装根据职责将属性和方法封装到一个抽象的类中
# 2.继承 实现代码的重用 相同的代码不需要重复的编写
# 3.多态 不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活度
# CLASS 392
# 一. 单继承
# 继承的概念：子类拥有父类所有的方法和属性
# 继承的语法：
# class 类名（父类名）：
#       pass
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
# 子类继承自父类，可以直接享受父类中已经封装好的方法
# 子类中应根据职责，封装子类特有的属性和方法
wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
# CLASS--393继承的相关术语——继承和派生
# Dog类是Animal类的子类，Animal类是Dog类的父类，Dog类从Animal类继承
# Dog类是Animal类的派生类，Animal类是Dog类的基类，Dog类从Animal类派生






