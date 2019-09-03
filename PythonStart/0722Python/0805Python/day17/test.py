"""
    学生信息: (列表 + 字典)
    [
    {"name": "张碧正",  "age": 18},
    {"name": "任思锦", "age": 17},
    ]
"""


# 将传递给该函数的参数信息, 进行打印输出
def get_info(params):
    for stu in params:
        name = stu.get("name")
        age = stu.get("age")
        print("姓名:{}, 年龄:{}".format(name, age))


p = [{"name": "任思锦", "age": 17}, ]

get_info(p)  # 相当于给函数传递参数



