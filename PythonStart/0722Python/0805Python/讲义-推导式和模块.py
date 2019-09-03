# 推导式包括 列表推导式，字典推导式，集合推导式
# 列表推导式的基本格式：
# 变量名 = [表达式 for 变量 in列表] 或者
# 变量名 = [表达式 for 变量 in 列表 if 条件]
# 练习1 将 lst中的每一个元素进行平方后放入到一个新列表中
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# lst_new = [i * i for i in lst]
# print(lst_new)

# 使用函数
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
#
# def square(i):
#     return i * i
#
# lst_new = [square(i) for i in lst]
# print(lst_new)


# 练习2 求出lst中是奇数的值，然后放到一个新列表中
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# lst_new = [i for i in lst if i %2 != 0]
# print(lst_new)

# 练习3 求列表中所有大于2的偶数进行平方计算
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# lst_new = [i*i for i in lst if i>2 and i %2 == 0]
# print(lst_new)

# 练习4 将一个嵌套列表转换成一个一维列表
# lst = [[1,2,3],[4,5,6],[7,8,9]]
# 转换成 lst2 = [1,2,3,4,5,6,7,8,9] 使用列表推导式
# lst = [[1,2,3],[4,5,6],[7,8,9]]
# lst2 = [i for lst1 in lst for i in lst1]
# print(lst2)

# 现有一列表 lst = [[1,2,3],[4,5,6],[7,8,9]],
# 要求取出1/4/7 和1/5/9元素
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lst1 = [lst[i][0] for i in range(len(lst))]
# print(lst1)
# lst2 = [lst[i][1] for i in range(len(lst))]
# print(lst2)

# 面试题
# 求a[0](2),a[1](2),a[2](2)的值
# a = [lambda x:x*i for i in range(3)]
# a = [lambda x:x*i for i in range(3)]
# print(a[0](2),a[1](2),a[2](2))
# a[0](2) == 4
# a[1](2) == 4
# a[2](2) == 4

# (二) 字典推导式
# 语法和列表差不多
# 练习：将字典中的key和value进行对换
# dic = {'a':10,'b':11}
# new_dic = {key:value for value,key in dic.items()}
# print(new_dic)

# (三) 集合推导式
# 和列表推导式相似，只是用{}代替[]
# 练习列表中每个值的平方，自带去重功能
# squared = {i*i for i in [1,-1,2]}
# print(squared)
# --------------------------------------------------------------------------
# 模块
# 模块导入的方式有多种
# import 模块名    # 直接导入模块
# import 模块名 as 别名
# import 模块名1，模块名2，...一行导入多个模块（不推荐）
# from ...import ...    # 局部导入
# from ... import ... as 别名
# from ... import 功能1，功能2
# from 模块 import * 导入所有

# pyc文件为了提高加载模块，python解释器会在__pycache__目录下，缓存每个模块编译后的版本，之后再被导入时，就是这个.pyc的临时文件

# 把模块当脚本运行
# 可以通过模块的全局变量__name__来查看模块名：
# 当做运行脚本：
# __name__ 的值 等于‘__main__’
#     当做模块导入：
# __name__的值等于模块名：
# 作用：用来控制.py文件在不同的应用场景下执行不同的逻辑
# print(__name__)
# if __name__ =='__main':
#     pass

# random模块
# random.random() 产生大于0 小于1的小数  左闭右开
# random.uniform() 产生指定范围的随机小数
# random.randint() 产生指定范围的整数  左闭右闭
# random.randrange(start,stop,step) 产生 start，stop范围内的整数，左闭右开
# random.choice(lst) 随机返回序列中的一个数据  字典和集合不可用
# random.shuffle(lst) 打乱列表顺序    元组，字典和集合不可用
# sys 模块
import time
ret = time.time()
print(ret)
ret1 = time.gmtime(ret)
print(ret1)
