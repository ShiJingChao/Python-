# CLASS 401 多继承
# 子类可以拥有多个父类 并且具有所有父类的属性和方法
# 例如孩子汇集成自己父亲和母亲的特性

# class A:
#     def test(self):
#         print("test 方法")
#
#
# class B:
#     def demo(self):
#         print("demo方法")
#
#
# class C(A, B):
#     '''多继承可以让子类对象，同时具有多个父类的属性和方法'''
#     pass
#
#
# # 创建子类对象
# c = C()
# c.test()
# c.demo()

# CLASS 402 多继承的使用注意事项
# 如果不同的父类中存在同名的方法，开发时    ，应该尽力那个避免这种容易产生混淆的情况！
# 如果父类之间存在同名的属性或者方法，应该尽量避免使用多继承

class A:
    def test(self):
        print("A---test 方法")

    def demo(self):
        print("A---demo方法")


class B:
    def demo(self):
        print("B---demo方法")

    def test(self):
        print("B---test 方法")


class C(B, A):
    '''多继承可以让子类对象，同时具有多个父类的属性和方法'''
    pass


# 创建子类对象
c = C()
c.test()
c.demo()

# CLASS 403 MRO方法搜索顺序
# Python中的内置属性MRO(method resolution order)——方法搜索顺序
# __mro__ 可以查看方法搜索顺序
# 主要用于在多继承时 判断方法、属性的调用路径

# 确定C类对象调用方法的顺序
print(C.__mro__)

# CLASS 404 新式类和旧式（经典）类

# object是Python为所有对象提供的基类，提供一些内置的方法和属性，可以使用dir查看
# 新式类：以object为基类的类，推荐使用
# 经典类：不以object为基类的类，不推荐使用
# 在Python 3.x 中没有指定父类，默认使用object作为该类的基类
# 在Python 2.x 中定义类，如果没有指定父类，不会以object作为基类
# 新式类和经典类在多继承时——会影响到方法的搜索顺序