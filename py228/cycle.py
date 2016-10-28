i = 5
while i < 50:
    print(i)
    i += 2

while True:
    print(i)
    i += 2
    if i > 100:
        break

good_boys = ['Азамат', 'Баракят','Хаджи-Мурад']

for good_boy in good_boys:
    if good_boy == 'Баракят':
        # break
        continue
    print(good_boy)

azamat = {'имя':'Азамат','фамилия':'Ханов','дата рождения':'05.04.04'}

for element in azamat.keys():
    print(element)


for element in azamat.values():
    print(element)


for key, value in azamat.items():
    print(key + " - " + value)


for i in range(5,19):
    print(i)


for i in range(5,19,3):
    print(i)