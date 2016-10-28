a = 10
while a < 50:
    a += 5
    print(a)
print('-' * 10)
while True:
    a += 5
    print(a)
    if a >= 100:
        break

good_boys = ['Арсен','Гаджимурад','Иван "больше не наш"','Сагид ака "Гепард"']

for good_boy in good_boys:
    if good_boy.startswith('Иван'):
        continue
    print(good_boy)


menu = {'первое':'борщ','второе':'пюрешки','выпить':'компот - "HCL"'}

# for dish in menu.keys():
#     print(dish)

# for dish in menu.values():
#     print(dish)

for key, value in menu.items():
    print(key,' - ',value)

for num in range(5,25):
    print(num)

for num in range(5,25,2):
    print(num)

