name = 'Расул'
age = 14
percent_of_coolness = 33.3
print(name + " красавчик. А ему" + str(age) +" лет. " 
 + "Его крутость равна " + str(percent_of_coolness))

print("%10.4s красавчик. А ему %10.5d лет. \
Его крутость равна %10.1f%% " % (name, age, percent_of_coolness))


print("{0} красавчик. А ему {1} лет. \
Его крутость равна {2}% ".format(name,age,percent_of_coolness))

comp_tech = {'Компьютер':'Пентиум3','Принтер':'HP',
'Мышка':'Logitech'}

print("У меня современный комьютер: {0[Компьютер]}, у него \
супер принтер - {0[Принтер]}. И у него есть мышка -- \
{0[Мышка]}. {1}. ".format(comp_tech, 'Что-нибудь еще'))


print("{0:8^10s} красавчик. А ему {1} лет. \
Его крутость равна {2}% ".format(name,age,percent_of_coolness))

import random

num = random.randint(0,1)
print(num)

print("Тинаматомет {0}".format('красавчик' if num else 'малышок'))