# 6 .编写Person类，类中属性需有：姓名name、年龄age两个属性,并且对这两个属性进行完全封装，提供构造方法与__str__方法
class Person:
    def __init__(self):
        self.name = "聪聪"
        self.age = 18

    def __str__(self):
        print(self.name, self.age)


per = Person()
per.__str__()
