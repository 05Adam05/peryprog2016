class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    
    def attack(self,target):
        target.health -= self.damage
        print("{0} атакует {1} и наносит {2} урона".format(self.name,target.name,self.damage))

class Player(Character):
    def __init__(self, name, weapon, health, damage):
        super().__init__(name, health, damage)
        self.weapon = weapon
        self.count = 0

class Zombie(Character):
    pass


class Game:



    def start(self):
        print("Весь мир погрузился в хаос. Зомби атакут людей. И вы должны спастись")
        self.create_zombie(Zombie('Бегун',70,10))
        while True:
            self.player.attack(self.zombie)
            self.zombie.attack(self.player)
            input()
            if self.player.health <= 0:
                print('Ты умер и стал зомби. Лшр.ххх х')
                print('Но ты убил зомби', self.player.count)
                break
            if self.zombie.health <= 0:
                self.create_zombie(Zombie('Бегун',70,10))
                self.player.count += 1


    def create_player(self,player):
        self.player = player

    def create_zombie(self,zombie):
        self.zombie = zombie



game = Game()

game.create_player(Player('Амир','Сковордка',150,50))
game.start()




