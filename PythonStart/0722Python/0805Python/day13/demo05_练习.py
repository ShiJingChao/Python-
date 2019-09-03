import time
# 1. 通过程序创建一个alpha.txt的文件, 将26个英文字母写在里边, 不要划拉键盘

def write_alpha():
    f = open("alpha.txt", "w")
    s = ""
    for x in range(65, 91):  # 65-90/ 97-122
        s += chr(x)
    f.write(s)
    f.close()

write_alpha()


# 2. 写一首诗, 每句换行
def poem():
    s = "\n鹅鹅鹅\n曲项向天歌\n白毛浮绿水\n红掌拨清波"
    f = open("alpha.txt", "w")
    f.write(s)
    f.close()

poem()


# 3. 模拟聊天记录, 循环通过键盘输入, 俩人, 将俩人的对话保存在chat.txt中
# 小花说: 用户输入说话的内容....
# 二狗说: ....
# 小花说: .....
# 二狗说: ....
# 小花说: 用户没有输入 直接回车
# 二狗说: 用户没有输入 直接回车
# 聊天结束, 将以上存在chat.txt中; 并记录聊天的日期和时间: 2019-08-21 14:12:38


def chat():
    f = open("chat.txt", "a")
    # 获取当前时间 --> 时间元组 2019-08-21 14:47:03
    t = time.localtime()
    time_str = time.strftime("%Y-%m-%d %H:%S:%M", t)
    f.write(time_str)  # 记录本次聊天的起始时间
    f.write('\n')  # 来个空格
    while True :
        p1 = input("小花说:")  # ""
        p2 = input("二狗说:")  # ""

        if not p1 and not p2:  # 如果小花也没有说, 二狗也没有说, 则聊天结束
            f.close()
            print("___聊天结束___")
            break
        else:
            p1_str = "小花说: " + p1 + "\n"
            p2_str = "二狗说: " + p2 + "\n"
            f.writelines([p1_str, p2_str])  # 记录小花二狗的聊天内容


chat()






