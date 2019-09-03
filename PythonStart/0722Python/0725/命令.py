# chat = open('chat.txt', 'w')
# chat.write('new new')
#
# chat.close()
# chat = open('chat.txt', 'a')
# chat.write('append append')
# chat.close()
# chat = open('chat.txt', 'r')
# r = chat.read()
# print(r)
import os

for i in range(1, 31):
    name = str(i)
    path = "D:/songs/"
    f = os.path.exists(name)
    if not f:
        os.mkdir(path+name)
        print(i, end='\t')
        if i % 6 == 0:
            print()
    else:
        print("创建失败")

# 要找到文件位置打开

# for i in range(100):
#     chat = open('chat.txt', 'w')
#     chat.close()
# from coverage.files import os
#
# flist = ['sport','news']
# for i in flist:
#     fn =
#     if os.path.exists(fn) != True:
#         mkdir(fn)

# import os
#
# for i in range(1, 101):
#     if os.path.exists(i):
#         os.remove(i)
