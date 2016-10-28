import random

def create_player():
    player = {}
    player['name'] = input("Введите имя: ")
    player['health'] = 200
    player['attack'] = 10
    
    add_a = 5
    add_h = 100
    while True:
        ch = input('Поднять жизни(1). Поднять атаку(2): ') 
        if ch == '1':
            player['health'] += add_h
            break
        elif ch == '2':
            player['attack'] += add_a
            break
        else:
            print('введите 1 или 2')
    return player

def show_player(player):
    print('Игрок: {0[name]}, жизни: {0[health]}, атака: {0[attack]}'.format(player))


def attack(p1,p2):
    luck = random.randint(-10,10)
    damage = p1['attack'] + luck
    p2['health'] -= damage
    print('{0} нанес {1} урона'.format(p1['name'],damage))


def fight(pl1,pl2):
    while True:
        attack(pl1,pl2)
        attack(pl2,pl1)
        show_player(player1)
        show_player(player2)
        input()

        if pl1['health'] <= 0:
            print(pl2['name'],'победил')
            break
        elif pl2['health'] <= 0:
            print(pl1['name'],'победил')
            break



print('В нашей эпичной игре сражаются два игрока. Поехали')
player1 = create_player()
player2 = create_player()
show_player(player1)
show_player(player2)
fight(player1,player2)
