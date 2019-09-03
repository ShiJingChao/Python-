# class Man:
#     def __init__(self, name):
#         self.name = name
#         self.__age = 18
#
#     def set_age(self, age):
#         self.__age = age
#         print(self.name, self.__age)
#
#
# m = Man("小聪")
# m.set_age(19)
#
#
# class Animals:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("吃吃吃")
#
#     def sleep(self):
#         print("一直睡")
#
#
# class Cat(Animals):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#         print(name, age, color)
#
#     def catch(self):
#         print("抓老鼠")
#
#     def eat(self):
#         print("吃猫粮")
#
#
# class Dog(Animals):
#     def look_door(self):
#         print("看门狗")
#
#
# c1 = Cat("尿尿", "1", "小黄")
#
# c1.eat()
# c1.sleep()
# c1.catch()

#
# 1.设计一个Game类："连连看"
# 	2.属性
# 		定义一个类属性：top_score,记录游戏的历史最高分
# 		定义一个实例属性：player_name，记录当前游戏的玩家姓名
# 	3.方法
# 		静态方法：show_help显示游戏帮助信息
# 		类方法：show_top_score，显示历史最高分
# 		实例方法：start_game，开始当前玩家的游戏
# 	4.主程序的步骤
# 		1) 查看帮助信息
# 		2) 查看历史最高分
# 		3) 创建游戏对象，调用方法
import random


class Game:
    top_score = 0

    def __init__(self, play_name):
        self.play_name = play_name

    def start_game(self):
        score = random.randint(1, 101)
        if score > self.top_score:
            Game.top_score = score
            print("您是最高分：%d" % score)
        else:
            print("您本次的分数为：%d" % score)
    @classmethod
    def get_top_score(cls):
        print("历史最高分：%d" % cls.top_score)
    @staticmethod
    def show_help():
        print("欢迎来到玩家系统...")

if __name__ == "__main__":
    Game.show_help()
    Game.get_top_score()
    g = Game("小聪")
    g.start_game()
    g.get_top_score()
