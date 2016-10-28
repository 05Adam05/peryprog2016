from random import choice
words = {
    'subjects': ['он','Тагир','Анжелика', 'Настя', 'молоток', 'стул', 'помидор', 'чай'],
    'predicates': ['убил','тусил','купил','летел','свистел'],
    'definition': ['милый','здоровый','больной','плохой','желтый']
}

while True:
    try:
        num = int(input("Введите коллчиество предложений: "))
        break
    except ValueError:
        print('Введи число')

for i in range(0,num):
    print('{0} {1} {2} '.format(choice(words['definition']), 
    choice(words['subjects']), choice(words['predicates'])))