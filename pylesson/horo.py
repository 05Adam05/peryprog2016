
# print('По гороскопу ты осел')
while True:
    try:
        birt = input("Введите дату рождения в виде дд.мм.гггг: ")
        date = int(birt[0:2])
        month = int(birt[3:5])
        print(date,month)
        if (date in range(0,21) and month == 4) or \
            (date in range(21,31) and month == 3):
            print("Ты овен")


        break
    except ValueError:
        print("Введи нормальную дату")
        continue