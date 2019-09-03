"""
2.有名为user_info.txt的文件，其内容格式如下，写一个程序，将id为100002的用户名修改为alex li；
with as 语句
"""

with open("user_info.txt") as f:
    all_list = f.readlines()


for line in all_list:  # 遍历列表获取每行的内容
    if "100002" in line:  # 对每行的内容进行判断, 看是否包含100002这个id
        index = all_list.index(line)  # 1. 获取line的索引值
        all_list[index] = "alex li, 100002\n"  # 2. 根据索引值, 修改列表

with open("user_info.txt", "w") as f:
    f.writelines(all_list)








