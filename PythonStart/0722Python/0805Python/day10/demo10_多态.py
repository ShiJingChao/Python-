"""
   多态:
        多种形态;
        1. 以继承和重写为前提, 形参为父类对象, 执行时, 由具体的对象执行相应的方法
        2. 非继承关系, 形参为对象, 执行时, 由具体的对象执行相应的方法

    python讲究鸭子类型:
        如果一只鸟, 长得像鸭子, 叫起来像鸭子, 走路也像鸭子, 那么我们就可以把他当做鸭子

"""


class Father:
    def say(self):
        print("老父亲喊你回家吃饭啦....")


class Son(Father):  # 子类继承自父类
    def say(self):   # 子类中重写父类的方法
        print("作为儿子, 我饿了, 我要主动回家吃饭啦...")


def func(obj):  # obj 是一个对象
    if isinstance(obj, Father):  # 判断obj是否是Father类的对象
        obj.say()
    else:
        print("不是父亲和儿子..憋张嘴...")


f = Father()
s = Son()

func(f)
func(s)  # 作为儿子, 我饿了, 我要主动回家吃饭啦...


class Duck:
    def say(self):
        print("嘎嘎..嘎嘎嘎...")


def func2(obj):  # obj 是一个对象
    obj.say()


d = Duck()
func2(d)  # 调用函数, 传参为鸭子类对象  嘎嘎..嘎嘎嘎...
func2(f)  # 调用函数, 传参为父亲类对象  老父亲喊你回家吃饭啦....
func2(s)  # 调用函数, 传参为儿子类对象  作为儿子, 我饿了, 我要主动回家吃饭啦...








