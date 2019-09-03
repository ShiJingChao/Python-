"""
1.设计一个Game类："连连看"
	2.属性
		定义一个类属性：top_score,记录游戏的历史最高分
		定义一个实例属性：player_name，记录当前游戏的玩家姓名
	3.方法
		静态方法：show_help显示游戏帮助信息
		类方法：show_top_score，显示历史最高分
		实例方法：start_game，开始当前玩家的游戏
	4.主程序的步骤
		1) 查看帮助信息
		2) 查看历史最高分
		3) 创建游戏对象，调用方法
"""
import random


class Game:
    top_score = 0
    def __init__(self, player_name):
        self.player_name = player_name

    def start_game(self):
        score = random.randint(1, 101)
        if score > Game.top_score:
            Game.top_score = score
            print("恭喜您打破了记录, 分数为{}".format(score))
        else:
            print("您本次的分数为{}".format(score))

    @classmethod
    def get_top_score(cls):
        print("历史最高分:{}".format(cls.top_score))

    @staticmethod
    def show_help():
        print("欢迎来到玩家系统...")


if __name__ == "__main__":
    Game.show_help()
    Game.get_top_score()
    g = Game("肖战")
    g.start_game()
    g.get_top_score()

















