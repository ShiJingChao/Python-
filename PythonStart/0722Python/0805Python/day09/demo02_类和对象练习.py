class Dog:
    def eat(self):
        print("---吃吃吃吃骨头---")

    def shake(self):
        print("---摇摇哟啊尾巴--")

    def look_door(self):
        print("---看大门---")


d1 = Dog()
d1.name = "旺财"
d1.color = "绿色"
d1.shake()
d1.look_door()

d2 = Dog()
d2.name = "大黄"
d2.color = "yellow"

print(d1)
print(id(d1))

print(d2)
print(id(d2))



