"""
    with
        在文件操作时, 使用with语句, 可以自动关闭掉使用完毕的文件, 不需要手动调用close方法

        语法:
            with open(路径, 模式, 编码) as 对象名:
                文件的操作.....
"""


with open("dragon.txt") as f:
    s = f.read()
    print(s)

print("-----over-----")





