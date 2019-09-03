"""
    1. 写一个类, 这个可以记录产生对象的个数
    2. 写个游戏类:
            1. 记录历史最高分
            2. 传入当前玩家姓名, 随机玩家分数
            3. 获取历史最高分
"""
import random

class Person:
    count = 0   # 不可变数据类型的类属性, 记录产生对象的个数
    def __init__(self):
        Person.count += 1


p1 = Person()
p2 = Person()
p3 = Person()
print(p2.count)


class Game:
    history_score = 0
    def play_game(self, name):
        score = random.randint(1, 100)
        print("尊敬的%s, 得分为%d!!!" % (name, score))
        if score > Game.history_score:  # 如果此次游戏所得分数>历史最高分
            Game.history_score = score  # 更新历史最高分

    def get_history_score(self):
        print("历史最高分为:%d" % self.history_score)


g = Game()
g.play_game("永登高峰")  # 尊敬的永登高峰, 得分为92!!!
g.play_game("永登高峰")
g.play_game("永登高峰")
g.play_game("永登高峰")
g.play_game("永登高峰")
g.play_game("永登高峰")
g.get_history_score()



