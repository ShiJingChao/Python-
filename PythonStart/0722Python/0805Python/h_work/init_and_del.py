class Person:
    def __init__(self,name):
        self.name =name
    def __del__(self):
        print("%s被销毁"%self.name)
p1 = Person("11")
p2 = Person("22")

