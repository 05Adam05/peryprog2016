class Avarec:
    def __init__(self,iq,strength,name):
        self.iq = iq
        self.strength = strength
        self.name = name
        self.hinkal = "аварский хинкал"
        self.hinkal_count = 1

    def vse(self):
        print("Аварцы делают все")

    def make_hinkal(self):
        self.hinkal_count *= 2

    def program(self,another_avarec):
        print('{0} программирует с {1}'\
            .format(self.name,another_avarec.name))

class CoolAvarec(Avarec):
    def __init__(self,iq,strength,name,something):
        super().__init__(iq,strength,name)
        self.something = something

    def make_connect(self,man):
        print('Аварец делает связь с',man)

    def make_hinkal(self):
        super().make_hinkal()
        self.hinkal_count *= 8


gadzhi_number_1 = CoolAvarec(300,100,'Гаджи','что-то')
print(gadzhi_number_1.something)
print(gadzhi_number_1.name)
print(gadzhi_number_1.hinkal)
gadzhi_number_1.strength *= 200
print(gadzhi_number_1.strength)
gadzhi_number_1.vse()
gadzhi_number_1.make_hinkal()
gadzhi_number_1.make_hinkal()
gadzhi_number_1.make_hinkal()
print(gadzhi_number_1.hinkal_count)
aburahman = Avarec(120,15,'Абурахаман')
aburahman.program(gadzhi_number_1)
gadzhi_number_1.make_connect('Умный')
