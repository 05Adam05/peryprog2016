class Zombie:
    def __init__(self,name,power):
        self.name = name
        self.power = power 
        self.teeth = 32

    def attack(self,target):
        if self.teeth > 0 :
            print("{0} кусает {1}".format(self.name,target))
            self.teeth -= 1
        else:
            print("Беззубый кусать не может")

abdul = Zombie('Абдул',0.1)
abdul.attack('Айдунбек') 

