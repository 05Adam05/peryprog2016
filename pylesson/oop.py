class Human:
    def __init__(self, name, skin, cost):
        self.name = name
        self.skin = skin
        self.cost = cost
    def walk(self):
        print('Я хожу')
    def breath(self):
        print('Я дышу')
    def kill(self, another_human):
        print("{0} убивает {1}а".format(self.name,another_human.name))

class ScoolBoy(Human):
    def __init__(self, name, skin, cost, fav_game):
        super().__init__(name, skin, cost)
        self.fav_game = fav_game
    
    def play_game(self,hours):
        print('Я играю в {0} {1} часов'.format(self.fav_game,hours))

    def walk(self):
        super().walk()
        print('"Спиной" к стенке я хожу')



ruslan = Human('Руслан','обычная',30)
print(ruslan.name)
print('Его лучшая цена: ', ruslan.cost)
ruslan.breath()
ruslan.walk()
arsen = ScoolBoy('Арсен','черная',90000,'Майнкрафт')
print(arsen.cost)
arsen.kill(ruslan)
ruslan.kill(arsen)
ruslan.walk()
arsen.play_game(20)
arsen.walk()