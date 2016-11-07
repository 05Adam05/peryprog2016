class Animal:
    def __init__(self,name,tail,speed):
        self.name = name
        self.tail = tail
        self.speed = speed

    def walk(self):
        print('животное ходит')

    def eat(self,food):
        print('{0} ест {1}а'.format(self.name,food))

class Lion(Animal):
    def __init__(self,name,tail,speed,mane):
        super(). __init__(name,tail,speed)
        self.mane = mane

    def walk(self):
        print('лев ходит')

    def lick_yourself(self):
        print(self.name,'облизался')

class BlackLion(Lion):
    def __init__(self,name,tail,speed):
        super(). __init__(name,tail,speed,'черный')

sheep = Animal('Баран',True,2)
print(sheep.name)
lion = Lion('Левчик',True,4,'черная')
lion.walk()
lion.eat(sheep.name)
lion.lick_yourself()
lion.walk()

b_lion = BlackLion('Левчик',True,4)