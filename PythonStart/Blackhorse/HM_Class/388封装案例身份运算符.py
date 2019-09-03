# 身份运算符用于比较两个对象的内存地址是否一致————是否对同一个对象的引用
# 在Python中针对None比较时，建议使用is判断
# is 与 == 区别
# is 用于判断两个变量引用对象是否为同一个
# ==用于判断引用的变量的值是否相等

a = [1, 2, 3]
b = [1, 2, 3]
c = 1
print(id(a[0]))
# print(id(a[1]))

print(id(b[0]))
# print(id(b[1]))

print(id(c))
print(b[0] is a[0])  # True
print(id(c) is id(b[0]))  # False
print(id(a[0]) is id(b[0]))  # False
