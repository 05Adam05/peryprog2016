import random



class Character:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self,target):
        target.hp -= self.damage
        print("{0} атакует {1}".format(self.name,target.name))


class Player(Character):
    def __init__(self,name,hp,attack,weapon):
        super().__init__(name,hp,attack)
        self.weapon = weapon



class Zombie(Character):
    pass


TINA = Player('Тина',200,10,'Перочиный нож')

FAST_ZOMBIE = Zombie('Зомби-быстрый-азамат',50,20)
BALD_ZOMBIE = Zombie('Зомби-лысый-баракят',500,1)
STUPID_ZOMBIE = Zombie('Зомби-тупой-я-тебя-ща напищу',2,5)



class Game:
    def __init__(self,player,tps):
        self.player = player
        self.tps = tps
        self.count = 0

    def start(self):
        self.zombie = random.choice(self.tps)
        while True:
            self.player.attack(self.zombie)
            self.zombie.attack(self.player)
            input()
            if self.zombie.hp <= 0:
                print("зомби умер")
                self.zombie = random.choice(self.tps)
                self.count += 1
            if self.player.hp <= 0:
                print("Ты умер лохохохохохох")
                print("Твой счет",self.count)


game = Game(TINA,[FAST_ZOMBIE,BALD_ZOMBIE,STUPID_ZOMBIE])
game.start()








