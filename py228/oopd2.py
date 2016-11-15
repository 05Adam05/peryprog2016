class Chert:
    
    count = 0

    @classmethod
    def show_count(cls):
        print("У нас на районе {0} черта".format(cls.count))

    def __init__(self,name,hair,strengh):
        self.name = name
        self.hair = hair
        self.heeyar = True
        self.strengh = strengh
        self.__jaguar = 5
        Chert.count += 1


    @property
    def jaguar(self):
        print("Возвращает колличество ягуара")
        return self.__jaguar

    @jaguar.setter
    def jaguar(self,something):
        self.__jaguar = something

    def strike(self,target):
        if self.__jaguar > 0:
            print("{0} кидает ягуар в {1}".format(self.name, target))
            self.__jaguar -= 1
        else:
            print("Кончилась яга")

    def __str__(self):
        return self.name

    def __len__(self):
        return self.hair

    def __iadd__(self, other):
        self.jaguar +=  other
        return self
    def __lt__(self,other):
        return self.hair < other.hair



said = Chert('chert',100,12)
said.strike('бабушку')
for i in range(1,13):
    said.strike('бабушку')
print(said.jaguar)
said.jaguar += 5
for i in range(1,13):
    said.strike('бабушку')
n = 5

tagir = Chert('Тагуха-Ашшашитн',169,12)
tagir += 5
print(tagir.jaguar)
print(tagir)
print(len(tagir))
print(Chert.count)
Chert.show_count()
print(said < tagir)