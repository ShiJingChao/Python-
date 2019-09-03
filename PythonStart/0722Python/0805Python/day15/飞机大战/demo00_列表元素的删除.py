a_list = [1, 2, 44, 2, 50, 33, 71, 100]

# 删除 33  remove(33)
# for x in a_list:
#     print(x)
#     if x == 33 or x == 2:
#         a_list.remove(x)
#
# print(a_list)
"""
第一次: x=1, 
第二次: x=33,  remove(33)   a_list少了一个元素
第三次: x=44, ....
"""

# 遍历列表的过程中, 不建议删除元素;

b_list = a_list
b_list = a_list.copy()
