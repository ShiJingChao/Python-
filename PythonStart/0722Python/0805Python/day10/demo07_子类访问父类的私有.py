"""
    子类访问父类的私有:
        私有: 只能在本类中使用, 类外不能使用; __私有

        * 子类不能访问父类的私有属性和私有方法;
        * 但是 子类可以通过父类的公有方法, 访问到父类的私有属性和方法;
"""

class Father:
    def __init__(self, name):
        self.name = name  # 父类的公有属性
        self.__age = 19  # 父类的私有属性

    def test1(self):
        print("我是父类的一个公有方法....")

    def __test2(self):
        print("我是父类的一个私有方法....")

    def test3(self):
        print("我是父类的公有方法,但是我是个叛徒...我大嘴巴告诉你私有年龄{}".format(self.__age))

    def test4(self):
        print("我是父类的公有方法,看我给你调用一下私有方法")
        self.__test2()


class Son(Father):

    def my_func(self):
        pass


s = Son("儿子")

print(s.name)
# print(s.__age)  AttributeError: 'Son' object has no attribute '__age'

s.test1()
# s.__test2() AttributeError: 'Son' object has no attribute '__test2'

s.test3()
s.test4()
