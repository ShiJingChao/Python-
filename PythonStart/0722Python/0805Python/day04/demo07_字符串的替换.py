"""
    字符串的替换:
        替换: 把 '谁' 替换成 '谁'
        replace(old, new. count)
            old : 被替换的
            new : 替换为的
            count: 替换次数, 默认为全部替换
            从左到右替换指定的元素,可以指定替换次数,默认全部替换

        translate() 按照对应的关系进行替换
            参数: 对应管系
                    str.maketrans(参数1, 参数2)
                        参数1: 字符串中的字符
                        参数2: 对应着将要替换为的字符
                        参数1 和 参数2 之间: 字符一对一的关系;

"""
s = '杨紫罗云熙&杨紫李现'

# 把杨紫替换成女神
s1 = s.replace('杨紫', '女神')
print(s1)  # 女神罗云熙&女神李现

s2 = s.replace('杨紫', '女神', 1)
print(s2)  # 女神罗云熙&杨紫李现

s3 = 'i love rose'

# 按照对应的关系替换

# step1: 明确替换关系, 制作一个替换关系
m_trans = str.maketrans('love', 'hate')

# step2: 使用替换关系函数进行替换
# s3.translate(str.maketrans('love', 'hate'))  # 按照对应关系替换函数
print(s3.translate(m_trans))  # i hate rase

# 1. 有个字符串'谁是世界上最美丽的人?大镁铝李雪' 替换成 '谁是世界上最漂亮的人?大镁铝李雪'
s4 = '谁是世界上最美丽的人?大镁铝李雪'

# step1: make对应关系
m2 = str.maketrans('美丽', '漂亮')
# step2: 使用函数进行替换
print(s4.translate(m2))  # 谁是世界上最漂亮的人?大镁铝李雪

# 2. 有个字符串'谁是世界上最美丽的人?大美女李雪' 按照替换关系 '美'-->'漂', '丽' --> '亮', 执行结果是什么?
s5 = '谁是世界上最美丽的人?大美女李雪'
print(s5.translate(m2))  # 谁是世界上最漂亮的人?大漂女李雪

