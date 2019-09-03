# 漂流瓶
# 用户可以扔瓶子，每天最多扔5个瓶子，每个瓶子的内容不得超过20个字符，
# 如果超过20个字符，提示超过20个字符，请重新输入
# 将瓶子保存在文本文档里，每个文本文档是一个瓶子，并且以时间命名，
# 捡瓶子就在所有的文档里随机读取
import os
import datetime
import random

pingzi = []
count = 0  # 用来统计扔瓶子的次数，每天上限5次
while True:
    print("1.扔瓶子\n2.捡瓶子\n3.退出")
    choose = input()
    path = "D:\\piaoliuping\\"
    f = os.path.exists(path)  # 返回D盘是否存在piaoliuping文件夹，有则返回True，没有返回False
    os.chdir("D:")
    if not f:  # 判断D盘是否有 piaoliuping这个文件夹，没有则创建，有则把工作目录更改为piaoliuping文件下
        os.mkdir("piaoliuping")
    else:
        os.chdir("D:/piaoliuping/")

    if choose == "1":
        if count > 5:
            print("您今天扔瓶子的次数已上限，请明天再来！")
            continue
        scrip = input("请输入漂流瓶内容：（不能超过20个字符）")
        if len(scrip) > 20:
            print("您输入的内容过长，无法输入！")
            continue
        else:
            # 创建一个以当前时间为文件名的文本文档
            w = open(path + (datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")) + ".txt", 'w', encoding='utf-8')
            w.write(scrip)  # 输入漂流瓶内容
            w.close()   # 关闭文件
            count += 1  #瓶子使用次数加1
            print("您的瓶子已扔出！您今天还剩{}次机会扔瓶子".format(5 - count))
            continue
    elif choose == "2":
        all = os.listdir(path)      # 返回指定的文件夹包含的文件或文件夹的名字的列表
        for i in all:               # 对文件中以 .txt 结尾的文件进行遍历
            if os.path.splitext(i)[1] == '.txt':
                pingzi.append(i[0])     # 将遍历到的文件名存入列表
        suiji = random.randint(0, len(all) - 1)     # 生成一个随机数，不超过列表的长度
        piaoliu = open(all[suiji], 'r', encoding='utf-8')  # 把列表中随机到的文本文档打开
        text = piaoliu.read()           # 随机到的文本文档进行读取
        print(text)     # 打印显示在控制台
        piaoliu.close()     # 关闭文档
        continue
    elif choose == "3":
        break
    else:
        print("输入错误，请重新选择！")
        continue
