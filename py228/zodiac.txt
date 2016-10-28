class DateError(Exception): pass
class MonthError(Exception): pass

while True:
    try:
        zodiak = input('Введите дату рождения в формате дд.мм.гггг :')
        date = int(zodiak[0:2])
        if date not in range(1,32):
            raise DateError
        month = int(zodiak[3:5])
        if month not in range(1,13):
            raise MonthError
        print (date, month)
        if (date in range(23,31) and month == 12) \
        or (date in range(1,22) and month == 1):
            print('ты козерог')



        break
    except ValueError:
        print('ты чё то не то ввёл')
    except DateError:
        print('введи нормальное число')
    except MonthError:
        print('введи нормальный месяц')

