"""
    多继承:
        子类具有多个父类的情况; 子类可以继承多个父类的功能;

        python: (继承的传递)
            多层继承: 子类 --> 父类 --> 爷爷类 --> 祖先类 ---> object类

"""


class A:
    def func1(self):
        print("我是A中func1中的方法...")


class B(A):
    def func2(self):
        print("我是B中的func2的方法...")

    # def func1(self):
    #     print("我是B中的func1的方法...")


class C(B):
    def func3(self):
        print("我是C中的func3的方法...")


# b = B()
# b.func1()

c = C()  # C --> B --> A --> object
c.func3()  # 我是C中的func3的方法...
c.func2()  # 我是B中的func2的方法...
c.func1()  # 我是A中func1中的方法...
