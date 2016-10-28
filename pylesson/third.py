a = 3
print(a)
s = 'Имя'
print(s)
# name = input("Введите имя")
# if name == "Артур":
#     print("Молодец")
# else:
#     print("Не молодец")

pokupki = ['Молоко','Бананы','Урук-хай']
print("У нас сегодня на обед",pokupki[1:3])
pokupki.append('Картошка')
print(pokupki)
pokupki.pop(0)
print(pokupki)
peoples = 'isa', 'isa2'
print(peoples)
pupils = {'Арсен','Артур','Кот','Кот'}
print(pupils)
pupils = pupils & {'Кот','Магомед'}
print(pupils)
pupils = pupils | {'Собака'}
print(pupils)
cool_man = {'имя':'Арсен','фамилия':'Сайдумов','возраст':3}
print(cool_man['имя'])
cool_man['имя'] = 'Руслан'
print(cool_man['имя'], cool_man['возраст'])

i = 5
# print(i+1)
# print(i+2)
# print(i+3)
# print(i+4)
# print(i+5)

while i <= 500:
    print(i)
    i *= 2

while True:
    print(i)
    i *= 2
    if i > 1000:
        break

m = 15
print(hex(m))

for pokupka in pokupki:
    print(pokupka)

for key, value in cool_man.items():
    print(key + ' - ' + str(value))

for i in range(1,10):
    print(i)

for i in range(1,10,2):
    print(i)
else:
    print("Ура")

for i in 'Привет':
    print(i)


