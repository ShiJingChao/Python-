# 记录所有的名片字典
# shift+F6 可以修改所有的变量名或者出现的所有名字
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0\n")
    print("1.新建名片\n2.显示全部\n3.查询名片\n\n0.退出系统")
    print("*" * 50)


def add_card():
    """添加名片"""
    print("-" * 50)
    print("新增名片")
    # 提示用户输入名片信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话:")
    work_str = input("请输入公司：")
    # 将用户信息保存在字典中
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "h_work": work_str}
    # 将名片字典保存在列表中
    card_list.append(card_dict)
    print(card_list)
    print("%s添加成功！" % name_str)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何的名片信息，请添加后重新显示！")
        # return下方的代码不会被执行
        # 如果return 后面没有任何的内容，表示会返回到调用函数的位置
        # 并且不会返回任何的结果
        return
    # 打印表头
    for name in ["姓名", "电话", "公司"]:
        print(name, end='\t\t')
    print()
    print("=" * 50)

    # 遍历名片列表依次输出所有名片信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t\t%s" % (card_dict["name"],
                                    card_dict["phone"],
                                    card_dict["h_work"]))


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    # 提示用户输入要搜索的姓名
    find_name = input("请输入要查询的姓名：")
    # 2.遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\t公司")
            print("=" * 50)
            print("%s\t\t%s\t\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["h_work"]))
            # 针对找到的名片记录执行修改和删除的操作
            deal_card(card_dict)
            break
    else:
        print("不好意思，没有找到%s" % find_name)


def deal_card(find_dict):
    """
    处理查找到的名片
    :param find_dict: 查找到的名片
    """
    print(find_dict)

    action_str = input("请选择要执行的操作："
                       "[1] 修改 [2] 删除 [0] 返回上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["h_work"] = input_card_info(find_dict["h_work"], "公司：")
        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片")


def input_card_info(dist_value, tip_message):
    """修改的进一步优化
    :param dist_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return:如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)
    # 2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果用户没有输入，返回字典中原有的值
    else:
        return dist_value
