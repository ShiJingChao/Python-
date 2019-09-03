"""
3. 字符串str="ABCDEFGHIJK"，要求输出最少一个最多八个的所有组合（向后连续字母）
输出如下：
A   [0::]
AB
ABC
ABCD
ABCDEFGH
B  [1::]
BC
BCD
...
BCDEFGHI
...
K  [最后一个索引值::]
切片 ---> 字符索引值
"""
s = "ABCDEFGHIJK"  # len(s) --> 11
for x in range(0, len(s)):  # 0 ~ 10 遍历出来切片的start  [start::]
    for y in range(x+1, x+9): # 8 遍历获取stop值
        if y > len(s):  # 如果stop结束值 > 字符串的长度
            break       # 结束内层循环
        print(s[x:y:])



