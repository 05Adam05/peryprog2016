import random
def create_player():
    player = {}
    player['name'] = input("Введите имя:")
    player['attack'] = 10
    player['health'] = 200
    add_a = 5
    add_h = 50
    while True:
        ch = input("Увеличить жизни(1). Увеличить атаку(2): ")
        if ch == '1':
            player['health'] += add_h
            break
        elif ch == '2':
            player['attack'] += add_a
            break
        else:
            print('Введите 1 или 2')
    return player

def show_player(player):
    print('Игрок: {0[name]}, здоровье: {0[health]}, атака:\
     {0[attack]}'.format(player))

def att(pl1,pl2):
    luck = random.randint(-10,10)
    damage = pl1['attack'] + luck
    pl2['health'] -= damage
    print('{0} нанес {1} урона'.format(pl1['name'],damage))

def fight(pl1,pl2):
    while True:
        att(pl1,pl2)
        att(pl2,pl1)
        show_player(player1)
        show_player(player2)
        input()
        if pl1['health'] <= 0:
            print(pl2['name'],'победил')
            break
        elif pl2['health'] <= 0:
            print(pl1['name'],'победил')
            break


player1 = create_player()
player2 = create_player()
# print(player1, player2)
show_player(player1)
show_player(player2)
input()
fight(player1, player2)



