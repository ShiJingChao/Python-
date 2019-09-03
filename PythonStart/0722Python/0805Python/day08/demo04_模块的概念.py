"""
    模块:
        1. 所谓模块, 就是指封装好一定功能的.py文件.
            如果想要使用某个模块,直接导入就行了.
        2. random.py 模块名就是文件名(不包含后缀)
        3. 模块名的命名规则,遵循标识符的命名规则; 变量, 函数名, 类名, 模块名

        模块的作用:
            1. 程序开发文件比较大, 都放在同一个文件中, 管理维护非常不方便,
                拆成多个模块进行管理, 方便维护;
            2. 模块可以增加程序的复用率;

        模块的分类:
            1. 自己写的;
            2. python自带的模块; random, time, datetime, sys, os....
            3. 第三方的模块; 别人写的,功能很强大,我们在程序开发的过程中,可以直接使用的;
                    自己安装到python解释器中才能够使用, cmd --> pip install 模块

        模块的导入:
            1. import 模块名
            2. import 模块名 as 别名  [注意]: 导入时起了别名, 就不能再使用模块原本的名字
            3. import 模块名1, 模块名2, ....   一次性打入多个模块(不建议使用)
            4. from 模块 import ...  从模块中导入变量, 函数, 类,...
            5. from 模块 import ... as 别名  [注意]: 导入时起了别名, 就不能再使用原本的名字
            6. from 模块 import 对象1, 对象2, 对象3, .... 一次性导入同一个模块中的多个变量, 类, 函数,...
            7. from 模块 import  *  将模块中的所有 变量, 类, 函数, 全部导入到当前模块中(不建议使用)

        [注1]: 导入模块会将被导入的模块执行一遍

        __name__ :
            1. 如果执行的是当前.py文件, 该模块的__name__ = __main__
            2. 如果当前文件作为导入模块被执行的, 该导入模块的__name__ = 模块名

        [注2]: 自定义的模块名不!要!与python自带模块名重!名!, 否则导入的会是当前你自定义的模块;

        pyc临时文件(针对自定义的模块而言):
            1. 为了提高加载模块的速度, python解释器会在__pycache__目录下缓存被导入模块编译后的pyc文件,
            之后,再次被导入时, 实际上导入的就是这个pyc的临时文件;
            2. python解释器会智能的认为,只有被import进来的文件才是需要被重用的文件,
            所以只给被导入的文件生成临时pyc文件

        __all__:
                通过 from 模块 import * 导入模块中的内容时, 可以通过__all__属性设置导入的内容;
                __all__属性为一个列表, 列表中的元素为字符串元素;
"""
# 模块的导入
# 1. import 模块名
# 使用时 需要使用 模块名.变量/方法/类
# import random
# res = random.randint(1, 10)  # [1, 10]
# print(res)

# 2. import 模块名 as 别名
# 注意: 导入时起了别名, 就不能再使用模块原本的名字
# import random as r
# res = r.randint(1, 10)
# print(res)
# res = random.randint(1, 10) NameError: name 'random' is not defined

# 3. import 模块1, 模块2, ...
# import random, time
# res1 = random.randint(1, 10)
# res2 = time.localtime()
# print(res1, res2)

# 4. from ... import ...
# from random import randint  # 变量, 函数, 类, ...
# res = randint(1, 10)
# print(res)

# 5. from ... import ... as 别名
# from random import randint as rint
# res = rint(1, 10)
# res = randint(1, 10)
# print(res)

# 6. from 模块 import 对象1, 对象2, 对象3, ...
# from random import choice, randint
# res1 = randint(1, 10)
# res2 = choice("abc")
# print(res1, res2)

# 7. from... import *
from random import *  # 函数,变量,类


