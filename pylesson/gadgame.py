import random
class Character:
    def __init__(self,name):
        self.name = name
        self.at = 50
        self.hp = 350

    def attack(self,target):
        target.hp -= self.at
        print('{0} атаковал {1}'.format(self.name,target.name))

class Orks(Character):
    def __init__(self,name):
        self.home = 'Мордор'
        super().__init__(name)

class Human(Character):
    def __init__(self,name):
        self.home = 'Гондор'
        super().__init__(name)

def show(character):
    print(character.name,'Ваши жизни:',character.hp, 'и атака:',character.at)
    
name = input('Скажи мне свое имя страник.')
print('Рад знакомству', name)       
print()
while True:
    ras = input('Выбирите свою рассу: "Human", "Orks".')
    if ras == 'Human':
        name = Human(name)
        print('Вы выбрали рассу людей!')
        print('Ваша база:', name.home)      
        break       
    elif ras == 'Orks':
        name = Orks(name)
        print("Вы выбрали рассу орков!")
        print('Ваша база:', name.home)           
        break
    else:
        print('Вы написали что-то не-то.')

print()

while True:
    vibor = input('Что улучшить: атаку или броню? ')    
    if vibor == 'атаку' and ras == 'Human':
        name.at += 20
        show(name)
        # print(Human(name).at)
        break
    elif vibor == 'броню' and ras == 'Human':
        name.hp += 120
        show(name)
        break
    elif vibor == 'атаку' and ras == 'Orks':
        name.at += 20
        show(name)
        break
    elif vibor == 'броню' and ras == 'Orks':
        name.hp += 140
        show(name)
        break
    else:
        print('Выберете атаку или броню.')

print('Нажмите энтер на продолжения.')
input()

if ras == 'Human':
    print('Ну что воин, я тебе расскажу про нашего противника - Орки!')
    print('Это безжалостные существа созданые великим властелином Саороном!')
    print('Сейчас мы выезжаем на защиту города Осгилиат. Противники уже близко! Нам нужно потоопиться!')
    print('Прибытие в Осгилиат:')
    print('По местам парни! Враги вот вот прибудут, деритесь до последнего вздоха! Они пришли... в атаку!!!!')
    print()
    print('Вы вступили в бой с орком!')
    print()
    print('Нажмите энтер на продолжения.')
    enemy = Orks('Ур-гор')
    enemy.at += 20


elif ras == 'Orks':
    print('Ааарррр, новобранцы! Наш противник Гондор - страна людей!')
    print('Повелитель сказал захватить выступать не медленно! Шевелитесь ленивые крысы !')
    print('Через мертвецкие топи мы придем в город Осгилиат и сожем его дотла!')
    print('Прибытие в Осгилиат:')
    print('Арррр!!!! В атаку ленивые крысы!!! Убейте всех!!!')
    print()
    print('Вы вступили в бой с человеком!')
    print()
    print('Нажмите энтер на продолжения.')
    enemy = Human('Арагорн')
    enemy.at += 120


while True:
    input()
    name.attack(enemy)
    enemy.attack(name)
    show(name)
    show(enemy)
    if enemy.hp <= 0:
        print('Ты победил. Конец игры!')
        break
    if name.hp <= 0:
        print('Ты проиграл. Конец игры!')
        break  
