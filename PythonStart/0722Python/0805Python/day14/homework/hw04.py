"""
4.有名为upoem.txt的文件，其内容如下，请删除第三行；
昔人已乘黄鹤去，此地空余黄鹤楼。
黄鹤一去不复返，白云千载空悠悠。
晴川历历汉阳树，芳草萋萋鹦鹉洲。
日暮乡关何处是？烟波江上使人愁。
"""

with open("upoem.txt") as f:
    line_list = f.readlines()
    line_list.pop(2)

with open("upoem.txt", "w") as f:
    f.writelines(line_list)





