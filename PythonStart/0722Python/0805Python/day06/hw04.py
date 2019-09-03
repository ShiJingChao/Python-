"""
5.ECALIYHWEQAEFSZCVZTWEYXCPIURVCSWTDBCIOYXGTEGDTUMJHUMBJKHFGUKNKN
每个字母出现的次数
	提示：字典{字母：count}
"""
s = "ECALIYHWEQAEFSZCVZTWEYXCPIURVCSWTDBCIOYXGTEGDTUMJHUMBJKHFGUKNKN"

"""
step1: 获取字符串中包含的字母
step2: 对这些字母进行计数
step3: 将结果存储到字典中
在不考虑代码执行效率的问题上,可以不用去重,因为字典相同的key会进行覆盖;
"""
dict1 = {}

for c in s:  # 遍历获取每一个字符元素
    c_count = s.count(c)  # 计算变量字符c在字符串中出现的次数
    dict1[c] = c_count  # 字典里,相同的key值会进行覆盖;

print(dict1)
"""
{'E': 5, 'C': 5, 'A': 2, 'L': 1, 'I': 3, 'Y': 3, 'H': 3, 'W': 3, 'Q': 1, 'F': 2, 'S': 2, 'Z': 2, 'V': 2, 'T': 4, 'X': 2, 'P': 1, 'U': 4, 'R': 1, 'D': 2, 'B': 2, 'O': 1, 'G': 3, 'M': 2, 'J': 2, 'K': 3, 'N': 2}
"""


"""
6.动态给字典输入五个姓名与手机号
"""
dict2 = {}
for x in range(5):   # 0,1,2,3,4
    name = input("请输入您的姓名:")
    tel = input("请输入您的电话")
    dict2[name] = tel  # 给字典中添加键值对

print(dict2)




