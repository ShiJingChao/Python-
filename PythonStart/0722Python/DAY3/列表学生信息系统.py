# 练习 列表的学员管理系统
# 需求分析：添加学员，删除学员，修改资料，多种方式查询



# 增加 一组 史景超
stu_info = [["demo", "nan", 18]]
while True:
    lst_tip = ["1.添加学员", "2.修改资料", "3.查询", "4.删除学员", "5.退出"]
    for i in lst_tip:   # 遍历列表循环输出提示
        print(i)
    choose = input("请输入你要选择的操作：")
    if choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5":
        print("输入有误，请重新操作")
        continue
    elif choose == "1":
        stu_name = input("请输入要添加的学生的姓名：")
        stu_gender = input("输入学生性别：")
        stu_age = input("输入学生年龄：")
        stu_date = [[stu_name, stu_gender, stu_age]]
        stu_info.extend([stu_date[0]])
        print("添加成功")
        continue
    # 四组 韦子健  修改学生信息
    elif choose == "2":
        n = 0
        m = 1
        while n < len(stu_info):
            print(m, ('号学生信息'), stu_info[n])
            m += 1
            n += 1
        sum = int(input('请输入要修改的学号'))
        while True:
            if sum:
                stu_info[sum - 1][0] = input('请输入姓名')
                stu_info[sum - 1][1] = input('请输入性别')
                stu_info[sum - 1][2] = int(input('请输入年龄'))
                break
        x = 0
        y = 1
        while x < len(stu_info):
            print(y, ('号学生信息'), stu_info[x])
            x += 1
            y += 1

# 四组 郭洋
    elif choose == "3":
        n = input('查询所有同学信息请扣1，某位同学请扣2\n')
        if n == '1':
            for i in stu_info:
                print(i)
        else:
            p = input('请输入同学姓名：\n')
            for i in stu_info:
                if i[0] == p:
                    print('姓名：%s, 性别:%s, 年龄：%s' % (i[0], i[1], i[2]))
                if i == stu_info[len(stu_info) - 1] and i[0] != p:  #遍历列表，查询学生姓名
                    print('没有该同学!!!')
    elif choose == "4":
        print("根据序号删除输入1，根据名字删除输入2")
        m = input()
        if m == "1":
            j = int(input("输入你要删除的学生的序号："))
            if j >= len(stu_info) or j <= 0:
                print("输入错误")
            else:
                stu_info.remove(stu_info[j-1])
                print("删除成功！")
        elif m == "2":
            stu_del = input("请输入你要删除的同学信息的名字：\n")
            for i in stu_info:
                for i in stu_info:
                    if i[0] == stu_del:
                        stu_info.remove(i)
                        print('删除成功')
                    elif i == stu_info[len(stu_info) - 1] and i[0] != stu_del:
                        print('没有该同学!!!')

    elif choose == "5":
        tuichu = input("结束，请输入任意键退出")
        if tuichu == "Y":
            break
        else:
            break
    break
