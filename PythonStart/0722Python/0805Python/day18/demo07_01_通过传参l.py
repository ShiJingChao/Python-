"""
    需求:
"""
from threading import Thread


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("{},吃吃吃...".format(self.name))

    def sleep(self):
        print("{},呼呼呼...".format(self.name))


# 人与动物说话, 并补充体力
def talkToAnimal(p_obj):
    print("与动物说话的人的信息:", p_obj.name, p_obj.age)
    p_obj.eat()
    p_obj.sleep()


def func(name, age):
    # 创建人类的对象
    p = Person(name, age)
    # 让这个人类与动物说话
    talkToAnimal(p)

# 不给talkToAnimal传参, 让函数中能够访问到, func中创建好的p对象(人类对象), 通过全局变量

if __name__ == "__main__":
    t1 = Thread(target=func, args=("李小花", 20))
    t1.start()

    t2 = Thread(target=func, args=("李小黄", 18))
    t2.start()




