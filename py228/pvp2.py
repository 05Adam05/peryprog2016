import random
def create_player():
    player = {}
    player["name"] = input("Введите имя: ")
    player["attack"] = 10
    player["health"] = 200
    add_h = 100
    add_a = 5
    while True:
        ch = input("Добавить атаку(1) или добавить \
здоровье(2): ")
        if ch == '1':
            player["attack"] += add_a
            break
        elif ch == '2':
            player["health"] += add_h
            break
        else:
            print("Введите 1 или 2: ")

    return player

def show_player(player):
    print("Игрок: {0[name]}, атака: {0[attack]},\
здоровье: {0[health]} ".format(player))

def hit(pl1, pl2):
    min_l = -10
    max_l = 10  
    luck = random.randint(min_l,max_l)
    if luck == min_l: print(pl1['name'], 'лоханулся')
    if luck == max_l: print(pl1['name'], 'кританул')
    damage = pl1['attack'] + luck
    pl2['health'] -= damage
    print('{0} нанес {1} урона'.format(pl1['name'],damage))



def fight(pl1,pl2):
    input()
    while True:
        hit(pl1,pl2)
        hit(pl2,pl1)
        show_player(player1)
        show_player(player2)
        input()

        if pl1['health'] <= 0:
            print(pl2['name'],'победил')
            break
        if pl2['health'] <= 0:
            print(pl1['name'],'победил')
            break


player1 = create_player()
player2 = create_player()
# print(player1, player2)
show_player(player1)
show_player(player2)
fight(player1, player2)