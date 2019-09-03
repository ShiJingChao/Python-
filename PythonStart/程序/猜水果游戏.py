a = ['西瓜', '梨子', '香蕉', '核桃', '苹果', '桃子', '花生', '石榴', '西瓜', '梨子']
b = ['绿色的，红心', '配冰糖，暖到心', '弯弯的月儿小小的船,小小的船儿两头尖', '皱肉皱骨头， 骨头生在肉外头。', '乔布斯', '胖娃娃，没手脚，红尖嘴，一身毛，背上一道沟，肚里好味道。',
     '青藤藤，开黄花，地上开花不结果，地下结果不开。,', '小小红坛子，装满红饺子，吃掉红饺子，吐出白珠子。', '绿色的，红心', '配冰糖，暖到心']
count = 0
tip = 3
k = 0
print("猜题游戏开始！")
print("游戏一共十道，每题十分，共100分")
while k < 10:
    if count == 10:
        print("您已经猜了10次，游戏结束")
        break
    print("第{}题：{}".format(k + 1, b[k]))
    print("1:使用锦囊\n2.不使用锦囊\n3.退出游戏")
    choose = input("请输入你的选择：")
    if choose == "1":
        if tip > 0:
            print("请输入你要使用的锦囊：")
            print("1.提示水果第一个字")
            print("2.提示水果第二个字")
            print("3.提示水果的字数")
            chose_tip = input("请输入您要使用的锦囊")
            if chose_tip == "1":
                print("水果的第一个字为：", a[k][0])
            elif chose_tip == "2":
                print("水果的第二个字为：", a[k][1])
            elif chose_tip == "3":
                print("水果一共有{}个字".format(len(a[k])))
            else:
                print("输入有误，请重新输入！")
            tip -= 1
            print("您还剩{}次使用锦囊的机会".format(tip))
            answer = input("您的答案为：")
            if answer == a[k]:
                count += 1
                print("您还剩{}次机会猜水果".format(10 - count))
                is_jixu = input("您猜对了，您是否要继续？\n1:继续2：退出")
                # count += 1
                if is_jixu == "1":
                    k += 1
                    continue
                elif is_jixu == "2":
                    break
                else:
                    print("输入错误，默认退出")
                    break
            elif answer != a[k]:
                count += 1
                print("您还剩{}次机会猜水果".format(9 - count))
                is_jixu = input("您猜错了，是否要继续？\n1:继续2：退出")
                if is_jixu == "1":
                    continue
                elif is_jixu == "2":
                    break
                else:
                    print("输入错误，默认退出")
                    break
        if tip <= 0:
            print("您的锦囊次数已经用完，不能使用！")
            continue
    elif choose == '2':
        answer = input("您的答案为：")
        if answer == a[k]:
            count += 1
            print("您还剩{}次机会猜水果".format(10 - count))
            is_jixu = input("您猜对了，您是否要继续？\n1:继续2：退出")
            if is_jixu == "1":
                k += 1
                continue
            elif is_jixu == "2":
                break
            else:
                print("输入错误，默认退出")
                break
        if answer != a[k]:
            count += 1
            print("您还剩{}次机会猜水果".format(10 - count))
            is_jixu = input("您猜错了，是否要继续？\n1:继续2：退出")
            if is_jixu == "1":
                continue
            elif is_jixu == "2":
                break
            else:
                print("输入错误，默认退出")
                break
    if choose == "3":
        print("程序结束")
        break

