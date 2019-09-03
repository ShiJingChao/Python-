# 单例设计模式
# __new__方法
# 使用设计模式是为了可重用代码，让代码更容易被他人理解、保证代码的可靠性
# 目的——让类创建的对象，在系统中 只有唯一的一个实例
# 每一次执行 类名（）返回的对象，内存地址是相同的
# 应用场景
# 音乐播放对象、回收站对象、打印机对象

# CLASS-419
# _new__方法
# 由基类提供的内置的静态方法，主要作用为：
# 1）在内存中为对象分配空间
# 2）返回对象的引用
# 重写 __new__ 方法的代码非常固定！！
# 重写 __new__ 方法一定要return super().__new__(cls)
# 否则Python的解释器得不到分配了空间的对象引用，就不会调用对象的初始化方法
# 注意： __new__是一个静态方法，在调用时需要主动传递cls参数

# CLASS 420-重写__new__方法
# class MusicPlayer:
#
#     def __new__(cls, *args, **kwargs):
#         # 1.创建对象时，new方法会被自动调用
#         print("创建对象，分配空间")
#         # 为对象分配空间
#         super.__new__(cls)
#         # 返回对象的引用
#         return super().__new__(cls)
#
#     def __init__(self):
#         print("播放器初始化")


# 创建播放器对象
# player = MusicPlayer()
# print(player)


# CLASS 421 单例  # CLASS 422-单例设计模式代码实现
# 单例--让类创建的对象，在系统中只有唯一的一个实例
# 1.定义一个类属性，初始值是None，用于记录单例对象的引用
# 2.重写__new__方法
# 3.如果类属性 is None ，调用父类方法分配空间，并在类属性中记录结果
# 4.返回类属性中记录的对象引用

# 单例相当于重写__new__方法 ，
# 给创建的类的__new__中增加了判断条件，
# 若类未被实例化，就没有实例获得内存区域
# 第一次实例化后，第一个实例有了第一个内存地址
# 就把这个地址赋给instance，
# 之后的所有实例都使用instance中的地址


# CLASS 423  初始化动作只执行一次
# 在每次使用 类名（）创建对象时，Python的解释器都会自动调用两个方法：
# __new__分配空间
# __init__对象初始化

class MusicPlayer:
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False
    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3.返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        # 1.判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return
        # 2.如果没有执行过，在执行初始化动作
        print("初始化播放器")
        # 3.修改类属性的标记
        MusicPlayer.init_flag = True
# 创建多个对象
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)



