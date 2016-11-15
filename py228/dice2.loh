import random

player1, player2 = {}, {}

player1['имя'] = input("Введите имя первого игрока: ")
player2['имя'] = input("Введите имя второго игрока: ")

player1['сумма'] = 500
player2['сумма'] = 500

while True:
    player1['ставка'] = int(input('Введите ставку: '))
    player1['магия'] = int(input('Введите счастливое число: '))
    if player1['ставка'] > player1['сумма']:
        player1['ставка'] = player1['сумма']
    player2['ставка'] = int(input('Введите ставку: '))
    player2['магия'] = int(input('Введите счастливое число: '))
    if player2['ставка'] > player2['сумма']:
        player2['ставка'] = player2['сумма']
        
    player1['ход'] = random.randint(2,12)
    player2['ход'] = random.randint(2,12)
    print(player1['имя'],'выбросил:', player1['ход'])
    print(player2['имя'],'выбросил:', player2['ход'])
    
    if player1['ход'] == player1['магия'] and player2['ход'] == player2['магия']:
        print('ничья')
    elif player1['ход'] == player1['магия'] or player1['ход'] > player2['ход']:
        if player1['ход'] == player1['магия']:
            print('Выпало счастливое число')
        print(player1['имя'], 'выиграл ход')
        player1['сумма'] += player2['ставка']
        player2['сумма'] -= player2['ставка']
        
    elif player2['ход'] == player2['магия'] or player2['ход'] > player1['ход']:
        if player2['ход'] == player2['магия']:
            print('Выпало счастливое число')
        print(player2['имя'],'выиграл ход')
        player2['сумма'] += player1['ставка']
        player1['сумма'] -= player1['ставка']
    else:
        print('ничья')


    print(player1['имя'],player1['сумма'])
    print(player2['имя'],player2['сумма'])

    if player1['сумма'] == 0:
        print(player1["имя"],'проиграл')
        break
    if player2['сумма'] == 0:
        print(player2["имя"],'проиграл')
        break