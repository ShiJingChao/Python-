"""
3、定义一个函数func(listinfo) listinfo:为列表，listinfo = [133, 88, 24, 33, 232, 44, 11, 44]，
返回列表小于100，且为偶数的数

filter(): 参数1:函数, 定义过滤的规则; 参数2: 被过滤的容器
map():
"""

# 满足需求的代码实现一下, 在代码执行的过程中, 捕获有可能发生的异常


# 定义一个过滤的规则:
# 参数, 列表中的每个元素
def filter_rule(x):   # x -->列表中的元素
    if x < 100 and x % 2 == 0:
        return True
    else:
        return False


def func1(list_info):
    try:
        res_list = list(filter(filter_rule, list_info))
    except:
        return "发生了异常"
    else:
        return res_list


r = func1([133, 88, 24, 33, 232, 44, 11, 44])
print(r)  # 发生了异常 / res_list

print("---------------------------------")


def func2(info_list):
    res_list = []
    for element in info_list:
        if element < 100 and element % 2 == 0:
            res_list.append(element)
        else:
            raise Exception(str(element))

    return res_list


# func2([133, 88, 24, 33, 232, 44, 11, 44])

print("===================================")


def func3(info_list):  # [133, 88, 24, 33, 232, 44, 11, 44]
    n = 0  # 0-7
    res_list = []  # 满足条件的列表
    while n < len(info_list):
        try:
            element = info_list[n]  # 133, 88, 24, 33, ....44

            if element < 100 and element % 2 == 0:
                res_list.append(element)
                n += 1
            else:
                n += 1
                raise Exception(str(element))
        except Exception as e:
            print("异常:", str(e))
            continue
    return res_list


func3([133, 88, 24, 33, 232, 44, 11, 44] )



