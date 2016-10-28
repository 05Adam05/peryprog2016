import random

player1_name = input("Введите имя первого игрока: ")
player2_name = input("Введите имя второго игрока: ")
player1_cash = 500
player2_cash = 500
while True:
    
    player1_rate = int(input(player1_name+' делайте вашу ставку:'))
    if player1_rate > player1_cash:
        player1_rate = player1_cash
    player1_cash -= player1_rate

    player2_rate = int(input(player2_name+' делайте вашу ставку:'))
    if player2_rate > player2_cash:
        player2_rate = player2_cash
    player2_cash -= player2_rate
      
    player1 = random.randint(2,12)
    player2 = random.randint(2,12)
    print(player1_name, 'выкинул', player1)
    print(player2_name, 'выкинул', player2)
    if player1 > player2:
        print(player1_name,'выйграл раунд')
        player1_cash += player2_rate + player1_rate

    elif player1 == player2:
        print('Ничья')
        player1_cash += player1_rate
        player2_cash += player2_rate
    else:
        print(player2_name, 'выйграл раунд')
        player2_cash += player2_rate + player1_rate
    print(player1_name, ":", player1_cash)
    print(player2_name, ":", player2_cash)
    
    if player1_cash == 0:
        print(player1_name,'проиграл')
        break
    if player2_cash == 0:
        print(player2_name,'проиграл')
        break
    



