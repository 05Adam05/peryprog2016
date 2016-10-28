import random

def get_card(player):
    while True:
        yield player.pop()


def hod(player1,player2):
    k = 0
    global player1_count, player2_count
    for card1, card2 in zip(get_card(player1),get_card(player2)):
        k += 2
        print(card1, card2)
        if card1[0] > card2[0]:
            player1_count += k
            break
        elif card1[0] < card2[0]:
            player2_count += k
            break


masti = ['Червы','Пики','Крести','Бубны']
koloda = [(n,m) for n in range(6,15) for m in masti]
# print(koloda)
random.shuffle(koloda)
# print(koloda)
player1 = koloda[:len(koloda)//2]
player2 = koloda[len(koloda)//2:]
print(player1,'---',player2)

player1_count = 0
player2_count = 0

while True:
    hod(player1,player2)
    print(player1_count,player2_count)
    input()
    if not player1 or not player2:
        break