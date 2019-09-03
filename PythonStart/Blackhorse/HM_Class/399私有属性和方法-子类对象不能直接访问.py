# CLASS 399——400
class A():
    def __init__(self):
        self.num = 100
        # 私有属性
        self.__num2 = 200

    # 私有方法
    def __test(self):
        print("私有方法%d%d" % (self.num, self.num2))

    def test(self):
        print("父类的公有方法%s" % self.__num2)


class B(A):
    def demo(self):
        # 1.在子类的对象方法中，不能访问父类的私有属性(无法访问)
        ## print("访问父类的私有属性%d"%self.__num2)
        # 2.在子类的对象方法中，同样不能调用父类的私有方法
        ## self.__test()
        # 3.访问父类的共有方法
        # 子类 可以通过父类的共有方法间接访问到私有属性或私有方法
        print(self.num)
        self.test()


a = A()
print(a.num)
b = B()
b.demo()
