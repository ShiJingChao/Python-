"""
	学生信息管理系统原有信息：
	     姓名			年龄		年级		班级
		李小花		18		高三		1班
		王二狗		17		高二		2班
		刘三胖		16		高一		1班
		史铁柱		17		高二		1班
		隔壁老王  	18		高三		2班
功能: 增删改查,显示全部,退出; 姓名不能重复,可根据姓名进行查找;
分析:
    1. 一个字典存储一个学生的信息:
        {
            "姓名": "李小花",
            "年龄": 18,
            "年级": "高三",
            "班级": "1班"
        }
    2. 列表用来存储所有的学生
            有序, 元素可以是任意的数据类型
            [{}, {}, {}, {}, ....]
            *不能用元组, 因为元组不可变, 无法进行增删改的操作;
            *不能用集合, 因为集合中的元素类型要求不可变, 集合中无法存储字典类型数据;

            字典: 装所有学生信息;
            {
                "李小花": [18, "高三", "2班"],
                "王二狗": [16, "高四", "4班"],
            }
"""

all_stu_list = [
    {"姓名": "李小花", "年龄": 18, "年级": "高三", "班级": "2班"},
    {"姓名": "王二狗", "年龄": 17, "年级": "高二", "班级": "2班"},
    {"姓名": "刘三胖", "年龄": 16, "年级": "高一", "班级": "1班"}
]  # 装着所有学生的列表

all_name_list = ["李小花", "王二狗", "刘三胖"]  # 装着所有学生姓名的列表

while True:
    print("*" * 60)
    print("欢迎来到学生信息管理系统".center(50))
    print("1. 增加学生".center(50))
    print("2. 删除学生".center(50))
    print("3. 修改学生".center(50))
    print("4. 查找学生".center(50))
    print("5. 退出系统".center(50))
    print("6. 显示全部学生".center(50))
    print("*" * 60)

    chose = input("请输入您的选择:")

    if chose == "1":  # 增加学生
        name = input("请输入姓名:")
        # 判断姓名是否存在, 不能出现重复姓名的同学
        if name in all_name_list:
            print("该生已存在, 不能重复录入系统")
            continue  # 结束当前循环, 继续下一次循环
        age = int(input("请输入年龄:"))  # 将用户输入的年龄转换为整型数据
        grade = input("请输入年级:")
        cls = input("请输入班级:")
        stu_dict = {"姓名": name, "年龄": age, "年级": grade, "班级": cls}  # 新学生的信息字典
        all_stu_list.append(stu_dict)  # 将新学生添加到所有学生列表中
        print("添加成功!")
        all_name_list.append(name)
    elif chose == "2":  # 删除学生
        name = input("请输入要删除的学生姓名:")
        for stu in all_stu_list:
            if name == stu["姓名"]:
                all_stu_list.remove(stu)
                print("删除成功")
                all_name_list.remove(name)
                break
        else:
            print("该生不存在,无法删除")
        # for..in..else
        # 如果执行了for..in..中的break,则不会执行else语句
        # 如果遍历结束之后都没有执行for..in..中的break,则会执行else语句
    elif chose == "3":  # 修改学生信息
        name = input("请输入修改学生的姓名:")
        for stu in all_stu_list:
            if name == stu["姓名"]:  # 遍历获取每一个学生字典
                after_name = input("请输入修改后的姓名:")
                if after_name in all_name_list and after_name != stu["姓名"]:  # 修改之后的姓名可以和原名字一样,但不可以和已存在的其他姓名一样
                    print("该生已存在, 不能重复录入系统")
                after_age = int(input("请输入修改后的年龄:"))
                after_grade = input("请输入修改后的年级:")
                after_cls = input("请输入修改后的班级:")
                after_stu = {"姓名": after_name, "年龄": after_age, "年级": after_grade, "班级": after_cls}
                # 将修改前的字典替换为修改后的字典,
                index = all_stu_list.index(stu)  # 获取修改前字典的索引值
                all_stu_list.remove(stu)  # 删除旧信息字典
                all_stu_list.insert(index, after_stu)  # 增加新信息字典
                print("修改成功!")
                if after_name != stu["姓名"]:  # 如果修改之后的姓名和修改之前的姓名不一致,则更新all_name_list:
                    # 获取旧姓名的索引值
                    old_name_index = all_name_list.index(stu["姓名"])
                    # 删除旧姓名
                    all_name_list.remove(stu["姓名"])
                    # 插入增加新姓名
                    all_name_list.insert(old_name_index, after_name)
                break
        else:
            print("该生不存在,无法进行修改")
    elif chose == "4":  # 查找学生
        name = input("请输入想要查找的学生姓名:")
        if name in all_name_list:
            for stu in all_stu_list:
                if name == stu["姓名"]:
                    print("您要查找的学生信息是:", stu)
        else:
            print("该生不存在...")
    elif chose == "5":  # 退出系统
        break  # 结束循环
    elif chose == "6":  # 显示全部学生
        for stu in all_stu_list:
            print("学生姓名:{}\t学生年龄:{}\t学生班级:{}\t学生年级:{}".format(stu["姓名"], stu["年龄"], stu["班级"], stu["年级"]))
    else:
        print("输入有误, 请重新输入")
        continue  # 结束当前循环, 继续下一次循环















