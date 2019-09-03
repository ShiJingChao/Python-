# CLASS-415-案例分析
# 需求
# 1.设计一个Game类
# 2.属性：
# 定义一个类属性 top_score记录游戏的历史最高分
# 定义一个实例属性play_name记录 当前游戏的玩家姓名
# 3.方法
# 静态方法：show_help显示游戏帮助信息
# 类方法：show_top_score显示历史最高分
# 实例方法：start_game开始当前玩家的游戏

# 4.主程序步骤：
# 1）查看帮助信息
# 2）查看历史最高分
# 3）创建游戏对象，开始游戏
#CLASS-417 演练
class Game:
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    # 静态方法
    @staticmethod
    def show_help():
        print("帮助信息:让僵尸进入大门")

    # 类方法
    @classmethod
    def show_top_score(cls):
        print("历史记录%d" % cls.top_score)

    # 实例方法
    def start_game(self):
        print("%s开始游戏了》》》" % self.player_name)


# 1.查看游戏的帮助3信息
Game.show_help()
# 2.查看历史最高分
Game.show_top_score()
# 3.创建游戏对象
game = Game("小明")
game.start_game()

# CLASS 417 确定方法类型的套路
# 1.实例方法——方法内部需要访问实例属性
# 实例方法内部可以使用类名.访问类属性
# 类方法——方法内部 只 需要访问类属性
# 静态方法——方法内部，不需要访问实例属性和类属性
