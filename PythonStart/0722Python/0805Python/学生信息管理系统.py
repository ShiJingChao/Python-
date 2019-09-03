# 用字典做法

def m_show():
    print("\n", "*" * 30,
          "\n*	欢迎进入学生信息管理系统	*"
          "\n* 		1.查找学生			*"
          "\n*		2.增加学生			*"
          "\n*		3.修改学生			*"
          "\n*		4.删除学生			*"
          "\n*		5.显示全部信息		*"
          "\n*		6.退出系统			*"
          "\n", "*" * 30)


# 初始字典中存放的学生信息
db = {1: {"姓名": "小花", "年龄": 18, "年级": "高三", "班级": "1班"},
      2: {"姓名": "二狗", "年龄": 17, "年级": "高二", "班级": "2班"},
      3: {"姓名": "三胖", "年龄": 16, "年级": "高一", "班级": "1班"},
      4: {"姓名": "铁柱", "年龄": 17, "年级": "高二", "班级": "1班"},
      5: {"姓名": "老王", "年龄": 18, "年级": "高三", "班级": "2班"}}

while True:
    m_show()
    choose = input("请输入你的选择：")
    cho_list = ["1", "2", "3", "4", "5", "6"]  # 将选择放在列表中，用户输入不在列表的范围内，则输入错误
    if choose not in cho_list:
        print("输入有误!返回主界面")
        continue
    elif choose == "1":
        find_stu = input("请输入学生姓名：")
        # 对字典进行遍历
        for k, v in db.items():
            # 对 输入的学生姓名是否在嵌套的字典的值中 进行判断
            if find_stu in v.values():
                # 存在，则对内层字典进行遍历输出，打印学生信息
                for m, n in v.items():
                    print(m, n)
                break
        else:
            print("没有找到这位同学！")
    elif choose == "2":
        name = input("请输入学生姓名：")
        # 对字典进行遍历
        for k, v in db.items():
            # 判断 输入的姓名 是否存在于内层字典的values值中
            if name in v.values():
                print("已存在学生%s，不能存储!" % name)
                break
        else:
            age = input("请输入学生年龄：")
            grade = input("请输入学生年级：")
            clas = input("请输入学生班级：")
            # 获取外层字典键的最大值，+1作为新添加学生的序号
            db[max(db.keys()) + 1] = {"姓名": name, "年龄": age, "年级": grade, "班级": clas}
            print("存储成功!")
    elif choose == "3":
        int_name = input("请输入要修改的学生的姓名：")
        # 对字典进行遍历
        for k, v in db.items():
            # 判断要 修改的学生的姓名 是否存在于内层字典中
            if int_name in v.values():
                name1 = input("请输入新学生姓名：")
                age1 = input("请输入新学生年龄：")
                grade1 = input("请输入新学生年级：")
                clas1 = input("请输入新学生班级：")
                db[k] = {"姓名": name1, "年龄": age1, "年级": grade1, "班级": clas1}
                print("修改成功!")
                break
        else:
            print("没有找到%s这名同学" % int_name)
    elif choose == "4":
        cho_del = input("根据姓名删除选择1，根据序号删除选择2：")
        if cho_del != "1" and cho_del != "2":
            print("输入有误，返回主界面!")
        elif cho_del == "1":
            del_stu = input("请输入要删除的学生的姓名：")
            # 对字典的键值对进行遍历
            for k, v in db.items():
                # 判断 输入的学生姓名是否存在于 嵌套字典的values中
                if del_stu in v.values():
                    # 将值对应的键赋值给a，以便删除操作
                    a = k
                    print("删除成功")
                    break
            else:
                print("没有找到%s这名同学" % del_stu)
            # 判断 a是否为空值 ，不为空，说明存在这名同学，做删除操作
            if a is not None:
                del db[a]
        elif cho_del == "2":
            del_stu = int(input("请输入要删除的学生的序号："))
            # 判断 输入的序号是否存在于 db字典的键中
            if del_stu not in db.keys():
                print("没有找到%s这名同学" % del_stu)
            else:
                db.pop(del_stu)
                print("删除成功!")
    elif choose == "5":
        # 对字典进行遍历，打印学生的序号及信息
        for k, v in db.items():
            print(k)
            for m, n in v.items():
                print(m, n, )
            print("-" * 60)
    elif choose == "6":
        exit()
