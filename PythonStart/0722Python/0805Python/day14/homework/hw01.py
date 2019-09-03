"""
1.有名为user_info.txt的文件，其内容格式如下，写一个程序，删除id为100003的行；
分析:
    1. 读取文件内容, readlines() ---> list
    2. list --> 某个行(某个元素) 从列表中删除满足条件的行
    3. 重写入文件中去
"""

f = open("user_info.txt", "r")
all_list = f.readlines()
f.close()

for line in all_list:  # 遍历获取每一行的内容
    if "100003" in line:   # 将每一行的内容进行判断, 看是否包含"100003"
        all_list.remove(line)  # 如果包含, 将此行从列表中删除


f_res = open("user_info.txt", "w")
f_res.writelines(all_list)
f_res.close()


