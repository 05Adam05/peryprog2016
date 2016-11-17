import random as r
import json
class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    
    def attack(self,target):
        rand_attack = r.randint(0,4)
        damage = self.damage  + rand_attack
        target.health -= damage
        print("{0} атакует {1} и наносит {2} урона".format(self.name,target.name,damage))

    def show_stats(self):
        print("{0.name} жизни: {0.health}, атака: {0.damage}".format(self))





class Player(Character):
    def __init__(self, name, weapons, health, damage):
        super().__init__(name, health, damage)
        self.weapons = weapons
        self.count = 0

    def show_weapons(self):
        for num, weap in enumerate(self.weapons):
            print('{0}.{1.name} урон: {1.damage}, здоровье: {1.count}'.format(num,weap))


class Zombie(Character):
    def die(self):
        print('{0.name} умер'.format(self))


class Weapon:
    def __init__(self,name,damage,count,max_count):
        self.name = name
        self.damage = damage
        self.count = count
        self.max_count = max_count


class Game:
    def load_conf(self):
        with open('conn.json', "rt", encoding='utf-8') as f:
            self.conf = f.read()
        self.conf = json.loads(self.conf)

    def load_weapons(self):
        self.weapons = [Weapon(n,ch['damage'],0,ch['count']) for n, ch in self.conf['weapons'].items()]


    def start(self):
        print("Весь мир погрузился в хаос. Зомби атакут людей. И вы должны спастись")
        self.load_conf()
        self.load_weapons()
        zombie=self.create_zombie()
        player=self.create_player()
        while True:
            player.show_weapons()
            player.attack(zombie)
            zombie.attack(player)
            player.show_stats()
            zombie.show_stats()
            input()
            if player.health <= 0:
                print('Ты умер и стал зомби. Лшр.ххх х')
                print('Но ты убил зомби', player.count)
                break
            if zombie.health <= 0:
                zombie.die()
                zombie = self.create_zombie()
                player.count += 1


    def create_player(self):
        name = input('Введите ваше имя,несчастное отродие ')
        self.player = Player(name,[Weapon('kulak',1,999,999)],150,50)
        return self.player

    def create_zombie(self):
        self.zombie = Zombie('Бегун',70,10)
        return self.zombie



game = Game()


game.start()




