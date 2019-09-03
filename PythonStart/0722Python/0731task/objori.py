# class Person(object):
#     """保卫者"""
#     def __init__(self,name):
#         self.name = name
#     def install_bullet(self,magazineclib,bullet):
#         '''将子弹安装到弹夹中'''
#         magazineclib.save_bullet(bullet)
#     def install_clib_2_gun(self,gun,clib):
#         '''6.1将弹夹安装到枪中'''
#         gun.insall_clib(clib)
#
# class Gun(object):
#     '''枪类'''
#     def __init__(self,name):
#         self.name = name
#         # 6.3用来记录弹夹的引用
#         self.clib = None
#     def install_clib(self,clib):
#         '''6.2将弹夹安装到枪中'''
#         self.clib = clib
#
#     #8.2 显示枪和弹夹的信息
#     def __str__(self):
#         if self.clib:
#             return "枪的信息：%s,%s"%(self.name,self.clib)
#         else:
#             return "枪的信息为%s，并且这把枪没有弹夹"%(self.name)
# class Magazineclib(object):
#     '''弹夹'''
#     def __init__(self,max_num):
#         self.max_num = max_num  #盛放子弹的最大容量
#         # 用来保存子弹
#         self.bullet_list=[]
#
#     def save_bullet(self,bullet):
#         '''将子弹装入弹夹中'''
#         self.bullet_list.append(bullet)
#
#     #7.1 打印 弹夹信息
#     def __str__(self):
#         return "弹夹的信息：%d%d"%(len(self.bullet_list),self.max_num)
# class Bullet(object):
#     '''子弹'''
#     def __init__(self,lethality):
#         self.lethality = lethality #子弹的杀伤力
#
# def main():
#     '''用来控制整个程序的流程'''
#     # 保卫者对象
#     bwz = Person("老王")
#     # AK-47 枪 对象
#     gun = Gun("AK-47")
#     # 弹夹对象
#     clib = Magazineclib(200)
#     # 7.2 创建一些子弹
#     for i in range(100):
#         # 子弹对象
#         bullet = Bullet(10) #打一枪掉10滴血
#         # 保卫者将自动那安装到弹夹中
#         bwz.install_bullet(clib,bullet)
#     # 保卫者将弹夹安装到枪中
#     bwz.install_clib_2_gun(gun,clib)
#
#     #7.测试弹夹信息
#     print(clib)
#     #8.测试枪的信息
#     print(gun)
#     #保卫者拿起枪
#     #侵略者对象
#     #保卫者开枪打敌人
#
# if __name__ == '__main__':
#     main()



class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print('没有子弹了')
            return
        self.bullet_count -= 20
        print("%s发射子弹[%d]..." % (self.model, self.bullet_count))
    def pick(self):
        print("你捡起了枪")
        self.bullet_count = 100
        print("子弹剩余%d"% self.bullet_count)


m99 = Gun('m99')
m99.pick()
m99.add_bullet(50)
m99.shoot()

class Sniper:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print('[%s] 还没有枪...' % self.name)
            return
        print('冲啊...[%s]' % self.name)
        self.gun.add_bullet(50)
        self.gun.shoot()

# m99 = Gun('m99')
sniper = Sniper('麦克')
sniper.gun = None
m99.pick()
sniper.gun = m99
sniper.fire()
