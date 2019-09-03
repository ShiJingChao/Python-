class Women():
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s的年龄是%d" % (self.name, self.__age))


xiaomei = Women("小美")
# 私有属性，在外界不能被直接访问
# print(xiaomei.__age)
# 私有方法，同样不允许在外界直接调用
# xiaomei.secret()

# CLASS 390 伪私有属性和方法
# 在日常开发中，不要用这种方式，访问对象的私有属性或私有方法
# Python中并没有真正意义的私有
# 在给属性和方法命名时，实际是对名称做了一些特殊处理，使得外界无法访问到
# 处理方式：在名称前面加上 _类名=> _类名__名称
# 伪私有属性
print(xiaomei._Women__age)
# 伪私有方法
xiaomei._Women__secret()