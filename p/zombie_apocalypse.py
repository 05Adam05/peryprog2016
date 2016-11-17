import random
import json
class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    
    def attack(self,target):
        att = random.randint(0,4)
        real_damg = att + self.damage
        target.health -= real_damg
        print("{0} атакует {1} и наносит {2} урона".format(self.name,target.name,real_damg))

    def show_stats(self):
        print("{0.name} жизни: {0.health}, атака: {0.damage}".format(self))


class Player(Character):
    def __init__(self, name, weapon, health, damage):
        super().__init__(name, health, damage)
        self.weapon = weapon
        self.count = 0

    def show_weapons(self):
        print("у вас есть:")
        for num, weapon in enumerate(self.weapon):
            print('{0}. {1.name} - сила: {1.damage}, колличество: {1.count}'.format(num,weapon))

    def chose_weapon(self):
        self.damage = 0
        while True:
            try:
                w = int(input("Введите номер оружия: "))
                if w in range(0,len(self.weapon)):
                    self.damage = self.weapons[w].damage
                    self.weapons[w]

class Zombie(Character):
    def die(self):
        print('{0.name} умер'.format(self))

class Weapon:
    def __init__(self, name, damage, count):
        self.name = name
        self.damage = damage
        self.count = count


class Game:

    def load_data(self):
        f1 = open("conf.json", 'rt', encoding = 'utf-8')
        data = f1.read()
        f1.close()
        # print(data)
        data = json.loads(data)
        return data

    def take_weapon(self):
        weapons = self.data['weapons']
        # print(weapons)
        self.weapons = [Weapon(name,ch['damage'],ch['count']) for name, ch in weapons.items()]



    def start(self):
        print("Весь мир погрузился в хаос. Зомби атакут людей. И вы должны спастись")
        self.data = self.load_data()
        self.take_weapon()
        self.create_player()
        self.create_zombie()
        player = self.player
        zombie = self.zombie
        while True:
            player.show_weapons()
            player.show_stats()
            zombie.show_stats()
            player.attack(zombie)
            zombie.attack(player)

            input()
            if player.health <= 0:
                print('Ты умер и стал зомби. Лшр.ххх х')
                print('Но ты убил зомби', self.player.count)
                break
            if zombie.health <= 0:

                self.create_zombie()
                player.count += 1


    def create_player(self):
        name = input('Введите имя своего персонажа:')
        self.player = Player(name,[Weapon('кулаки',1,999)],150,50)

    def create_zombie(self):
        self.zombie = Zombie('Бегун',70,10)



game = Game()

game.start()