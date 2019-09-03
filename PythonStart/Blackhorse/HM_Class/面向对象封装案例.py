# CLASS——377——378封装
# 1.封装是面向对象编程的一大特点
# 2.面向对象编程的第一步——将属性和方法封装到一个抽象的类中
# 3.对象方法的细节都被封装在类的内部

# 需求：1.小明体重75kg
#       2.小明每次跑步会减肥0.5kg
#       3.小明每次吃东西体重增加1kg
# class Person:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#     def __str__(self):
#         return "我的名字叫%s，我的体重是%.2f kg" % (self.name, self.weight)
#
#     def run(self):
#         print("%s爱跑步，跑步锻炼身体" % self.name)
#         self.weight -= 0.5
#
#     def eat(self):
#         print("%s是吃货，吃完才有力气减肥" % self.name)
#         self.weight += 1
#
#
# xiaoming = Person("小明", 75.0)
# xiaoming.run()
# xiaoming.eat()
# print(xiaoming)

# CLASS——379扩展-多个对象属性之间互不干扰
# xiaomei = Person()
# xiaomei.run()
# xiaomei.eat()
# print(xiaomei)


# CLASS_380——381——382——383摆放家具-需求分析-被使用的类应该先开发
# 需求：1.房子（House）有户型，总面积和家具名称列表
#     ·新房子没有任何的家具
# 家具（HouseItem）有名字和占地面积，其中
# 席梦思（bed）占地4平米
# 衣柜（chest）占地2平米
# 餐桌（table）占地1.5平米
# 3.将以上三件家具添加到房子中
# 打印房子时，要求输出：户型，总面积，剩余面积，家具名称列表

# 应该先开发家具类，房子要使用到家具，被使用的类应该先开发

class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地%.2f 平米" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []

    def __str__(self):
        return ("户型%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加%s" % item)
        # 1.判断家具的面积
        if item.area > self.free_area:
            print("%s的面积太大了，无法添加" % item.name)
            return

        # 2.将家具的名称添加到列表中
        self.item_list.append(item.name)
        # 3.计算剩余面积
        self.free_area -= item.area


# 1.创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)

my_home = House("三室一厅", 200)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
