"""
        1. 创建对象的过程:p1 = Person()
            1. 开辟内存,存储对象
            2. 自动调用了init方法

        2. 实例变量:
            初始化实例变量, 初始化对象的属性;
            实例变量: 对象的变量 --> 对象属性;

            实例变量 归对象所有, 每个对象都有一份, 对象之间互不影响;
            self.变量名 --> 表示实例变量(实例属性)

        3. init
            默认情况下啥事也没干;
            一般情况下,会在init方法中初始化实例变量(对象的属性);

"""


class Person:  # 姓名, 年龄, 性别
    def __init__(self, name, age, sex):  # name=高科 age=100 sex=女
        # print("啦啦啦啦 高科啥时候来呀 啦啦啦啦")
        self.name = name  # name属性的值 = 高科
        self.age = age
        self.sex = sex


# 创建对象, 1,开辟内存; 2,自动调用init方法
p1 = Person("高科", 100, "女")
p2 = Person("吴钰铂", 38, "女")

print(p1.age, p1.name, p1.sex)
print(p2.age, p2.name, p2.sex)

p1.name = "高蝌蚪"
print(p1.name)
p2.age = 251
print(p2.age)






