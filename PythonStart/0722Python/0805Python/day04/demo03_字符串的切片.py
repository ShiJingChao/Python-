"""
    1. 字符串的拼接
        + : "abc" + "def"  --->  "abcdef"
        * : "李现" * 3 ---> "李现李现李现"

    2. 字符串的长度
        容器: 字符元素
        python的内置函数len(): 获取变量的长度;

    3. 切片:slice
        通过切片操作获取字符串中的一部分数据;
        格式:
            字符串[start : stop : step]

            start: 起始值, 索引值
            stop: 结束值, 索引值
            step: 步长, 整数

        * 注意: 1. 切片中的::必须写
                2. step默认为1
                3. start默认是从头开始切;
                4. stop默认是切到最后一个字符
"""
s = '人生苦短 我用python'
print(len(s))  # 13

s1 = 'i love python'
#  step 步长为正数
print(s1[2:6:1])  # love
print(s1[2:6:])  # love
print(s1[0::2])  # 从第一个字符开始到最后一个字符,每两个字符取一个
print(s1[::2])  # start默认是从头开始切; stop默认是切到最后一个字符

s2 = '0123456789'
# 1. 截取下标(索引)是从2-5的字符串
print(s2[2:6:])
# 2. 截取下标从2开始到末尾的字符串
print(s2[2::])
# 3. 截取字符串开始到5的位置, 不包含5
print(s2[0:5:])
print(s2[:5:])
# 4. 截取完整的字符串
print(s2[::])
# 5. 从开始位置, 每隔一个字符截取
print(s2[::2])
# 6. 从索引1开始, 每隔一个字符截取
print(s2[1::2])
# 7. 截取从2到末尾的前一个字符串
print(s2[2:9:])
print(s2[2:len(s2)-1:])
print(s2[2:-1:])
# 8. 截取末尾2个字符串
print(s2[8::])
print(s2[-2::])

# step 步长为负数
# 9. 反转字符串
print(s2[::-1])
print(s2[9::-1])
# 10. 截取出'97531'这个字符串
print(s2[::-2])




