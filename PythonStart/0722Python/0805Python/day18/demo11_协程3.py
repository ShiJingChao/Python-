"""
    协程:
        生产者,消费者
"""


def customer():
    res = 0  # 每次生成器对象, 获取到的值
    while True:
        r = yield res   # 希望生产者使用send传递过来啥, 下一次就返回啥
        res = r


def product(g):
    for i in range(50):  # 0,1,2,3....49
        if i == 0:
            res = g.__next__()
        else:
            res = g.send(i)
        print("\t生产者生产的值是: {}".format(i))
        print("消费者消费的值: {}".format(res))


g = customer()  # g 生成器对象
product(g)

# g.__next__()  # 0
# g.send(666)  # 1. 获取数据  2. 传给上一次yield调用的位置一个值









