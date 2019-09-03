"""
    字典的其他操作
        for.. in..
        in..
        not in..

        综上: in和not in 判断的是 元素 是否在字典的键里;
"""

if 'a' in 'abc':
    print("字符在字符串里")

if 'a' in ["a", "b", "c"]:
    print("元素在列表里")

if "a" in ("a", "b", "c"):
    print("元素在元组里")


if "name" in {"name": "小星星"}:  # 判断是否在字典的key中
    print("key在字典里")  # key在字典里

if "小星星" in {"name": "小星星"}:
    print('小星星在字典里')

if "小星星" in {"name": "小星星"}.values():
    print('value在字典里')

if "age" not in {"name": "小星星"}:
    print('年龄不在字典的key里')
