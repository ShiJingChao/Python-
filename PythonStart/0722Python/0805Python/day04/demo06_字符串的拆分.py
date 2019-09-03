"""
    字符串的拆分:
        splitlines() : 按行分隔, 返回分隔后包含各行字符串的列表
        split() :
            参数1: 按照谁去切割, 切割完后,不包含切割部分
            参数2: 默认为切割所有;
                    指定了切割次数, 则按照指定的切割次数进行切割
            返回值: 列表

        partition() : 从左开始, 找到第一个切割部分, 将字符串切割成3部分, (切割部分前, 切割部分, 切割部分后)
        rpartition() : 从右开始, 找到第一个切割部分, 将字符串切割成3部分, (切割部分前, 切割部分, 切割部分后)
"""
res = "i love python".split(' ')
print(res)  # ['i', 'love', 'python']

res1 = 'i love python'.split(' ', maxsplit=1)
print(res1)  # ['i', 'love python']

res2 = 'i love python'.split(' ', maxsplit=3)
print(res2)   # ['i', 'love', 'python']

res3 = 'i love python'.partition(' ')
print(res3)  # ('i', ' ', 'love python')

res4 = 'i love python'.rpartition(' ')
print(res4)  # ('i love', ' ', 'python')

# 分别按行切割以下字符串, 看看结果, 思考为啥
s1 = "人生苦短\n我用pyton\n"
s2 = "人生苦短\n我用pyton"
s3 = """
人生苦短
我用Python
"""
# print(s1.splitlines())
print('----------------------')
result1 = s1.splitlines()
print(result1)  # ['人生苦短', '我用pyton']
print('----------------------')
result2 = s2.splitlines()
print(result2)  # ['人生苦短', '我用pyton']
print('-----------------------')
print(s3.splitlines())  # ['', '人生苦短', '我用Python']
print('------------------------')

