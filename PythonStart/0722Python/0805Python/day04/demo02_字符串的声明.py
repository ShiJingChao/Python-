"""
    IndexError: string index out of range  字符串的索引超出了范围;索引越界
    TypeError: int... str...  类型错误

    字符串:
        定义: 0-多个字符组成的一个有序的序列;
            ''  ---> 空字符串
            '孙行者'  '行者孙'  '者行孙'

        注意:
            1. 字符串一定是有序的;
            2. 字符串是不可变的数据类型; 字符串不可修改;
            *  number数值类型(int,float,bool,complex)数值类型也是不可变的数据类型

        声明的语法:
            怎么样定义一个字符串;
            1. ''  通过一对单引号定义
            2. ""  通过一对双引号定义
            3. ''' ''' 通过三对单引号
            4. 通过三对双引号定义

        字符串的索引:
            字符串中的每个字符都是有索引值的;
            索引值从左到右, 依次是0, 1, 2, 3, ....
            索引值从右到左, 依次是-1, -2, -3, -4 ,.....
            格式:
                字符串[索引值] ----> 能够获取到对应索引值的字符

            s = "abcde"
                 01234

             注意: 空格也是一个字符;
"""
s1 = 'abcde'
print(s1[2])  # c
print(s1[4])  # 4
# print(s1[5])      print(s1[5])
# IndexError: string index out of range

s2 = 'i love python'
print(s2[2])

s3 = 'gfasuykjhajfhydhfjewiurhyuewhidhyreoiuhfipohyreaufhcnvyreufhure'
print(s3[-5])  # f
# print(s3[-500])  # IndexError: string index out of range

# 验证字符串的不可变性;
s4 = '念念不忘 必有回响'
space_char = s4[3]
print(space_char)  # 通过索引获取一个字符

# 尝试通过索引更改一个字符
# TypeError: 'str' object does not support item assignment
# s4[3] = '想'  # 将'想'赋值给字符串s4中的索引值为3的字符元素
print(s4)

# a = 2
# print(id(a))  # 8791176605984
# a = 3
# print(id(a))  # 8791176606016