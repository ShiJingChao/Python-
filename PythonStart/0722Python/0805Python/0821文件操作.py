# # file = open(r"C:\Users\Administrator\PycharmProjects\test1\0722Python\0805Python\message.txt","r",encoding="gbk")
# # b = []
# # text = file.read()
# # print(text)
# # f_year = input("请输入年份：")
# # for i in text.split("\n"):
# #     # print(i)
# #     a = i.split("|")
# #     b.append(a)
# # c = [j for i in b for j in i]
# # for i in range(len(c)):
# #     if c[i] == f_year:
# #         print("举办国：{}  冠军国：{}".format(c[i+1],c[i+2]))
# #         break
# # else:
# #     print("{}年没有举办".format(f_year))
#
#
#
# file = open(r"C:\Users\Administrator\PycharmProjects\test1\0722Python\0805Python\message.txt","r",encoding="gbk")
# line_list = file.readlines()
#
# year = input("请输入一个年份：")
#
# for this_year in line_list:
#     if this_year.startswith(year):
#         res = this_year.split("|")
#         print("举办地：",res[1])
#         print("冠军国：",res[-1])
#     # 或者这样判断
#     if year in this_year:
#         index1 = this_year.rfind("|")
#         print("冠军国：",this_year[index1+1:])
#         print("举办地",this_year[5:index1])
#
#
import time
# file = open("chat.txt",mode="a+",encoding="utf8")
# while 1:
#     x_h = input("小花说：")
#     e_g = input("二狗说：")
#     if x_h == '' and e_g == '':
#         t = time.time()
#         file.write(time.strftime("\n%Y-%m-%d",time.localtime()))
#         break
#     else:
#         file.write("小花说："+x_h)
#         file.write("\n二狗说："+e_g)
#
# file.close()
# def chat():
#     f = open("chat.txt","a",encoding="utf8")
#     t = time.localtime()
#     time_str = time.strftime("%Y-%m-%d %H:%M:%S", t)
#     f.write(time_str)
#     f.write("\n")
#     while True:
#         p1 = input("小花说：")
#         p2 = input("二狗说：")
#
#         if not p1 and not p2:
#             print("--聊天结束--")
#             f.close()
#             break
#         else:
#             p1_str = "小花说："+p1+"\n"
#             p2_str = "二狗说："+p2+"\n"
#             f.writelines([p1_str, p2_str])
# chat()
# 输入字母A到Z
# def write_alpha():
#     f = open("alpha.txt","w")
#     s = ""
#     for x in range(65,91):
#         s+= chr(x)
#         f.write(s)
#         f.close()
# write_alpha()

# 写一首诗，每句换行
# def poem():
#     s = "\n鹅鹅鹅\n曲项向天歌\n白毛浮绿水\n红掌拨清波"

# file = open(r"C:\Users\Administrator\PycharmProjects\test1\HTML前端\day02CSS\img\QQ图片20190813141855.jpg",'rb')
# file1 = open("new.jpg","wb")
# d = file.read()
# f = file1.write(d)
# file.close()
# file1.close()





# import os
#
# def is_dir(f):  # 判断是否为目录
#     if os.path.isdir(f):
#         os.chdir(f)
#         print("-"*30)
#         for i in all:   # 遍历目录列表
#             if os.path.isfile(i):
#                 print("{} 是文件".format(i))
#             elif os.path.isdir(i):
#                 print("{} 是目录".format(i))
#         print("-"*30)
#         return True
#     else:
#         print("输入不符合规范或目录不存在!")
#         return False
#
#
# def menu(): # 主菜单
#     print("1.添加前缀\n2.删除前缀\n3.创建文件\n4.删除文件\n5.重命名文件\n6.退出")
#
# def cho_one():  # 添加前缀
#     cho_name = input("请输入你要添加前缀的文件名：")
#     if cho_name not in all:
#         print("您输入的文件名不存在！")
#     else:
#         cho_name1 = input("请输入您要添加文件名的前缀：")
#         for i in all:
#             if i == cho_name:   # 目录下文件名和输入的要添加前缀名相同
#                 os.rename(cho_name,cho_name1+cho_name)  # 添加前缀
#                 print("修改成功!")
# def cho_two():  # 删除前缀
#     cho_name = input("请输入你要删除前缀的文件名：")
#     if cho_name in all: # 遍历
#         f_num = input("请输入你要删除前缀的前几位？(纯数字)")
#         if f_num.isdigit(): # 判断输入的是否为纯数字
#             if int(f_num)>= len(os.path.splitext(cho_name)[0]): # 判断输入的数字的长度是否大于或者等于文件前缀长度
#                 print("文件前缀名没有这么长哦~请重新选择~")
#                 return False
#             else:
#                 os.rename(cho_name,cho_name[int(f_num):])   # 删除前缀
#                 print("删除成功!")
#                 return True
#         else:
#             print("您输入的不符合规范哦~")
#             return False
#     else:
#         print("您输入的文件名不存在!")
#         return False
#
# def cho_three():    # 创建文件夹或文件
#     cho_f = input("1.创建文件夹\n2.创建文件")
#     if cho_f != "1" and cho_f != "2":
#         print("输入错误!")
#         return False
#     elif cho_f == "1":
#         f_name = input("请输入文件夹名：")
#         a = "\\\\/:*?\"<>|"
#         if f_name in all:   # 判断文件夹名是否已经存在
#             print("文件夹已存在！")
#             return False
#         else:
#             for i in f_name:    # 输入的文件夹名是否包含系统不允许的字符
#                 if i in a:
#                     print("您输入的不合法!")
#                     return False
#                 else:
#                     os.mkdir(f_name)    # 创建文件夹
#                     print("成功！")
#     elif cho_f == "2":
#         wj_name = input("请输入文件名：")
#         a = "\\\\/:*?\"<>|"
#         if wj_name in all:   # 判断文件是否在目录中
#             print("文件夹已存在！")
#             return False
#         for i in wj_name:
#             if i in a or "." not in wj_name:    # 判断文件名是否合法
#                 print("您输入的不合法!失败!")
#                 return False
#         else:
#             f = open(wj_name, "a+", encoding="utf8")    # 创建文件
#             f.close()
#             print("成功!")
#
# def cho_four(): # 删除文件
#     de_f = input("请输入要删除的文件名：")
#     if not os.path.isfile(de_f):
#         print("您输入的不是文件名！")
#         return False
#     else:
#         if de_f in all:
#             os.remove(de_f)
#             print("删除成功!")
#         else:
#             print("您输入的文件不存在!")
#             return False
# def cho_five(): # 重命名
#     re_f = input("请输入您想重命名的文件名或目录名:")
#     if re_f in all:
#         re_f_new = input("请输入您想改后的名字")
#         a = "\\\\/:*?\"<>|"
#         if os.path.isfile(re_f):
#             for i in re_f_new:
#                 if i in a or "." not in re_f_new:
#                     print("您想修改的名字不合法！")
#                     return False
#                 else:
#                     os.rename(re_f,re_f_new)
#                     print("修改成功!")
#                     return True
#         else:
#             for i in re_f_new:
#                 if i in a:
#                     print("您输入的不合法!失败!")
#                     return False
#                 else:
#                     os.rename(re_f, re_f_new)
#                     print("修改成功!")
#                     return True
#
#     else:
#         print("您输入的文件或者目录名不存在!")
#         return False
#
# if __name__ == "__main__":
#     while True:
#         f = input("请输入一个目录：")
#         if not os.path.exists(f):
#             print("目录不存在")
#         else:
#             all = os.listdir(f) # 获取输入的目录列表
#             dir = is_dir(f)
#             if dir == False:
#                 continue
#             menu()
#             list = ["1","2","3","4","5","6"]
#             choose = input("请输入您的选择：")
#             if choose not in list:
#                 print("输入有误！")
#             elif choose == "1":
#                 cho_one()
#             elif choose == "2":
#                 t = cho_two()
#                 if t == False:
#                     continue
#             elif choose == "3":
#                 t = cho_three()
#                 if t == False:
#                     continue
#             elif choose == "4":
#                 f = cho_four()
#                 if f == False:
#                     continue
#             elif choose == "5":
#                 f = cho_five()
#                 if f == False:
#                     continue
#             elif choose == "6":
#                 exit()

import os
#
"""
    给定一个目录,
    列举出这个目录中的所有文件和文件夹, 
        以及子文件夹中的所有文件...
"""
# def ml(f):
#     for root, dirs, files in os.walk(f):
#         for dir in dirs:
#             print(dir)
#         for file in files:
#             print(file)
#
#
#
# if __name__ == "__main__":
#     f = input("请输入一个目录：")
#     ml(f)


# 或者递归函数
# def func(path): # 参数为给定目录
#     file_list = os.listdir(path)
#     for file in file_list:
#         file_path = path+ "/"+ file
#         if os.path.isfile(file_path):
#             print("[文件]：", file)
#
#         elif os.path.isdir(file_path):
#             print("[目录]：", file)
#             func(file_path)




#
# 1.有名为user_info.txt的文件，其内容格式如下，写一个程序，删除id为100003的行；
# pizza,100001
# alex, 100002
# egon, 100003


# f = open("user_info.txt","r")
# all_list = f.readlines()
# f.close()
#
# for line in all_list:
#     if "100003" in line:
#         all_list.remove(line)
#
# f_res = open("user_info.txt","w")
# f_res.writelines(all_list)
# f_res.close()



# 2.有名为user_info.txt的文件，其内容格式如下，写一个程序，将id为100002的用户名修改为alex li；
# pizza,100001
# alex, 100002
# egon, 100003

# with open("user_info.txt") as f:
#     all_list = f.readlines()
#
# for line in all_list:
#     if "100002" in line:
#
#         index = all_list.index(line)
#         all_list[index] = "alex li , 100002"
#
# with open("user_info.txt","w") as f:
#     f.writelines(all_list)



# 3.有名为username.txt的文件，其内容格式如下，写一个程序，判断该文件中是否存在"alex", 如果没有，则将字符串"alex"添加到该文件末尾，否则提示用户该用户已存在；
# pizza
# flex
# egon


# with open("username.txt","r+") as f:
#     all = f.read()
#     if "alex" in all:
#         print("该用户已存在！")
#     else:
#         f.write("\nalex")


# 4.有名为poetry.txt的文件，其内容如下，请删除第三行；
# 昔人已乘黄鹤去，此地空余黄鹤楼。
# 黄鹤一去不复返，白云千载空悠悠。
# 晴川历历汉阳树，芳草萋萋鹦鹉洲。
# 日暮乡关何处是？烟波江上使人愁

# with open("upoem.txt") as f:
#     line_list = f.readlines()
#     line_list.pop(2)
#
# with open("upoen.txt","w") as f:
#     f.writelines((line_list))



# 5.封装一个函数，可以使用mkdir的方法， 实现创建多级目录的功能

import os
def my_makedirs(path):
    path_list = path.split("/")

    for this_path in path_list:
        if not os.path.exists(this_path):
            os.mkdir(this_path)

        print(os.getcwd())
        os.chdir(this_path+"/")


my_makedirs("D:/first_level/day11/a1/b1/c1/de")




# 6. 用户输入文件名以及开始搜索的路径，搜索该文件是否存在，如遇到文件夹，则进入文件夹继续搜索

# def func(s_file,path):
#     file_list = os.listdir(path)
#
#     for file in file_list:
#         file_abs_path = path + "/" + file
#
#         if os.path.isdir(file_abs_path):
#             res = func(s_file, file_abs_path)
#             if res == True:
#                 print(f)
#                 return True
#
#         elif file == s_file:
#             print(file_abs_path)
#             return True
#
#     return False
#
# r = func("c.txt","D:\新建文件夹")



while 1:
    try:
        num = input("请输入一个整数：")
        num = int(num)
        num = num/3
    except ValueError:
        continue
    else:
        print(num)
        break