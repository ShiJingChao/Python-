# 包是一个包含多个模块的特殊目录
# 目录下有一个特殊的文件 __init.py
# 包名的命名方式和变量名一致，小写字母+_

# CLASS 441 封装模块、设置 __init__和外界导入包
# 要在外界使用包中的模块，需要在__init__中指定对外界提供的模块的列表
#例如在 __init__中  导入
# from . import 模块名   # . 为当前目录

import 黑马.class440包

黑马.class440包.send_message.send("hello")
txt = 黑马.class440包.receive_message.receive()
print(txt)