"""
    字符串的修饰:
        center : 居中, 让字符串在指定的长度居中; 默认填充空格;可以指定填充的字符;
                如果填充的字符不对称, 右短左长
        ljust : 左对齐, 让字符串在指定的长度左对齐, 默认填充空格, 可以指定填充的字符;
        rjust : 右对齐, 让字符串在指定的长度右对齐, 默认填充空格, 可以指定填充的字符
        zfill : 将字符串填充到指定的长度, 不足的地方用0从左开始填充
        strip : 默认去除两边空格, 去除内容可以指定
        lstrip : 默认去除左边的空格, 去除内容可以指定
        rstrip : 默认去除右边的空格, 去除内容可以指定
"""
s = 'python'  # 长度 --> 6

# 1. 居中
print(s.center(10))  # 指定长度居中,默认填充空格   python
print(s.center(10, '*'))  # 指定填充的字符 **python**

# 将字符串s, 指定长度为9居中, 指定填充字符为'+'
print(s.center(9, '+'))  # ++python+
print(s.center(3))  # python

print(" --------------------------")
# 2. 左对齐
print(s.ljust(10))  # python    默认填充空格
print(s.ljust(10, '$'))  # python$$$$  指定填充方式

# 3. 右对齐
print(s.rjust(10))  # 指定长度为10, 默认填充方式空格    python
print(s.rjust(10, '@'))  # 指定长度为10, 指定填充方式@  @@@@python

# zfill  将字符串填充到指定长度, 不足的地方用0从左开始补充
print(s.zfill(10))  # 0000python

# 默认去除两边空格, 去除内容可以指定
s1 = '  i love python  '
print(s1.strip())  # i love python
print(s1.lstrip())  # i love python  去除左边的空格
print(s1.rstrip())  #   i love python 去除右边的空格

s2 = '~~~life is short~~~'
# 去除两边的波浪线  life is short
print(s2.strip('~'))
# 去除左边的波浪线  life is short~~~
print(s2.lstrip('~'))
# 去除右边的波浪线  ~~~life is short
print(s2.rstrip('~'))


