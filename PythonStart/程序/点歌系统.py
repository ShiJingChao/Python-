# 点歌系统
# 选择点歌方式（通过地区点歌选择1，通过歌手点歌选择2）
# 港台地区选择1，大陆地区选择2
# 曲库有：{'1': {'邓紫琪': {'我的秘密', '泡沫', 'ANNY'},
# '刘德华': {"忘情水", '世界第一等', '来生缘'}},
# '2': {'张碧晨': {'不要忘记我爱你', '年轮', '白芍花开'},
# '赵雷': {'成都', '三十岁的女人', '理想'}}}
# 如果输入错误，重新启动程序
# 选择歌手后还要选择喜欢的歌曲


while True:
    print("点歌系统启动!")
    print("*" * 60)
    diange = input("通过地区点歌请输入1,通过歌手点歌请输入2")
    if diange != "1" and diange != "2":
        print("选择有误，重新启动程序！")
        continue
    elif diange == "1":
        print("港台地区选择1")
        print("大陆地区选择2")
        diqu = input()
        quku = {'1': {'邓紫琪': {'我的秘密', '泡沫', 'ANNY'}, '刘德华': {"忘情水", '世界第一等', '来生缘'}},
                '2': {'张碧晨': {'不要忘记我爱你', '年轮', '白芍花开'}, '赵雷': {'成都', '三十岁的女人', '理想'}}}
        if diqu != "1" and diqu != "2":
            print("输入有误，重新启动程序")
            continue
        elif diqu == "1":
            for i in quku['1'].keys():
                print(i)
            geshou = input("请输入你喜欢的歌手：")
            if geshou != "邓紫琪" and geshou != "刘德华":
                print("输入有误，重新启动程序！")
                continue
            elif geshou == "邓紫琪":
                for i in quku['1']['邓紫琪']:
                    print(i)
                deng_gequ = input("请输入你要播放的歌曲名：")
                if deng_gequ not in quku:
                    print("输入有误，重新启动程序！")
                    continue
                else:
                    print("即将播放您选择的歌曲...\n播放开始，开始播放")
            elif geshou == "刘德华":
                for i in quku['1']['刘德华']:
                    print(i)
                liu_gequ = input("请输入你要播放的歌曲：")
                if liu_gequ != "忘情水" and liu_gequ != "世界第一等" and liu_gequ != "来生缘":
                    print("输入有误，重新启动程序！")
                    continue
                else:
                    print("即将播放您选择的歌曲...\n播放开始，开始播放")
                    break
            break
        elif diqu == "2":
            for j in quku['2'].keys():
                print(j)
            geshou = input("请输入你喜欢的歌手：")
            if geshou != "张碧晨" and geshou != "赵雷":
                print("输入有误，重新启动程序！")
                continue
            elif geshou == "张碧晨":
                for i in quku['2']['张碧晨']:
                    print(i)
                deng_gequ = input("请输入你要播放的歌曲名：")
                if deng_gequ != '不要忘记我爱你' and deng_gequ != '年轮' and deng_gequ != '白芍花开':
                    print("输入有误，重新启动程序！")
                    continue
                else:
                    print("即将播放您选择的歌曲...\n播放开始，开始播放")
            elif geshou == "赵雷":
                for i in quku['2']['赵雷']:
                    print(i)
                liu_gequ = input("请输入你要播放的歌曲：")
                if liu_gequ != "成都" and liu_gequ != "三十岁的女人" and liu_gequ != "理想":
                    print("输入有误，重新启动程序！")
                    continue
                else:
                    print("即将播放您选择的歌曲...\n播放开始，开始播放")
                    break
            break
        else:
            print("输入有误，请重新输入！")
            continue
    elif diange == "2":
        quku = {'1': {'邓紫琪': {'我的秘密', '泡沫', 'ANNY'}, '刘德华': {"忘情水", '世界第一等', '来生缘'}},
                '2': {'张碧晨': {'不要忘记我爱你', '年轮', '白芍花开'}, '赵雷': {'成都', '三十岁的女人', '理想'}}}
        print('曲库的歌手有：')
        for k, v in quku['1'].keys(), quku['2'].keys():
            print(k)
            print(v)
        geshou = input("请输入你选择的歌手名字：")
        if geshou != "邓紫琪" and geshou != "刘德华" and geshou != "张碧晨" and geshou != "赵雷":
            print("输入有误，系统重新启动！")
            continue
        elif geshou == "邓紫琪":
            for i in quku['1']['邓紫琪']:
                print(i)
            gequ = print("请输入你想播放的歌曲：")
            if gequ != "我的秘密" and gequ != "泡沫" and gequ != "ANNT":
                print("输入错误，程序重新启动！")
                continue
            else:
                print("即将播放您选择的歌曲...\n播放开始，开始播放")
                break
        elif geshou == "刘德华":
            for i in quku['1']['刘德华']:
                print(i)
            gequ = input("请输入你想播放的歌曲：")
            if gequ != "忘情水" and gequ != "世界第一等" and gequ != "来生缘":
                print("输入错误，程序重新启动！")
                continue
            else:
                print("即将播放您选择的歌曲...\n播放开始，开始播放")
                break
        elif geshou == "张碧晨":
            for i in quku['2']['张碧晨']:
                print(i)
            gequ = input("请输入你想播放的歌曲：")
            if gequ != "不要忘记我爱你" and gequ != "年轮" and gequ != "白芍花开":
                print("输入错误，程序重新启动！")
                continue
            else:
                print("即将播放您选择的歌曲...\n播放开始，开始播放")
                break
        elif geshou == "赵雷":
            for i in quku['2']['赵雷']:
                print(i)
            gequ = input("请输入你想播放的歌曲：")
            if gequ != "成都" and gequ != "三十岁的女人" and gequ != "理想":
                print("输入错误，程序重新启动！")
                continue
            else:
                print("即将播放您选择的歌曲...\n播放开始，开始播放")
                break
        break

