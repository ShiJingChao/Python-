# 名片管理系统
import card_tools

while True:
    # TODO 显示菜单
    card_tools.show_menu()

    choose = input("请输入你的选择：")
    print("您选择的操作是：%s" % choose)
    if choose in ['1','2','3']:
        # 新增名片
        if choose == "1":
            card_tools.add_card()
        # 显示名片
        if choose == "2":
            card_tools.show_all()
            pass
        # 查询名片
        if choose == "3":
            card_tools.search_card()
            pass
    elif choose == "0":
        break
    else:
        print("您的输入不正确，请重新选择")