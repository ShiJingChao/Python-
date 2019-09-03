"""
    1. 类:  对同一类事物抽象的描述, 抽象的概念
            定义类的语法:
                class 关键字; 命名规则: 大驼峰StudentInfo;       (小驼峰studentInfo)

                class 类名:
                    pass
                    属性:  理解为用于描述类名词 (名字, 年龄, 颜色, 身高,...)
                    方法:  也叫做函数, 理解为类能够实现的行为功能(吃饭, 睡觉, 打豆豆,...)

    2. 对象: 真实存在的,类的具体的一个实例;
            对象 : 也叫做实例;
            创建对象的过程: 叫做类的实例化;
            ----------------
            对象.方法()
            获取对象的属性值: 对象.属性
            给属性赋值: 对象.属性 = 新值

            * 动态的给对象的属性赋值;
                类中没有定义该属性, 则在对象中给哪个对象的属性动态赋值, 只有该对象能使用此属性;

    3. self 自己, 本身
            谁调用谁就是self, self指的是当前调用的对象;
"""


class Cat:
    # 1. 定义一个方法: 抓耗子
    def catch_mouse(self):
        print("---- 抓到一只大耗子 ----")

    def show_me(self):
        print("--------show me-------%s" % self)


# 创建一个对象,
c1 = Cat()  # 创建对象的过程: 类的实例化;
print(c1)  # <__main__.Cat object at 0x0000000001DDE6C8>
print(type(c1))  # <class '__main__.Cat'>

print(type([]))  # <class 'list'>

c1.catch_mouse()  # 调用方法
c1.name = "小花猫"  # 给c1对象属性赋值
print(c1.name)  # 获取c1对象的属性值

print("----------------------")
c2 = Cat()
print(c2)
c2.catch_mouse()
# print(c2.name)  # AttributeError: 'Cat' object has no attribute 'name'

print("====================================")
print(c1)  # <__main__.Cat object at 0x00000000026C9688>
c1.show_me()  # --------show me-------<__main__.Cat object at 0x00000000026C9688>

print(c2)  # <__main__.Cat object at 0x00000000026C9708>
c2.show_me()  # --------show me-------<__main__.Cat object at 0x00000000026C9708>

# a = "abc"
# a.show_me()  不是cat类的对象不能调用cat类的方法

"""
1. 定义一个狗类:
    吃骨头, 摇尾巴, 看家
    名字, 颜色
    
2. 创建该类的两个对象,分别为:旺财,二黄
3. 打印对象, 打印对象的内存地址id()
"""

