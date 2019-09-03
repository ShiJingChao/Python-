class Circle:
    def __init__(self,r):
        self.r = r
    def get_perimenter(self):
        return 2*3.14*self.r
    def get_area(self):
        return 3.14*self.r*self.r

c1 = Circle(1)
print(c1.get_perimenter())
print(c1.get_area())

class RunningMan:
    def __init__(self,weight):
        self.weight = weight
    def running(self):
        self.weight -= 2.5
        print(self.weight)
    def eatting(self):
        self.weight += 3
        print(self.weight)

c = RunningMan(10)
c.running()
c.eatting()

class Road:
    def __init__(self,long):
        self.long = long
    def get_time(self,car_obj):
        t = self.long/car_obj
        print("时间为：%.2f"%t)
class Car:
    def __init__(self,speed):
        self.speed = speed
r = Road(10)
c = Car(2)
r.get_time(c.speed)

# class House:
#     def __init__(self,area,name):
#         self.area = area
#         self.name = name
# class HouseItem:
#     def __init__(self,area,name):
#         self.area = area
#         self.name = name


class Num:
    count = 0
    def __init__(self):
        Num.count+=1
p = Num()
p1 = Num()
print(Num.count)
import random
class Game:
    h_score = 0
    def play_game(self,name):
        score = random.randint(1,100)
        print("%s分数为%d" % (name,score))
        if score > Game.h_score:
            Game.h_score=score
    def get_history_score(self):
        print("最高分：%d"%self.h_score)
g = Game()
g.play_game("尿尿")
g.play_game("尿尿")
g.play_game("尿尿")
g.play_game("尿尿")
g.play_game("尿尿")
g.get_history_score()
