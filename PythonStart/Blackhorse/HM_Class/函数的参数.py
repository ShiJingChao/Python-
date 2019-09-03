# Class 348
# 在函数内部，针对参数使用赋值语句，不会影响调用函数时传递的实参变量
# 无论传递的参数是可变还是不可变
# 只要针对参数使用赋值语句，会在函数内部修改局部变量的引用，不会影响到外部变量的引用

# CLASS 350 函数的参数
# 在参数内部 列表使用+=本质上等于调用expend方法，而不是计算相加后的结果

# CLASS 351 缺省参数
# 定义函数时，可以给某个参数指定一个默认值，具有默认值的参数就叫做缺省参数
# 调用函数时，如果没有传入缺省参数的值，则在函数内部使用定义函数时指定的参数默认值
# 函数的缺省参数，将常见的值设置为参数的缺省值，从而简化函数的调用
# gl_num_list = [6, 3, 9]
# 默认就是升序，因为这种应用需求更多
# gl_num_list.sort()
# print(gl_num_list)

# 只有当需要降序排序时，才需要传递‘reverse’参数
# gl_num_list.sort(reverse=True)
# print(gl_num_list)

# CLASS 353 缺省参数的注意事项
#   必须保证带有默认值的缺省参数在参数列表末尾
#   在调用函数时，如果有多个缺省参数，
#   需要指定参数名，这样解释器才知道参数逇对应关系

# CLASS 354 多值参数
#   有时可能需要一个函数能够处理的参数个数是不确定的，这个时候，就可以使用多值参数（多出现在框架里）
#   python中有两种多只参数：
#   参数名前增加一个*可以接收元组
#   参数名前增加两个*可以接收字典

# CLSS 355 多值参数案例——计算任意多个数字的和

# 需求：1.定义一个函数 sum_numbers,可以接收的任意多个整数
#      2.功能要求，将传递的所有数字累加并且返回累加结果

# def sum_numbers(*args):
#     '''求和'''
#     num = 0
#     # 遍历args元组顺序求和
#     for n in args:
#         num += n
#     return num
#
# print(sum_numbers(1, 2, 3, 4))

# CLASS 356 元组和字典的拆包
# def demo(*args, **kwargs):
#     print(args)
#     print(kwargs)


# 元组变量/字典变量
# gl_nums = (1, 2, 3)
# gl_dict = {"name": "小明", "age": 18}
# 拆包语法：简化元组变量/字典变量的传递
# demo(gl_nums,gl_dict)   # 会将参数全部传给元组
# demo(*gl_nums, **gl_dict)  # 拆包

# CLASS 357 函数的递归

# 函数调用自身的编程技巧称为递归
# 递归函数的特点
# 特点：
# 一个函数内部调用自己
#   函数内部可以调用其它函数，当然在函数内部也可以调用自己
# 代码特点
# 函数内部的代码是相同的，知识针对参数不同，处理的结果不同
# 当参数满足一个条件时，函数不再执行
#   这个非常重要，通常被称为递归的出口，否则会出现死循环
# 示例代码
# def sum_numbers(num):
#     print(num)
#     #递归的出口很重要，否则会出现死循环
#     if num ==1:
#         return
#     sum_numbers(num-1)
# sum_numbers(3)

# 递归实现数字累加
# def sum_numbers(num):
#     if num ==1:
#         return 1
#     temp = sum_numbers(num-1)
#     return num+temp
# sum = sum_numbers(100)
# print(sum)