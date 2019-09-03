# 在开发中，子类的方法实现中包含父类的方法实现
# 父类原本封装的方法实现是子类方法的一部分
# 就可以使用扩展的方式
# 1.在子类中重写父类的方法
# 2.在需要的位置使用super（）.父类方法来调用父类方法的执行
# 3.代码其他的位置针对子类的需求，编写子类特有的代码实现

# 关于super
# 在python中super是一个特殊的类
# super（）就是使用super类创建出来的对象
# 最常使用的场景就是在重写父类方法时，调用在父类中封装的方法的实现
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
    def bark(self):
        # 针对子类特有的需求，编写代码
        print("我是神狗，我会飞")
        # 使用super（），调用原本在父类中封装的方法
        super().bark()
        # Animal.run(self)
        # 增加其他子类的方法
        print("我会腾云")


xtq = xiaotianquan()
xtq.bark()

# CLASS 397——398
# 调用父类方法的另一种方式
# 在python 2.x时，如果需要调用父类的方法，还可以使用下种方法
# 父类名.方法(self)(写在子类中) 这种方式在python 3.x还支持
# 这种方法不推荐，因为一旦父类发生变化，方法调用位置的类名同样需要修改
# 在开发时，父类名和super()两种方式不要混用