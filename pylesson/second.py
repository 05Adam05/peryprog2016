list1 = ['Иса','Халид','Журналист','Арсен','Гаджи','Алиомар']
print(list1[1])
print(list1[1:4])

print(list1[1:])
print(list1[-1:-5:-1])
print(len(list1))
list1.append('Венера')
print(list1)
list1.extend(['лох1', 'лох2'])
print(list1)
list1.insert(2,'Собака')
print(list1)
del list1[3]
print(list1)
list1.remove('Собака')
print(list1)
list1.pop()
print(list1)
print(list1.pop(6))
print(list1)
list1.sort()
print(list1)
list1.sort(reverse = True)
print(list1)
list1[0] = 5
print(list1)
list2 = list1
# list2[0] = 'чу чух чу чух'
# print(list1)
list2 = list1.copy()
list2 = list1[:]
list2[0] = 'чу чух чу чух'
print(list1)
print(list2)

tuple1 = 'Иса', 'Чупанисаев'

print(tuple1)
# tuple1[0] = 'Магомед'

name, surname = tuple1
print(name)
print(surname)

dict1 = { 'имя': 'Арсен', 'фамилия':'Сайдумов', 'нога': True}
print(dict1['нога'])
dict1['нога'] = False
print(dict1['нога'])
print(dict1.values())
print(dict1.keys())
print(dict1.items())

set1 = {'Ручка', 'Нога', 'Нога', 'Рука'}
print(set1)
set2 = {'Ручка','Собака', 'Кошка'}
print(set1 | set2)
print(set1.union(set2))

print(set1 & set2)
print(set1.intersection(set2))

print(set1 - set2)
print(set1.difference(set2))
print(set2 - set1)

print(set(list1))

print(tuple(set1))



