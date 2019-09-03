"""
    1. 字符串的遍历:
        依次获取字符串中的每个字符元素;

        for 字符元素 in 字符串:
                print(字符元素)

    2. 字符串的解包
        一次性将字符串中的每个字符赋值给不同的变量;
        保证: 字符串的长度和解包的变量数量相等;
"""
# = 赋值运算符: 把等号右边的赋值给等号左边
x = 3
y = "abc"
a, b, c = "孙悟空"  # 把'孙'赋值给a, 把'悟'赋值给b, 把'空'赋值给c
print(a)
print(b)
print(c)

# m, n, p, q = "猪悟能"  # ValueError: not enough values to unpack (expected 4, got 3)

# m, n = '沙悟净'  # ValueError: too many values to unpack (expected 2)


