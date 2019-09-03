"""
    单例:
        单个实例; 确保某个类只有一个实例存在;

    举例:
        1. 登录app, 当前的登录对象, 只能有一个;
        2.音乐播放器, 正在播放的歌曲类而言, 只能有一个实例;
"""
import my_util   # 被导入的模块会从头到尾执行一遍

o1 = my_util.a
o2 = my_util.a
o3 = my_util.a

print(o1)
print(o2)
print(o3)


class Person:
    __obj = None  # 单例

    def __new__(cls, *args, **kwargs):  # 创建实例对象 ---> 实例

        if not cls.__obj:
            cls.__obj = super().__new__(cls)
        return cls.__obj

    def __init__(self):  # 自己,本身; 谁调用谁就是self; 实际上,在调用init时, 实例对象已经被创建出来了;
        pass


p1 = Person()  # 1. 调用new方法,创建实例对象, 开辟内存空间, 存储对象   2. 自动调用init方法
p2 = Person()

print(p1)  # <__main__.Person object at 0x000000000269AA88>
print(p2)  # <__main__.Person object at 0x000000000269AA88>

# print(Person.__obj)












