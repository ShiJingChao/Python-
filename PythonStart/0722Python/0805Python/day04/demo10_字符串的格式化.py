"""
    字符串的格式化:
        占位符 %
        %d : 给int类型的数据占位
        %f : 给float类型的数据占位
                其中: 保留小数点后一位  %.1f  or  %.f
                      保留小数点后两位  %.2f
                      ..... 以此类推......
        %s : 给str类型的数据占位
"""
# 1. 乘法算式 106 * 9 = 54
s1 = '%d * %d = %d' % (106, 9, 106*9)
print(s1)  # 106 * 9 = 954

# 2. 除法算式  333 / 17 = ?
s2 = '%d / %d = %f' % (333, 17, 333/17)
print(s2)  # 333 / 17 = 19.588235

s3 = '%d / %d = %.3f' % (333, 17, 333/17)
print(s3)  # 333 / 17 = 19.588

# 3.
s4 = '我最大的希望近期实现的愿望:%s' % '发大财'   # 只有一个占位符时, 此括号可以省略
print(s4)  # 我最大的希望近期实现的愿望:发大财

s5 = '我今天进行了体检, 我的体脂率高达33%'  # 此时%没有任何特殊的含义, 就是一个字符
print(s5)  # 我今天进行了体检, 我的体脂率高达33%







