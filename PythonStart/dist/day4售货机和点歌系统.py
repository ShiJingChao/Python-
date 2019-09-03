# 19.07.19作业 史景超
# 1.使用列表来保存商品

# lst = ['手机', '电脑', '鼠标', '平板']
#
# for product in lst:
#     msg = "商品的序号是：{}，名称：{}".format(lst.index(product) + 1, product)
#     print(msg)
# while True:
#     choose = input('请输入要购买的商品的序号[Q/q退出程序]：')
#     # 判断输入的是否是纯数字
#     if choose.isdigit():
#         num = int(choose)
#         if 0 < num <= len(lst):
#             print(lst[int(choose) - 1])
#         else:
#             print('输入的序号有误，请重新输入！')
#     elif choose == 'q' or choose == 'Q':
#         print('程序结束')
#         break
#     else:
#         print('输入的内容错误，请重新输入！')

# 点歌系统

while True:
    print("点歌系统已经启动！")
    print("***************")
    print("请选择点歌方式")
    print("通过地区点歌点击1")
    print("通过歌手点歌点击2")
    a = input("请选择您的点歌方式：")  # 装饰

    if a == '1':
        print("**港台地区请选择1**")
        print("**大陆地区请选择2**")
        quku = {'1': {'邓紫琪': {'我的秘密', '泡沫', 'ANNY'}, '刘德华': {"忘情水", '世界第一等', '来生缘'}},
                '2': {'张碧晨': {'不要忘记我爱你', '年轮', '白芍花开'}, '赵雷': {'成都', '三十岁的女人', '理想'}}}  # 字典
        where_name = input("请选择您喜欢歌手所属地区")
        if where_name != '1' and where_name != '2':
            print("输入有误！请重新输入！我们将重新启动程序")
            continue
        print("根据您的选择我们找到以下歌手：")
        for i in list(quku[where_name].keys()):  # 得到地区后遍历歌手
            print(i, end='  ')
            print()
        songer_name = input(" 请输入你喜欢的歌手 ：")
        if songer_name not in list(quku[where_name].keys()):
            print("您的输入错误！我们将重新启动程序！")
            continue
        print("根据您的选择我们找到以下歌曲：")
        for j in list(quku[where_name].get(songer_name)):  # 得到歌手后遍历他（她）的歌曲
            print(j, end=' ')
            print()
        song_name = input("请输入您喜欢的歌名：")
        print("请稍等.......")
        print("播放开始！请开始你的表演")
        break

    elif a == '2':
        quku = {'邓紫棋': {'我的秘密', '泡沫'}, '刘德华': {"忘情水", '世界第一等'}, '张碧晨': {'不要忘记我爱你', '年轮'}, '赵雷': {'成都', '三十岁的女人'}}  # 字典
        print("曲库的歌手有：")
        for i in list(quku.keys()):  # 得到歌手后遍历他（她）的歌曲
            print(i, end=' ')
            print()

        songer_name = input(" 请输入你喜欢的歌手 ")
        if songer_name not in list(quku.keys()):
            print("您的输入错误！我们将重新启动程序！")
            continue
        print("根据您的选择我们找到：")
        for j in list(quku.get(songer_name)):  # 得到歌手后遍历他（她）的歌曲
            print(j, end=' ')
            print()
        song_name = input("请输入您喜欢的歌名")
        print("请稍等..........")
        print("播放开始！请开始你的表演")
        break

    else:
        print("您的选择有误！请按照屏幕上的规定重新选择！")
        continue
