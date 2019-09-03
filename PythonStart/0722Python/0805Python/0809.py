# list = [['a','b'],['abc',100],'abc',100,[0.9,0.7]]
# for i in list:
#     if type(i) != type(list):
#         print(i)
#     elif type(i) == type(list):
#         for j in i:
#             print(j)
# list1 = [['a','b'],['abc',100],'abc',100,[0.9,0.7]]
# for i in list1:
#     if isinstance(i,list):
#         for j in i:
#             print(j)
#     else:
#         print(i)

# list1 = [1,2,3]
# # list2 = [4,5,6]
# # print(id(list1))
# # print(id(list1[0]))
# # print(id(list1[1]))
# # print(id(list1[2]))
# # print(id(list2))
# # print(id(list2[0]))
# # print(id(list2[1]))
# # print(id(list2[2]))
# list3 = [100,200]
# list4 = [100,200,list3]
# print(id(list3))
# print(id(list4))
# list3[1] = 500
# print(id(list3))
# print(id(list4))

# a = {"1":12,"2":"12"}
# a.setdefault("3",4)
# print(a)

# nums = [2, 1, 2, 1, 3, 1, 4, 5, 3]
# for i in nums:
#     if nums.count(i) % 2 != 0:
#         print(i, end='')
print(3//3)