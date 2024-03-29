"""
   元组:tuple
        1. 定义:
            python的基础数据类型之一;
            用于存储一组数据的有序序列, 一旦创建, 元组中的各个元素不允许修改;

        2. 特点:
            1. 元组有序;
            2. 元组是不可变的数据类型;不可修改;
            3. 元组中可以存储重复的数据;
            4. 元组中可以同时存储不同数据类型的数据;

        3. 语法:
            (元素1, 元素2, 元素3,...)
            注意:
                (100)  --> int
                100,  ---> tuple
                (100,) ---> tuple

        4. 索引:
            元组的索引(下标), 与列表和字符串一样一样的;

        5. 切片:
            通过切片,可以获得一个新的元组对象;

        6. 拼接:
            +  拼接
            *  自拼

        7. 访问多维元组:
            (
                (1, 2),
                ("a", "b")
            )

        8. 序列的解包
            *m, n = ('abc', '100', 'A')
                m --> ['abc', '100']
                n --> 'A'

            *m, n = ("a",)
                m --> []
                n --> 'a'
"""
t1 = ('韩商言', '老韩', '韩商言')
print(t1)  # ('韩商言', '老韩', '韩商言')
print(type(t1))  # <class 'tuple'>

t2 = (100)
print(t2)  # 100
print(type(t2))  # <class 'int'>

t3 = (100,)
print(t3)  # (100,)
print(type(t3))  # <class 'tuple'>

t4 = 100,
print(t4)  # (100,)
print(type(t4))  # <class 'tuple'>

print(t1[1])  # 老韩
print(t1[-2])  # 老韩

t5 = (0, 1, 2, 3, 4, 5)

# (4, 2, 0)
t6 = t5[-2::-2]
print(t6)

# 元组的拼接
print(t5 + t6)  # (0, 1, 2, 3, 4, 5, 4, 2, 0)

# 元组的自拼
print(t1 * 3)  # ('韩商言', '老韩', '韩商言', '韩商言', '老韩', '韩商言', '韩商言', '老韩', '韩商言')

# 遍历多维元组
t7 = (
    (100, 200),
    "鱿小鱼",
    ("a", 18)
)
for x in t7:
    if isinstance(x, tuple):
        for y in x:
            print(y)
    else:
        print(x)

print("~~~~~~~~~~~~~~~~")

# t7[1] = "佟年"  # TypeError: 'tuple' object does not support item assignment



