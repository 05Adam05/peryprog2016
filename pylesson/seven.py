lst1 = [5,5,0,2]
lst1 = iter(lst1)
print(next(lst1))
print(next(lst1))
print(next(lst1))
print(next(lst1))
# print(next(lst1))

for i in [5,5,0,2]:
    print(i,end=' ')
print()

lst2 = iter([5,5,0,2])
while True:
    try:
        print(next(lst2),end=' ')
    except StopIteration:
        break
print()

print(tuple(range(5)))

lst1 = [5,5,0,2]

print(sum(lst1),max(lst1),min(lst1),all(lst1),any(lst1))

lst2 = ['f1',5,1]
for i1, i2, i3 in zip(lst1,lst2,('1','2')):
    print(i1, i2, i3)

names = ['Артур','Абдул']
for num, element in enumerate(names):
    print(num, element)

my_list = []
for i in range(1,51):
    if not i % 2:
        my_list.append(i)
print(my_list)

my_list2 = [i for i in range(1,51) if not i % 2]
print(my_list2)

shop_list = []
for i in range(1,4):
    for j in ['молоко','сыр','арсен']:
        shop_list.append((i,j))
print(shop_list)

shop_list = [(i,j) for i in range(1,4)
         for j in ['молоко','сыр','арсен']]

print(shop_list)

import random

def random_gen(a,b,c=1):
    for i in range(a,b,c):
        yield random.randint(a,b)

print(list(random_gen(1,10)))
for i in random_gen(1,15):
    print(i, end=' ')
print()

def bukva_random_gen(a,b,c=1):
    bukvi = list('aбвгдеёжзийклмномпрстуфхцчшщъыьэюя')
    for i in range(a,b,c):
        yield random.choice(bukvi)

for i in bukva_random_gen(1,10):
    print(i, end=' ')
print()

