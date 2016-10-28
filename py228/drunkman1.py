import random

def get_card(player):
    while True:
        yield player.pop()

def play(player1,player2):
    k = 0
    global player1_count, player2_count
    for card1, card2 in zip(get_card(player1), get_card(player2)):
        k += 2
        print(card1,card2)
        if card1[0] > card2[0]:
            player1_count += k
            break
        elif card1[0] < card2[0]:
            player2_count += k
            break

m = ["Черви", "Пики", "Бубны","Крести"]
deck = [(num, mast) for num in range(2,15) for mast in m]
# print(deck)
random.shuffle(deck)
# print(deck)
player1 = deck[:len(deck)//2]
player2 = deck[len(deck)//2:]
# print(player1,'---',player2)
player1_count = 0
player2_count = 0
while  True:
    play(player1, player2)
    print(player1_count,player2_count)
    input()
    if not player1 or not player2:
        break

