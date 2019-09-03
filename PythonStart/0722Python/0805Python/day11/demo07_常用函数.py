"""
    isinstance()
            功能: 判断是否是某指定类的对象
            isinstance(对象, 类)
            isinstance(对象, (类1, 类2, 类3))
            返回值: bool

    issubclass():
            功能: 判断某个类是否是指定类的子类
            issubclass(子类, 父类)
            issubclass(子类, (父类1, 父类2, 父类3))
            返回值: bool

"""

print(isinstance(True, bool))  # True  bool --> int --> object
print(isinstance(True, int))  # True  int --> object
print(isinstance(True, float))  # False  float --> object
print(isinstance(True, (str, list, int)))  # True

print(bool.__mro__)  # (<class 'bool'>, <class 'int'>, <class 'object'>)
print(bool.__bases__)  # (<class 'int'>,)

print(issubclass(bool, int))  # True
print(issubclass(bool, object))  # True
print(issubclass(bool, set))  # False
print(issubclass(bool, (str, list, int)))  # True

