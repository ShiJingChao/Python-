"""
    集合中的数学运算
        交集: 取的公共部分 &  intersection

        并集: 取的是所有部分,不包括重复数据 |  union

        差集: 第一个集合有的,第二个集合没有的 - difference

        反交集: 跟交集反着 取的非公共部分 ^  symmetric_difference

        子集: 判断某个集合是不是另一个集合的子集  set1 < set2 issubset

        超集:

"""
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 & set2)  # {3, 4}
print(set1.intersection(set2))

print(set1 | set2)  # {1, 2, 3, 4, 5, 6}
print(set1.union(set2))

print(set1 - set2)  # {1, 2}
print(set1.difference(set2))

print(set1 ^ set2)  # {1, 2, 5, 6}
print(set1.symmetric_difference(set2))

print(set1 < set2)  # False
print(set1.issubset(set2))

print({1, 2} < {1, 2, 3, 4})  # True

print(set2 > set1)   # False
print(set2.issuperset(set1))

print({3, 4, 5, 6} > {3, 6})  # True
