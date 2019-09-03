"""
    random 随机数模块
        python自带的模块

        1. random.randint(a, b) : 在某个范围内随机产生一个整数;
                                    [a, b], 能取到a, 也能取到b
        2. random.random() : 随机产生一个0-1之间的浮点数
                                    [0, 1), 0可以取到, 1取不到
        3. random.uniform(a, b) : 在某个范围内随机产生一个实数;
                                    [a, b], 能取到a, 也能取到b
        4. random.randrange(start, stop, step) : 在某个范围内随机产生一个整数
                                    [start, stop), 能取到start, 取不到stop
        5. random.choice(sequence) : 随机返回序列中的某个数;
        6. random.shuffle() : 打散,打乱,混序
                                注: 该函数无返回值, 将打乱顺序后的结果直接作用于原列表
        7. random.sample(population, k) : 取样
                                population: 取样的对象
                                k : 取样个数
"""
import random

r1 = random.random()
print(r1)

r2 = random.randint(1, 10)
print(r2)

r3 = random.uniform(1, 10)
print(r3)

r4 = random.randrange(0, 11, 5)
print(r4)

r5 = random.choice(["rose", "黄瓜丝", "面条"])
print(r5)

list1 = [1, 2, 3, 4, 5]
r6 = random.shuffle(list1)  # None
print(list1)  # [4, 1, 2, 3, 5]

r7 = random.sample(list1, 3)
print(r7)  # [3, 2, 5]