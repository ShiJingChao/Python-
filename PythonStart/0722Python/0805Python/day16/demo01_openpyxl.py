"""
    openpyxl:
        1. WorkBook
        2. WorkSheet
        3. cell
"""
import openpyxl, random
# 随机点名


def call_somebody():
    excel = openpyxl.load_workbook(r"C:\Users\ThinkPad\Desktop\0805python学员名单.xlsx")
    sheet = excel.active
    name_list = []  # 装着所有的人名
    for name in range(1, 49):
        cell = sheet["C" + str(name)]  # "C" + "47"
        name_list.append(cell.value)

    return random.choice(name_list)


print(call_somebody())


