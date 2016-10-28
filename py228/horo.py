class WrongDateError(Exception): pass
class WrongMonthError(Exception): pass

while True:
    try:
        birth = input("Введите дату рождения в формате дд.мм.гггг: ")

        date = int(birth[0:2])
        month = int(birth[3:5])
        if date not in range(1,32):
            raise WrongDateError
        if month not in range(1,13):
            raise WrongMonthError
        print(date,month)
        if (date in range(21,32) and month == 3) or \
        (date in range(1,20) and month == 4):
            print("Ты овен")

        break
    except ValueError:
        print("Введи числа нормально.")
    except WrongDateError:
        print("Введи правильный день")
    except WrongMonthError:
        print("Введи правильный месяц")
