abdula = [2,3,4]
abdula = iter(abdula)
# print(abdula)
print(next(abdula))
print(next(abdula))
print(next(abdula))
# print(next(abdula))

abdula = [2,3,4]
for i in abdula:
    print(i, end=' ')
print()

abdula = iter([2,3,4])
while True:
    try:
        print(next(abdula), end=' ')
    except StopIteration:
        break
print()

for i in 'Абдулла':
    print(i, end=' ')
print()

abdula2 = [2,3,4,0,-4]
print(len(abdula2),sum(abdula2),min(abdula2),max(abdula2),
    any(abdula2), all(abdula2))

abdula3 = [2,4,6]

for i, j in zip(abdula2, abdula3):
    print(i,j)

names = ['Baracuda1,','UnionOfAbdulla','Kharlik01']

for num, elem in enumerate(names):
    print(num, elem)


i=0
for elem in names:
    print(i, names)
    i+=1

empty_abdulla = []
for i in range(1,51):
    if not i % 2:
        empty_abdulla.append(i)

print(empty_abdulla)

empty_abdulla = [i for i in range(1,51) if not i % 2]
print(empty_abdulla)

names = ['Абдулла','Саид','Абдурахман']
nicknames = ['Union','Hotabich']
true_names = []
for name in names:
    for nickname in nicknames:
        true_names.append((name, nickname))
print(true_names)

true_names = [(name, 
    nickname) for name in names for nickname in nicknames]
print(true_names)

empty_abdulla2 = [i for i in range(1,21) if i != 5 and i !=3]
print(empty_abdulla2)

print(range(1,10))

import random



def rand_range(a,b,c=1):
    for i in range(a,b,c):
        yield random.randint(a,b)

for i in rand_range(1,10):
    print(i, end=' ')
print()


def w_rand_range(a,b,c=1):
    w = list('абвгдеёжзийклмнабдулла')
    for i in range(a,b,c):
        yield random.choice(w)

for i in w_rand_range(1,10):
    print(i, end=' ')
print()