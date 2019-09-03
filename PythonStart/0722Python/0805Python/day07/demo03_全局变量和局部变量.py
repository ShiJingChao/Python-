"""
    局部变量: 在函数内部声明的变量, 只在函数中有效;
    全局变量: 在模块中声明的变量, 在整个模块中有效;
    -----------------------------
    全局变量是不可变数据类型, 函数无法修改全局变量的值;
    全局变量是可变数据类型时, 函数可以修改全局变量的值;
        (如果给函数传递的参数是 全局可变类型数据, 在函数多次调用的过程中, 全局变量会发生改变;)

"""

name = "张三"  # 全局变量, 在整个模块中(整个程序)中有效
def get_name(name):
    name = "李四"  # 局部变量, 在函数内部有效
    age = 18  # 局部变量,

get_name(name)  # 实参: 张三
print(name)
# print(age)

print("------------------------------")

list1 = [1, 2, 3]

def get_num(a=list1):  # 形参为a, 在函数定义时给形参a赋默认值
    a.append(4)
    return a

print(get_num())  # [1,2,3,4]
print(list1)  # [1,2,3,4]
print(get_num())  # [1,2,3,4,4]
print(list1)  # [1,2,3,4,4]
print(get_num())  # [1,2,3,4,4,4]
print(list1)  # [1,2,3,4,4,4]

print("===========================")

list2 = [1,2,3]

def get_num_two(a):  # 形参a --> 位置参数
    a.append(4)
    return a


print(get_num_two(list2))  # [1,2,3,4]
print(list2)  # [1,2,3,4]
print(get_num_two(list2))  # [1,2,3,4,4]
print(list2)  # [1,2,3,4,4]
print(get_num_two(list2))  # [1,2,3,4,4,4]
print(list2)   # [1,2,3,4,4,4]






