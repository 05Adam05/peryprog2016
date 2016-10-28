lst1 = [2,3,4]
lst1 = iter(lst1)
# print(lst1)
print(next(lst1))
print(next(lst1))
print(next(lst1))
# print(next(lst1))

lst1 = [2,3,4]
for i in lst1:
    print(i,end=' ')
print()

lst1 = iter([2,3,4])
while True:
    try:
       print(next(lst1),end=' ')
    except StopIteration:
        break
print()

for i in 'abcd':
    print(i)

lst2 = [1,-1,0,5]
print(len(lst2),sum(lst2),min(lst2),max(lst2),all(lst2),any(lst2))

lst3 = [5, 4, 2]
for i, j in zip(lst2, lst3):
    print(i, j)

names =['Тина','Сагид']
for num, name in enumerate(names):
    print(num, name)

g1 = []
for i in range(1,51):
    if not i % 2:
        g1.append(i)

print(g1)

g1 = [i for i in range(1,51) if not i % 2]
print(g1)

names =['Тина','Сагид']
nicknames = ['Тина','Молодчик','Тигр']
two = []
for i in names:
    for j in nicknames:
        two.append((i, j))
print(two)

two = [(i,j) for i in names for j in nicknames ]
print(two)


print(range(1,20))

import random
def rand_range(a,b,c=1):
    for i in range(a,b,c):
        yield random.randint(a,b)

print(rand_range(1,20))

for i in rand_range(1,20):
    print(i,end=' ')
print()


def w_rand_range(a,b,c=1):
    w = list('букв')
    for i in range(a,b,c):
        yield random.choice(w)

for i in w_rand_range(1,20):
    print(i,end=' ')
print()












