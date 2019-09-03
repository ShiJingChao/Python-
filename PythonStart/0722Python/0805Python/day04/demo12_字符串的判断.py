"""
    字符串的判断
"""
# isalnum  判断是否全部由数字或者字母组成的
print('12345'.isalnum())  # True
print('123abc'.isalnum())  # True
print('****abc123'.isalnum())  # False

# isalpha
print('abc'.isalpha())  # True
print('python1'.isalpha())  # False

# isdigit
print('123'.isdigit())  # True
print('123cab'.isdigit())  # False

# isupper  字母部分是否都是大写
print('ABC'.isupper())  # True
print('123ABC'.isupper())  # True
print('123abc'.isupper())  # False

# islower 字母部分是否都是小写
print('abc'.islower())  # True
print('123abc'.islower())  # True
print('Abc'.islower())  # False

# istitle 判断是否每个单词的首字母是大写的
print('I Love*Python'.istitle())  # True
print('i love Python'.istitle())  # False

# isspace 判断是否全部由空白字符组成, 空白字符: 空格, \t, \n
print(''.isspace())  # False
print('      '.isspace())  # True
print('\t'.isspace())  # True
print('\n'.isspace())  # True

# startswith 判断是否以...开头
print('love love python'.startswith('l'))  # True
print('love love python'.startswith('love'))  # True
print('love love python'.startswith('lova'))  # False

# endswith 判断是否以...结尾
print('love love python'.endswith('n'))  # True
print('love love python'.endswith('python'))  # True
print('love love python'.endswith('  python'))  # False