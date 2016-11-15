import random
player1 = {'ход': 0, 'имя': '', 'сумма': 100, 'ставка': 0}
player2 = {'ход': 0, 'имя': '', 'сумма': 100, 'ставка': 0}

player1['имя'] = input('Введите имя первого игрока: ')
player2['имя'] = input('Введите имя второго игрока: ')

while True:
    #ставки
    player1['ставка'] = int(input('Введите ставку: '))
    if player1['ставка'] > player1['сумма']:
        player1['ставка'] = player1['сумма']

    player2['ставка'] = int(input('Введите ставку: '))
    if player2['ставка'] > player2['сумма']:
        player2['ставка'] = player2['сумма']
    
    # броски
    player1['ход'] = random.randint(2,12)
    player2['ход'] = random.randint(2,12)
    print(player1['имя'], 'выкинул', player1)
    print(player2['имя'], 'выкинул', player2)

    if player1['ход'] > player2['ход']:
        print(player1['имя'], 'выйграл раунд')
        player1['сумма'] += player1['ставка']
        player2['сумма'] -= player2['ставка']
    elif player1['ход'] == player2['ход']:
        print('Ничья')
    else:
        print(player2['имя'], 'выйграл раунд')
        player2['сумма'] += player2['ставка']
        player1['сумма'] -= player1['ставка']

    print(player1['имя'], 'сумма:', player1['сумма'])
    print(player2['имя'], 'сумма:', player2['сумма'])
    if player1['сумма'] == 0:
        print(player1['имя'], 'проиграл')
        break
    if player2['сумма'] == 0:
        print(player2['имя'], 'проиграл')
        break