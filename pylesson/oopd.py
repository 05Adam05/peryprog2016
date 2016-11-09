class Dragon:
    number_of_dragons = 0

    @classmethod
    def show_dragons(cls):
        print("У нас",cls.number_of_dragons,"драконов")
    
    def __init__(self,name,power):
        self.name = name
        self.power = power
        self.__fireball = 5
        self.__sock = 'красный носочек'
        Dragon.number_of_dragons += 1


    def __str__(self):
        return self.name
    

    def __iadd__(self, other):
        self.__fireball += int(other)
        return self

    @property
    def fireball(self):
        print("Возвращает файрбол")
        return self.__fireball

    @fireball.setter
    def fireball(self, col):
        print('Добавляются шары')
        self.__fireball = col

    @property
    def sock(self):
        return self.__sock


    def fire(self):
        if self.__fireball > 0:
            print("вылетел огненный шар")
            self.__fireball -= 1
        else:
            print('Кончились силы')

ruslan = Dragon('Руслан',10)
for i in range(1,8):
    ruslan.fire()
print(ruslan.fireball)

ruslan.fireball = 10
print(ruslan.sock)
# ruslan.sock = 'синий носочек'
# for i in range(1,8):
#     ruslan.fire()

Dragon.show_dragons()

arsen = Dragon('Арсен',3)

Dragon.show_dragons()
ruslan += 5
print(ruslan)
print(ruslan.fireball)
# print(ruslan < arsen)

print(arsen)
