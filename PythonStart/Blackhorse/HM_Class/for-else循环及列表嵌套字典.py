# 在迭代遍历嵌套的数据类型时，例如一个列表包含了多个字典
# 需求：要判断某一个字典中是否存在指定的值
# 如果存在，提示并且退出循环
# 如果不存在，再循环整体结束后，希望得到一个统一的提示

students = [
    {"name": "阿土",
     "age": 20,
     "gender": True,
     "height": 1.7,
     "weight": 75.0},
    {"name": "小美",
     "age": 19,
     "gender": False,
     "height": 1.6,
     "weight": 45.0}
]

for i in students:
    if i["name"] == "阿":
        print("存在，结束。找到了%s"%"阿土")
        break
else:
    print("列表中不存在")