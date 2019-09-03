"""
    读取文件
        read() : 不传参--> 默认读取文件中的所有内容
                 参数: 读取的字符的个数, 读取指定个数的字符
                 * 换行,标点等也是一个字符;


        [注]: 同一个文件对象, 多次调用读取方法, 从上次读取结束的位置,继续向后读取数据;

        readline() : 读取一行;
        readlines() : 一次性读取所有的行, 返回值为list;

        for..in f : 获取文件中的每一行的内容;
                open()返回一个文件句柄对象(其本身是一个可迭代对象);
"""

f = open(r"D:\first_level\day13\inner\pizza.txt")

# print(f.read(3))  # 药药!
# print(f.read(3))  # 切克闹
# print(f.read(2))  # !\n
#
# print(f.readline())
# print(f.readline())

# res = f.readlines()
# print(res)
"""
['喜欢脆的多放面！\n', '辣椒腐乳小葱花！\n', '铁板铁铲小木刷！\n', '药药！切克闹！\n', '放点面酱些许甜！\n', '趁热吃了似神仙！\n', '艾瑞巴蒂！黑喂够！\n', '跟我一起来一套！\n', '动词大慈动词！\n', '我说煎饼你说要！\n', '“煎饼”“要”“煎饼”“要”切克闹切克闹！\n', '金黄喷香好味道！\n', '药！药！切客闹！\n', '卡姆昂北鼻沟！\n', '动词大慈动动大慈动词大慈动动大慈！\n', '是谁在唱歌！动词大慈！\n', '温暖了寂寞！动词大慈！\n', '白云悠悠蓝天依旧！动动大慈！\n', '药！药！药！药药！黑为够！~切克闹切克闹！']"""

for x in f:
    print(x)

f.close()

# 读取message.txt中的内容,世界杯的信息, 键盘上输入年份, 输出对应的举办地和冠军国
# 如果输入的年份没有举办, 则输出没有举办

file = open("message.txt")

line_list = file.readlines()  # ["2002|韩国|日本", "", "", ...]

year = input("请输入一个年份:")

for this_year in line_list:  # "2002" --> "2002|韩国|日本"
    if this_year.startswith(year):
        res = this_year.split("|")  # ["2002", "韩国", "日本"]
        print("举办地:", res[1])
        print("冠军国:", res[-1])
        break

    # if year in this_year:
    #     index = this_year.rfind("|")  # "2002|韩国|日本"
    #     print("冠军国:", this_year[index+1:])
    #     print("举办地:", this_year[5:index])
    #     break

file.close()



