class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, victim):
        victim.hp -= self.damage
        print("{0} атаковал {1} и нанес {2} урона".format(self.name, victim.name, self.damage))

class Player(Character):
    def __init__(self, name, hp, damage,weapon):
        super().__init__(name, hp, damage)
        self.weapon = weapon

class Zombie(Character):
    pass

class Game():

    def start(self):
        self.player = Player('Гордон',100,20,'топор')
        self.zombie = Zombie('Абдулла',30,5)
        self.count = 0
        while True:
            self.player.attack(self.zombie)
            self.zombie.attack(self.player)
            input()
            if self.player.hp <= 0:
                print("Вы проиграли, но убили",self.count)
                break
            if self.zombie.hp <= 0:
                self.zombie = Zombie('Абдулла',30,5)
                self.count += 1

game = Game()
game.start()


