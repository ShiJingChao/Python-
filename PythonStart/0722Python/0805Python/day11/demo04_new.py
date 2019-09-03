"""
    __new__(cls):  类方法
            实例化的魔术方法;
            触发时机: 当实例化对象的时候,会被自动调用;

            功能: 实例化一个对象;
            返回值: 实例化的那个对象;

            __new__(cls)方法将实例化的对象传递给__init__(self)方法的第一个参数;

    * __new__()是object类底层的实现, 单例;
"""


class Person:
    def __new__(cls, *args, **kwargs):  # 必须有返回值: 创建好的对象,类的实例;
        print("我是一个new方法...")
        return super().__new__(cls)

    def __init__(self):
        print("我是一个init方法...")


p = Person()  # 创建对象
print(p)  # None

