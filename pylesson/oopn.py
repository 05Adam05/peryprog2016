class Animal:
    def __init__(self,evil,name,habitat):
        self.evil = evil
        self.paws = 4
        self.name = name
        self.habitat = habitat

    def sleep(self):
        print('хрррррр')

    def eat(self):
        print('омномном')

    def hunt(self,target):
        print(self.name,'охотится на',target)

class Dog(Animal):
    def __init__(self,evil,name,habitat,breed):
        super().__init__(evil,name,habitat)
        self.breed = breed

    def protect(self, place):
        print("{0} охраняет {1}".format(self.name, place))

    def eat(self):
        print("нямнямням")




boar = Animal(True,'Коза','У бабушки в деревне')

print(boar.name)
print(boar.paws)

boar.sleep()
boar.eat()

wolf = Animal(True,'Волк','лес')

wolf.hunt(boar.name)

dog = Dog(False,'Шарик','Дома','Хаски')
print(dog.name)
dog.protect("дом")
dog.eat()

    