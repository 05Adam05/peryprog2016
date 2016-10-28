# print('Привет')
# d = 5
# print(d)

loxi = ['Тагир', 'Баракят', 'Саид', 'Азамат', 'Ахмет-Хан']

print(loxi[1])
print(loxi[1:])
print(loxi[1:4:2])
print(loxi[1::3])
print(loxi[-1:0:-1])

loxi.append('Тина')
print(loxi)
add1 = ['Саид','Хаджи-Мурад']
loxi.extend(add1)
print(loxi)
loxi.insert(1,'Исак')
print(loxi)

del loxi[4]
print(loxi)
loxi.remove('Баракят')
print(loxi)
loxi.pop()
print(loxi)
print(loxi.pop(3))
print(loxi)

print(loxi.index('Саид'))

loxi[3] = 'Гитинамагомед'

print(loxi)

loxi.sort()
print(loxi)

loxi.sort(reverse = True)
print(loxi)

# loxi2 = loxi
# loxi2[0] = 'Асассина'
# print(loxi)


# loxi2 = loxi.copy()
loxi2 = loxi[:]
loxi2[0] = 'Асассина'
print(loxi)
print(loxi2)

tuple1 = 'Руслан', 'Азамат', 'Путин', 'Гитлер'
print(tuple1[0])
ruslan, azamat,  putin, adolf = tuple1
print(azamat)
print(ruslan)
print(putin)
print(adolf)

set1 = {'Руслан', 'Азамат', 'Путин', 'Гитлер', 'Гитлер'}
print(set1)
set2 = {'Баракята', 'Хаджи-Мурад', 'Путин'}

print(set1 | set2)
print(set1.union(set2))
print(set1 & set2)
print(set1.intersection(set2))
print(set1 - set2)
print(set1.difference(set2))


murad = {'имя':'Мурад','фамилия':'Рустамов','рука': 2}

print(murad)
print(murad['фамилия'])
murad['фамилия'] = "Жужня"
print(murad)
print(murad.values())
print(murad.keys())
print(murad.items())