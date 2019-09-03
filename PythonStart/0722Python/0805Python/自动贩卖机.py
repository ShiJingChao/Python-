history = []    # 用来存储购买记录
while True:
    # 主界面内容
    welcome_show = ["=" * 30,
                    "=\t欢迎来到AI牌自动贩卖机 \t=",
                    "=\t1.零售\t\t\t\t\t=",
                    "=\t2.查询消费记录\t\t\t=",
                    "=\t3.退出\t\t\t\t\t="]
    # 存储产品序号名称
    retail1 = {1: "可口可乐",
               2: "3+2饼干",
               3: "泡面",
               4: "笔记本",
               5: "钢笔",
               6: "文曲星"}
    # 遍历主界面输出
    for i in welcome_show:
        print(i)
    choose = input("请输入你选择的操作：")
    # 输入选项外数据，返回主界面
    if choose != "1" and choose != "2" and choose != "3":
        print("输入有误，返回主界面")
        continue
    # 用户选择零售
    elif choose == "1":
        # 零售界面
        retail = ["=" * 30,
                  "=\t1.可口可乐\t50元 \t\t=",
                  "=\t2.3+2饼干\t35元\t\t=",
                  "=\t3.泡  面\t15元\t\t=",
                  "=\t4.笔记本\t\t4元\t\t\t=",
                  "=\t5.钢  笔\t3元\t\t\t=",
                  "=\t6.文曲星\t\t108元\t\t="]
        # 遍历零售界面输出内容
        for i in retail:
            print(i)
        cho_product = input("请输入你要购买的产品序号：")
        # 存储商品序号
        ser_num = ["1", "2", "3", "4", "5", "6"]
        # 存储商品价格
        price = [50, 35, 15, 4, 3, 108]
        if cho_product not in ser_num:
            print("输入错误！")
            continue
        else:
            cho_nums = input("请输入你要购买的产品的数量：")
            # 判断输入的是否全部为数字
            # 纯数字
            if cho_nums.isdigit():
                # 对字典中产品序号进行遍历
                for i in retail1.keys():
                    # 如果 输入的产品序号等于遍历的序号
                    if i == int(cho_product):
                        # 输出信息及计算金额
                        money = int(price[i]) * int(cho_nums)
                        print(retail1[i])
                        print("您购买数量为{}".format(cho_nums))
                        print("您所要花费的金额为:{}元".format(money))
                        # 是否购买
                        affirm = input("是否进行购买？"
                                       "\n1.小钱，买了"
                                       "\n2.太贵了，不买")
                        # 输入错误信息
                        if affirm != "1" and affirm != "2":
                            print("输入错误，返回主界面")
                        # 不购买
                        elif affirm == "2":
                            print("返回主界面")
                        # 购买
                        elif affirm == "1":
                            # 接收用户输入的金额
                            in_money = input("请输入您给了多少钱（元）：")
                            # 判断 金额是否全 数字
                            # 有非数字
                            if in_money.isdigit() == False:
                                print("输入有误！返回主界面")
                            # 纯数字
                            else:
                                # 强制转换类型
                                in_money = int(in_money)
                                # 判断钱是否足够
                                # 不够
                                if in_money < money:
                                    print("您输入的钱不够哦~返回到主界面，请重新操作！")
                                    continue
                                # 够
                                elif in_money >= money:
                                    print("您给的金额为{}，找零为：{}元".format(in_money, in_money - money))
                                    print("购买成功!")
                                    # 购买成功则存储购买记录
                                    history.append(retail1[i])
                                    history.append(cho_nums)
                                    history.append(money)
                                    continue
            # 有非数字
            else:
                print("输入错误！")
    # 用户选择查询消费记录
    elif choose == "2":
        # 选择查询单次还是全部
        f_history = input("1.查询单次消费记录\n"
                          "2.查询所有消费记录\n"
                          "请输入您的选择：")
        # 输入数据为其他数据 则返回
        if f_history != "1" and f_history != "2":
            print("输入有误，请重新输入!")
        # 输入正确
        elif f_history == "1":
            # 具体的消费记录
            dc_history = input("单次查询：\n请输入你要查询哪次的消费记录")
            # 输入的为其他字符
            # 输入无哦呜
            if dc_history.isdigit() == False:
                print("输入有误！返回主界面")
            else:
                # 强制类型转换
                dc_history = int(dc_history)
                # 输入要查询的消费记录序号不能超过历史记录长度的1//3(3个信息为一个单位)
                max_his = (len(history) // 3)
                # 大于长度，不存在
                if dc_history > max_his:
                    print("不存在此次消费记录，返回主界面")
                # 存在
                elif dc_history <= max_his:
                    # 输出提示信息
                    print("产品名称\t购买数量\t花费金额")
                    # 遍历历史记录，找到对应的信息进行输出
                    for i in range((dc_history - 1) * 3, (dc_history - 1) * 3 + 3):
                        print(history[i], end="\t\t")
                    print()
        # 输出全部
        elif f_history == "2":
            print("产品名称\t购买数量\t花费金额")
            # 对消费记录进行遍历
            for i in range(0, len(history)):
                # 按格式输出
                if i != 0 and i % 3 == 0:
                    print()
                print(history[i], end="\t\t")
            print()
    # 用户选择退出
    elif choose == "3":
        is_exit = input("1:退出\n"
                        "2:返回主菜单\n"
                        "请输入是否要退出：")
        if is_exit.isdigit():
            if int(is_exit) == 1:
                exit()
        else:
            continue
