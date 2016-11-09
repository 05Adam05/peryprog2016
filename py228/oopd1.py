class Zombie:
    count = 0

    @classmethod
    def show_zombie(cls):
        print("Колличество зомби:",cls.count)

    @classmethod
    def show_class(cls):
        print(cls.__name__)

    def __eq__(self,other):
        return self.power == other.power
    
    def __init__(self,name,power):
        self.name = name
        self.power = power 
        self.__teeth = 32
        Zombie.count += 1

    @property
    def teeth(self):
        print("вывод зубов")
        return self.__teeth

    @teeth.setter
    def teeth(self,something):
        self.__teeth = something

    def attack(self,target):
        if self.__teeth > 0 :
            print("{0} кусает {1}а".format(self.name,target))
            self.__teeth -= 1
        else:
            print("Беззубый кусать не может")

    def __str__(self):
        return self.name

    def __iadd__(self, other):
        self.__teeth += other
        return self

abdul = Zombie('Абдул',1)
abdul.attack('Айдунбек') 
for i in range(1,34):
    abdul.attack('Айдунбек')


abdul.teeth += 5  
for i in range(1,10):
    abdul.attack('Айдунбек')
print(abdul.teeth)
print(Zombie.count)
barakyat = Zombie('Страшный зомби Баракь',800)
Zombie.show_zombie()
Zombie.show_class()
n = 5 
n += 2
barakyat += 10
print(n)
print(barakyat)
print(barakyat.teeth)
print(barakyat == abdul)
