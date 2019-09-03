"""
    threading.local类, 使用这个类可以生成一个全局变量, 每个线程可以对他的属性进行读写, 互不影响;
            存啥取啥;
    解决了在线程中多次传递同一个参数的问题;
"""
from threading import Thread, current_thread,local
import time

local = local()  # 全局变量


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("{},吃吃吃...".format(self.name))

    def sleep(self):
        print("{},呼呼呼...".format(self.name))


# 人与动物说话, 并补充体力
def talkToAnimal():
    p_obj = local.person

    print("与动物说话的人的信息:", p_obj.name, p_obj.age)
    p_obj.eat()
    p_obj.sleep()


def func(name, age):  # 线程执行的任务
    # 创建人类的对象
    p = Person(name, age)
    local.person = p  # 给全局变量local 动态添加属性p
    # 让这个人类与动物说话
    talkToAnimal()


# 不给talkToAnimal传参, 让函数中能够访问到, func中创建好的p对象(人类对象), 通过全局变量


if __name__ == "__main__":
    t1 = Thread(target=func, args=("李小花", 20))
    t1.start()

    t2 = Thread(target=func, args=("李小黄", 18))
    t2.start()




