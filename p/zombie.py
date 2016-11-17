import random
import json
class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    
    def attack(self,target):
        ran = random.randint(0,4)
        real_damage = self.damage + ran
        target.health -= real_damage
        print("{0} атакует {1} и наносит {2} урона".format(
            self.name,target.name,real_damage))

    def show_stats(self):
        print("{0.name} жизни: {0.health} урон: {0.damage}".format(self))

class Player(Character):
    def __init__(self, name, weapons, health, damage):
        super().__init__(name, health, damage)
        self.weapons = weapons
        self.count = 0

    def show_weapons(self):
        for num, weapon in enumerate(self.weapons):
            print("{0}.{1.name} - коллличество: {1.count}, урон {1.damage}".format(num,
                weapon))

    def chose_weapon(self):
        while True:
            try:
                weapon = int(input("Выберите номер оружия: "))
                if weapon in range(0,len(self.weapons)):
                    self.damage = self.weapons[weapon].damage
                    self.weapons[weapon].count -= 1
                    if self.weapons[weapon].count <= 0:
                        self.weapons.pop(weapon)
                    break
                else:
                    print('Введите существующее оружие')
            except ValueError:
                print('Введите номер оружия')



class Zombie(Character):
    def die(self):
        print('{0.name} умирает'.format(self))

class Weapon:
    def __init__(self,name,damage,count,max_count):
        self.name = name
        self.damage = damage
        self.count = count
        self.max_count = max_count


class Game:

    def load_conf(self):
        f = open('config.json','rt', encoding = 'utf-8')
        self.conf = f.read()
        self.conf = json.loads(self.conf)

    def take_weapons(self):
        self.weapons = [Weapon(name,ch['damage'],0,ch['count']) for name, ch in self.conf['weapons'].items()  ]

    def give_weapon(self,player):
        if not random.randint(0,4):
            this_weapon = random.choice(self.weapons)
            this_weapon.count += this_weapon.max_count
            if this_weapon not in player.weapons:
                player.weapons.append(this_weapon)


    def start(self):
        print("Весь мир погрузился в хаос. Зомби атакут людей. И вы должны спастись")
        self.load_conf()
        self.take_weapons()
        self.create_player()
        self.create_zombie()
        player = self.player
        zombie = self.zombie
        while True:
            self.give_weapon(player)
            player.show_weapons()
            player.chose_weapon()
            player.show_stats()
            zombie.show_stats()
            player.attack(zombie)
            zombie.attack(player)
            if player.health <= 0:
                print('Ты умер и стал зомби. Лшр.ххх х')
                print('Но ты убил зомби', player.count)
                break
            if zombie.health <= 0:
                zombie.die()
                self.create_zombie()
                zombie = self.zombie
                player.count += 1


    def create_player(self):
        name = input("Введите ваше имя: ")
        self.player = Player(name,[Weapon('кулак',1,9999,9999)],250,0)

    def create_zombie(self):
        self.zombie = Zombie('Бегун',20,5)



game = Game()


game.start()