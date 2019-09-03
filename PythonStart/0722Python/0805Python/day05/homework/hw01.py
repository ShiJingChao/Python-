"""
1. 给定一个以下字符串：统计大写字母的个数，小写字母的个数，非字母的个数。
	str1 = "ajdkkKDKEK1343KFKiriromfkfKKRIOWJF0928398jjee11djdDJJRH"
"""

str1 = "ajdkkKDKEK1343KFKiriromfkfKKRIOWJF0928398jjee11djdDJJRH"
big_num = 0  # 记录大写字母个数
small_num = 0  # 记录小写字母个数
not_alpha_num = 0  # 记录非字母个数

for c in str1:
    if c.isupper():
        big_num += 1
    elif c.islower():
        small_num += 1
    else:
        not_alpha_num += 1

"""
for c in str1:
    if c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        big_num += 1  # 大写+1
    elif c in 'qwertyuiopasdfghjklzxcvbnm':
        small_num += 1  # 小写 + 1
    else:
        not_alpha_num += 1  # 非字母 + 1
"""

print('大写字母个数为:%d, 小写字母个数:%d, 非字母个数:%d' % (big_num, small_num, not_alpha_num))






