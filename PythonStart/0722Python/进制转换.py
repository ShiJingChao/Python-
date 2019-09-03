# # 十进制转换为其他进制的函数
#
# a = 5454
# print(a, '转换十六进制为：', hex(a))
# print(a, '转换为八进制为：', oct(a))
# print(a, '转换为二进制为：', bin(a))
# print('转换进制后的类型为：', type(bin(a)))
#
# # 其他进制转换为十进制
#
# a = int('11', 2)
# print('二进制转换为十进制为：', a)
# b = int('11', 8)
# print('八进制转换为十进制：', b)
# c = int('11', 16)
# print('十六进制转换为十进制：', c)

# print(int("11", 16))

# a = int('11010110', 2)
# # b = int('101101', 2)
# # c = int('1001100', 2)
# # print(a)
# # print(b)
# # print(c)
# #
# # print(hex(214))
# # print(hex(45))
# # print(hex(76))
# #
# # print(oct(214))
# # print(oct(45))
# # print(oct(76))

# 如果子类是pass 会继承父类，子类有值得话，就不会继承父类
# class Parent(object):
#     x = 1
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass
#
#
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)



dict = {1:2,2:3,3:4}
print(dict[4])