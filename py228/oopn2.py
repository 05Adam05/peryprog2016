class Animal:
    def __init__(self,name,weight,height,wild,speed):
        self.weight = weight
        self.height = height
        self.wild = wild
        self.speed = speed
        self.name = name

    def eat(self,food):
        print("{0} кушает {1}".format(self.name,food))

class Sloth(Animal):
    def __init__(self,name,weight,height,wild,speed,claws):
        super().__init__(name,weight,height,wild,speed)
        self.claws = claws
        self.speed -= 50

    def sleep(self):
        print("{0} спит".format(self.name))

class MegaSloth(Sloth):
    def __init__(self,name,weight,height,wild,speed,claws):
        super().__init__(name,weight,height,wild,speed,claws)
        self.speed -= 9000000000000000000000000000000000000000000000000000000000000000



cheetah = Animal("Сагид",200,80,True,356)
print(cheetah.weight)
cheetah.height += 10
print(cheetah.height)
cheetah.eat("фрукты")
tagir = MegaSloth("Тагир",100,2,True,-20,"мощные")
print("Скорость",tagir.name+'а =',tagir.speed)
tagir.sleep()