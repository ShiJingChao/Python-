"""
    字符串的查找方法
        find() : 查找, 返回从左开始第一个指定字符的索引值, 没找到返回-1
        rfind(): 查找, 返回从右开始第一个指定字符的索引值, 没找到返回-1
        index(): 查找, 返回从左开始第一个指定字符的索引值, 没有找到报错ValueError
        rindex(): 查找, 返回从右开始第一个指定字符的索引值, 没有找到报错ValueError

        count() : 计数, 返回指定字符在字符串中的个数
"""
s1 = '0123456789'
res1 = s1.find('6')
r1 = s1.index('6')
print(res1, r1)  # 6

s2 = 'abcdefghij'
res2 = s2.find('g')
r2 = s2.index('g')
print(res2, r2)  # 6

res3 = s2.find('cde')
r3 = s2.index('cde')
print(res3, r3)  # 2

s3 = 'abc000abc111abc222'
res4 = s3.find('bc')
r4 = s3.index('bc')
print(res4, r4)  # 1

res5 = s3.find('z')
# r5 = s3.index('z')   # ValueError: substring not found
# print(res5, r5)  # -1

print("----------------")

s = 'abcabc'
print(s.rfind('b'))  # 4
print(s.rindex('a'))  # 3

print(s.rfind('z'))  # -1
# print(s.rindex('z'))  # ValueError

print(s.count('bc'))  # 2



