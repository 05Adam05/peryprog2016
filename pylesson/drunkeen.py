import random

def give_card(player):
    yield player.pop()

def hot(player1,player2):
    global player1_count, player2_count
    k = 0
    for card1, card2 in zip(give_card(player1), give_card(player2)):
        k += 2
        print(k)
        input()
        print(card1, card2)
        
        if card1[0] > card2[0]:
            player1_count += k
            break
        if card1[0] < card2[0]:
            player2_count += k
            break
        # else:
        #     continue



m = ['Бубны', 'Червы', 'Крести', 'Пики']
c = [(num, mas) for num in range(6,15) for mas in m]
# print(с)
random.shuffle(c)
# print(с)

player1 = c[:len(c)//2]
player2 = c[len(c)//2:]
player1_count = 0
player2_count = 0
print(player1,'===',player2)
while True:
    hot(player1, player2)
    print(player1_count,player2_count)
    # input()
    
    if not player1 or not player2:
        break
# print(player1_count, player2_count)